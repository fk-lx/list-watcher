$(document).ready(function(){
   $('.edit').click(function(){

   });

   $('ul').on('click', '.delete', function(){
       var parent = $(this).closest('li');
       var id = $(this).attr('data-id');
       $.ajax({
            url: '/tags/delete',
            type: 'DELETE',
            dataType: 'json',
            contentType: 'application/json',
            data: '{ "id":' + id +"}",
            success : function()
            {
                parent.remove();
            }
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
                ul.append('<li id="'+data.id+'">'
                    + name +
                    '<span data-id="'
                    +data.id+'" class="glyphicon glyphicon-edit edit" ></span> <span id="delete" data-id="'+data.id+'"class="glyphicon glyphicon-remove delete" ></span></li>');

            }
        });
    })
});