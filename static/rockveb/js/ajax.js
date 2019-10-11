$(document).ready(function(){
    $('#company').change(function(){
        let commind = $('#company').val()
        $.ajax({
            type:'GET',
            url:"http://127.0.0.1:8000/socar/rocweb/?commind=" + commind,            
            success: function(data){
                console.log(data)
                $('#qovshaq').html(data)

            }
           
        })
    })

    $('#datepicker').datepicker({
        uiLibrary: 'bootstrap4',
        format: 'yyyy.mm.dd'
    });
    $('#datepicker1').datepicker({
        uiLibrary: 'bootstrap4',
        format: 'yyyy.mm.dd',

    });
    
   
})
