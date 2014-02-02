$(document).ready(function(){
    $('#mail-table').dataTable({
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>"
    });

    $.extend( $.fn.dataTableExt.oStdClasses, {
        "sWrapper": "dataTables_wrapper form-inline"
    } );


    $('#remark-form').submit(function(event){
        var ident = $('#ident').val();
        var remark = $('#remark').val();
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url:  '/mails/',
            data: { ident: ident, remark: remark}
        });
    });
});
