# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airwet(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.
    airwet = models.SmallIntegerField(db_column='AirWet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AirWet'


class Badmvslist(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    rid = models.IntegerField(db_column='RID', blank=True, null=True)  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BadMVSList'


class Birlik(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    pubname = models.CharField(db_column='PubName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Birlik'


class Company(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pubname = models.CharField(db_column='PubName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Company'


class Constants(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    params = models.CharField(db_column='Params', max_length=50)  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Constants'


class Currparams(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    diffpress = models.FloatField(db_column='DiffPress', blank=True, null=True)  # Field name made lowercase.
    press = models.FloatField(db_column='Press', blank=True, null=True)  # Field name made lowercase.
    temp = models.FloatField(db_column='Temp', blank=True, null=True)  # Field name made lowercase.
    curflow = models.FloatField(db_column='CurFlow', blank=True, null=True)  # Field name made lowercase.
    todayflow = models.FloatField(db_column='TodayFlow', blank=True, null=True)  # Field name made lowercase.
    yesterdayflow = models.FloatField(db_column='YesterdayFlow', blank=True, null=True)  # Field name made lowercase.
    boru = models.FloatField(db_column='Boru', blank=True, null=True)  # Field name made lowercase.
    diaf = models.FloatField(db_column='Diaf', blank=True, null=True)  # Field name made lowercase.
    basedensity = models.FloatField(db_column='BaseDensity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CurrParams'


class Customize(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    birlikid = models.IntegerField(db_column='BirlikID')  # Field name made lowercase.
    mvsstatus = models.IntegerField(db_column='MVSStatus')  # Field name made lowercase.
    mvssign = models.IntegerField(db_column='MVSSign')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customize'


class Disordered(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    curdate = models.DateTimeField(db_column='CurDate')  # Field name made lowercase.
    disordereddate = models.DateTimeField(db_column='DisorderedDate', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disordered'


class Emaillist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmailList'


class Events(models.Model):
    rocid = models.ForeignKey('RocMaster', models.DO_NOTHING, db_column='ROCID')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    operid = models.CharField(db_column='OperID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    oldvalue = models.FloatField(db_column='OldValue', blank=True, null=True)  # Field name made lowercase.
    newvalue = models.FloatField(db_column='NewValue', blank=True, null=True)  # Field name made lowercase.
    descript = models.CharField(db_column='Descript', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Events'


class Gasparams(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    curdate = models.DateTimeField(db_column='CurDate')  # Field name made lowercase.
    basedensity = models.FloatField(db_column='BaseDensity', blank=True, null=True)  # Field name made lowercase.
    n2 = models.FloatField(db_column='N2', blank=True, null=True)  # Field name made lowercase.
    co2 = models.FloatField(db_column='CO2', blank=True, null=True)  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    nc4 = models.FloatField(db_column='nC4', blank=True, null=True)  # Field name made lowercase.
    ic4 = models.FloatField(db_column='iC4', blank=True, null=True)  # Field name made lowercase.
    nc5 = models.FloatField(db_column='nC5', blank=True, null=True)  # Field name made lowercase.
    ic5 = models.FloatField(db_column='iC5', blank=True, null=True)  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7', blank=True, null=True)  # Field name made lowercase.
    c8 = models.FloatField(db_column='C8', blank=True, null=True)  # Field name made lowercase.
    c9 = models.FloatField(db_column='C9', blank=True, null=True)  # Field name made lowercase.
    c10 = models.FloatField(db_column='C10', blank=True, null=True)  # Field name made lowercase.
    h2s = models.FloatField(db_column='H2S', blank=True, null=True)  # Field name made lowercase.
    h2o = models.FloatField(db_column='H2O', blank=True, null=True)  # Field name made lowercase.
    he = models.FloatField(db_column='He', blank=True, null=True)  # Field name made lowercase.
    o2 = models.FloatField(db_column='O2', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    h2 = models.FloatField(db_column='H2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GasParams'


class Gasparamsdaily(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    curdate = models.DateTimeField(db_column='CurDate')  # Field name made lowercase.
    basedensity = models.FloatField(db_column='BaseDensity', blank=True, null=True)  # Field name made lowercase.
    n2 = models.FloatField(db_column='N2', blank=True, null=True)  # Field name made lowercase.
    co2 = models.FloatField(db_column='CO2', blank=True, null=True)  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1', blank=True, null=True)  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2', blank=True, null=True)  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3', blank=True, null=True)  # Field name made lowercase.
    nc4 = models.FloatField(db_column='nC4', blank=True, null=True)  # Field name made lowercase.
    ic4 = models.FloatField(db_column='iC4', blank=True, null=True)  # Field name made lowercase.
    nc5 = models.FloatField(db_column='nC5', blank=True, null=True)  # Field name made lowercase.
    ic5 = models.FloatField(db_column='iC5', blank=True, null=True)  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6', blank=True, null=True)  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7', blank=True, null=True)  # Field name made lowercase.
    c8 = models.FloatField(db_column='C8', blank=True, null=True)  # Field name made lowercase.
    c9 = models.FloatField(db_column='C9', blank=True, null=True)  # Field name made lowercase.
    c10 = models.FloatField(db_column='C10', blank=True, null=True)  # Field name made lowercase.
    h2s = models.FloatField(db_column='H2S', blank=True, null=True)  # Field name made lowercase.
    h2o = models.FloatField(db_column='H2O', blank=True, null=True)  # Field name made lowercase.
    he = models.FloatField(db_column='He', blank=True, null=True)  # Field name made lowercase.
    o2 = models.FloatField(db_column='O2', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    h2 = models.FloatField(db_column='H2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GasParamsDaily'


class Histcolname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pointtype = models.IntegerField(db_column='PointType')  # Field name made lowercase.
    paramnum = models.IntegerField(db_column='ParamNum')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isgas = models.SmallIntegerField(db_column='isGas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistColName'


class Histdaily(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    histcolid = models.IntegerField(db_column='HistColID')  # Field name made lowercase.
    histdate = models.DateTimeField(db_column='HistDate')  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistDaily'


class Histhour(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    histcolid = models.IntegerField(db_column='HistColID')  # Field name made lowercase.
    histdate = models.DateTimeField(db_column='HistDate')  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistHour'


class Histtype(models.Model):
    histtype = models.IntegerField(db_column='HistType', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistType'


class Limitcontrol(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    minvalue = models.FloatField(db_column='MinValue', blank=True, null=True)  # Field name made lowercase.
    maxvalue = models.FloatField(db_column='MaxValue', blank=True, null=True)  # Field name made lowercase.
    param = models.IntegerField(db_column='Param')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LimitControl'


class Logs(models.Model):
    ip = models.CharField(db_column='IP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    curdate = models.DateTimeField(db_column='CurDate', blank=True, null=True)  # Field name made lowercase.
    mvsid = models.IntegerField(db_column='MVSID', blank=True, null=True)  # Field name made lowercase.
    histcolid = models.IntegerField(db_column='HistColID', blank=True, null=True)  # Field name made lowercase.
    histdate = models.DateTimeField(db_column='HistDate', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    oldvalue = models.DecimalField(db_column='OldValue', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    newvalue = models.DecimalField(db_column='NewValue', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Logs'


class Mvsname(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pubname = models.CharField(db_column='PubName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mvsno = models.IntegerField(db_column='MVSNo')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rocid = models.IntegerField(db_column='ROCID')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    borudiam = models.FloatField(db_column='BoruDiam', blank=True, null=True)  # Field name made lowercase.
    diafdiam = models.FloatField(db_column='DiafDiam', blank=True, null=True)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    air = models.SmallIntegerField(db_column='Air', blank=True, null=True)  # Field name made lowercase.
    wet = models.SmallIntegerField(db_column='Wet', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MVSName'


class Mvspcuname(models.Model):
    mvsid = models.IntegerField()
    pcu_roc_hist = models.CharField(max_length=20)
    pcu_mvs = models.CharField(max_length=20)
    pcu_rtu = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'MVSPCUName'


class Minhourday(models.Model):
    rocid = models.IntegerField(db_column='ROCID')  # Field name made lowercase.
    chmin = models.SmallIntegerField(db_column='chMin')  # Field name made lowercase.
    chhour = models.IntegerField(db_column='chHour')  # Field name made lowercase.
    chday = models.SmallIntegerField(db_column='chDay')  # Field name made lowercase.
    hourtime = models.IntegerField(db_column='HourTime', blank=True, null=True)  # Field name made lowercase.
    hourbegindt = models.DateTimeField(db_column='HourBeginDT', blank=True, null=True)  # Field name made lowercase.
    hourenddt = models.DateTimeField(db_column='HourEndDT', blank=True, null=True)  # Field name made lowercase.
    daytime = models.IntegerField(db_column='DayTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MinHourDay'


class Modemconntime(models.Model):
    conntime = models.DateTimeField(db_column='ConnTime', blank=True, null=True)  # Field name made lowercase.
    conduration = models.FloatField(db_column='Conduration', blank=True, null=True)  # Field name made lowercase.
    oprmode = models.CharField(db_column='OPRMode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rocid = models.ForeignKey('RocMaster', models.DO_NOTHING, db_column='ROCID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('UserMaster', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModemConnTime'


class Permission(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Permission'


class Pointdescription(models.Model):
    pointtype = models.IntegerField(db_column='PointType', blank=True, null=True)  # Field name made lowercase.
    paramnumber = models.IntegerField(db_column='ParamNumber', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointDescription'


class Pubhistdaily(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    histcolid = models.IntegerField(db_column='HistColID')  # Field name made lowercase.
    histdate = models.DateTimeField(db_column='HistDate')  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PubHistDaily'


class Pubhisthour(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    histcolid = models.IntegerField(db_column='HistColID')  # Field name made lowercase.
    histdate = models.DateTimeField(db_column='HistDate')  # Field name made lowercase.
    value = models.FloatField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PubHistHour'


class Rochistpoint(models.Model):
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    pointindex = models.SmallIntegerField(db_column='PointIndex')  # Field name made lowercase.
    histcolid = models.IntegerField(db_column='HistColID')  # Field name made lowercase.
    histtypeid = models.IntegerField(db_column='HistTypeID')  # Field name made lowercase.
    checked = models.SmallIntegerField(db_column='Checked')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROCHistPoint'


class RocMaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pubname = models.CharField(db_column='PubName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    air = models.IntegerField(db_column='Air', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    stationid = models.ForeignKey('Station', models.DO_NOTHING, db_column='StationID', blank=True, null=True)  # Field name made lowercase.
    defconntype = models.SmallIntegerField(db_column='DefConnType', blank=True, null=True)  # Field name made lowercase.
    date = models.IntegerField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    rocip = models.CharField(db_column='ROCIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rocno = models.IntegerField(db_column='ROCNo', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)  # Field name made lowercase.
    bdate = models.DateTimeField(db_column='BDate', blank=True, null=True)  # Field name made lowercase.
    x = models.IntegerField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.IntegerField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    base = models.IntegerField(db_column='Base', blank=True, null=True)  # Field name made lowercase.
    dstunit = models.IntegerField(db_column='dstUnit', blank=True, null=True)  # Field name made lowercase.
    dstgroup = models.IntegerField(db_column='dstGroup', blank=True, null=True)  # Field name made lowercase.
    timediff = models.IntegerField(db_column='TimeDiff', blank=True, null=True)  # Field name made lowercase.
    isitritechservice = models.BooleanField(db_column='isITRITechService', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROC_MASTER'


class Reason(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reason'


class Route(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID')  # Field name made lowercase.
    ischrom = models.BooleanField(db_column='isChrom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Route'


class Routepopupmenu(models.Model):
    routeid = models.IntegerField(db_column='RouteID')  # Field name made lowercase.
    mvsid = models.IntegerField(db_column='MVSID')  # Field name made lowercase.
    ischequie = models.BooleanField(db_column='isChequie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoutePopupMenu'


class Saveselroc(models.Model):
    selrocname = models.CharField(db_column='SelRocName', max_length=100)  # Field name made lowercase.
    rocid = models.IntegerField(db_column='ROCID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SaveSelRoc'


class Station(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Station'


class UserMaster(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    namenew = models.CharField(db_column='NameNew', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status')  # Field name made lowercase.
    stationid = models.IntegerField(db_column='StationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_MASTER'


class Userpermission(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    pid = models.ForeignKey(Permission, models.DO_NOTHING, db_column='PID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserPermission'


class Userudlroclist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='UID')  # Field name made lowercase.
    rocid = models.IntegerField(db_column='ROCID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserUdlROCList'
