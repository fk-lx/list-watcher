$(document).ready(function(){
    $('#mail-table').dataTable({
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>"
    });

    $.extend( $.fn.dataTableExt.oStdClasses, {
        "sWrapper": "dataTables_wrapper form-inline"
    } );

    $('.mailTags').tagit({
            readOnly: true,
            allowSpaces: false
    });
});
