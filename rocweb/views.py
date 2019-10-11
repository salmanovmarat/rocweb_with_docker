from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .render import Render
from datetime import timedelta


def store_restructurizator_hourly(store):
    mydict = {}
    for st in store:
        date = (st[15] - timedelta(minutes=1)).strftime("%d.%.m.%Y")
        if date not in mydict:
            mydict[date] = []
        mydict[date].append(st)
    return mydict


def store_restructurizator_daily(store):
    mydict = {
        'qovsaqlar': {}
    }
    for st in store:
        date = st[15].strftime("%d.%m.%Y")
        if date not in mydict['qovsaqlar']:
            mydict['qovsaqlar'][date] = []
        mydict['qovsaqlar'][date].append(st)
    return mydict


def login_view(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT id,namenew,password FROM Birlik')
        birlik = cursor.fetchall()
    if request.method == 'POST':
        request.session['birlik'] = request.POST.get('birlik')
        birliy = request.POST.get('birlik')
        password = request.POST.get('password')
        for bir in birlik:
            if birliy == str(bir[0]) and password == bir[2]:
                return redirect('home')
        else:
            messages.info(request, 'Şifrəni düzgün daxil edin')
            return redirect('login')
        return redirect('home')
    return render(request, 'login.html', {'birlik': birlik})


# @login_required(login_url=reverse_lazy('login'))
def home(request):
    formalar = [(1, "Gunluk"), (2, 'Ayliq'), (3, 'Yekun'), (4, "Enerji"),
                (5, "Boru,Diafraqma"), (6, 'Nasazliqlar siyahisi'), (7, 'Qazin terkibi')]
    forms = [(1, "PDF"), (2, "MSWord"), (3, "MSExcel")]
    birind = request.session['birlik']
    with connection.cursor() as cursor:
        cursor.execute(""" SELECT MVS.ID ID, MVS.PubName Name
                        FROM   Customize C INNER JOIN 
                        MVSName MVS ON C.MVSID = MVS.ID
                        WHERE  C.BirlikID  = """ + birind + """
                        AND MVS.ISACTIVE = 1 GROUP BY MVS.ID, MVS.PubName
                        ORDER BY MVS.PubName """)
        qovshaq = cursor.fetchall()
        cursor.execute(""" SELECT CompanyID, NameNew
                        FROM   Customize INNER JOIN
                        Company  ON Customize.CompanyID = Company.ID
                        WHERE  BirlikID = """ + birind + """
                        GROUP BY CompanyID, NameNew
                        ORDER BY CompanyID""")
        company = cursor.fetchall()
        context = {
            'companies': company,
            'qovshaq': qovshaq,
            'formalar': formalar,
            'forms': forms,
        }
        if request.is_ajax():
            commind = request.GET.get('commind')
            cursor.execute(""" SELECT MVS.ID ID, MVS.PubName namenew
                            FROM   Customize C INNER JOIN
                            MVSName MVS ON C.MVSID = MVS.ID
                            WHERE  (C.BirlikID  = """ + birind + """) AND MVS.ISACTIVE = 1
                            AND (C.CompanyID = """ + commind + """ ) 
                            GROUP BY MVS.ID, MVS.PubName ORDER BY MVS.PubName """)
            qovshaq1 = cursor.fetchall()
            context.update(qovshaq=qovshaq1)
            return render(request, 'ajax_template/qovshaq_list.html', context)

        if request.method == "POST":
            commind = request.POST.get('commind')
            start_date = request.POST.get('time1')
            end_date = request.POST.get('time2')
            mvsname = request.POST.get('mvsname')
            pubhist = request.POST.get('gender')
            cursor.execute(
                f"EXEC [dbo].[RAPORDaily] @p_TableName=%s,@p_BHistDate =%s, @p_EHistDate=%s, @p_BirlikId= %s, @p_CompanyId= %s ,@p_MVSID = %s, @p_PrintForm=0, @p_IsView=1", [f'PubHist{pubhist}', f'{start_date} 1:00:00', f'{end_date} 0:00:00', birind, commind, mvsname])
            store = cursor.fetchall()

            if pubhist == 'Daily':
                store = store_restructurizator_daily(store)
            elif pubhist == 'Hour':
                store = store_restructurizator_hourly(store)
            context.update({'store': store, 'pubhist': pubhist})

            if 'pdf' in request.POST:
                return Render.render('report.html', context)
            return render(request, 'home.html', context)
    return render(request, 'home.html', context)
