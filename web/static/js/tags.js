$(document).ready(function(){
   $('ul').on('click', '.edit', function(){
       var editInput = $('<input type=text>');
       $(this).closest('div').attr('visible', 'false');

   });

    /*$(".click").editable('/tags/edit/', {
        tooltip : "Click to edit...",
        style : "inherit"

    });*/

    $("body").on('click', '.click', function(){
        $(this).editable('/tags/edit/', {
            tooltip : "Click to edit...",
            style : "inherit"
        });
    });


   $('ul').on('click', '.delete', function(){
       var parent = $(this).closest('li');
       var id = $(this).attr('data-id');
       parent.remove();
       $.ajax({
            url: '/tags/delete',
            type: 'DELETE',
            dataType: 'json',
            contentType: 'application/json',
            data: '{ "id":' + id +"}"
       });
   });

    $('#addform').submit(function(e){
        e.preventDefault();
        var name = $('#tagName').val();
        var ul = $('#tag-list');
        $.ajax({
            url: '/tags/add',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: '{ "name": "' + name +'"}',
            success: function(data)
            {
                ul.append('<li id="'+data.id+'"><div class="click" id="'+data.id+'">'
                    + name +
                    '</div> <span id="delete" data-id="'+data.id+'"class="glyphicon glyphicon-remove delete" ></span></li>');

            }
        });
    })
});