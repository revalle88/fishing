function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}


$(function () {
       $(".delete").click(function(){
                var id_number = this.id;
                alert(id_number);
                $.ajax({
                   type: 'DELETE',
                   headers: { "X-CSRFToken": getCookie("csrftoken") },
                   url: '/basic-upload/',
                   data: 'photo_id='+id_number,
                   success: function(){
                      if(data) {alert("Success!")}
                    }
                })
       })
  });

