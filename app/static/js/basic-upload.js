$(function () {
  /* 1. OPEN THE FILE EXPLORER WINDOW */
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
  $("#fileupload").fileupload({
    dataType: 'json',
    done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
      if (data.result.is_valid) {
        $("#gallery").prepend(
          "<div id='photo_container_"+ data.result.id +"><a href='" + data.result.url + "'><img src = '" + data.result.url + "' class = 'fish_icon_medium'></a><button class = 'delete' id="+ data.result.id +">delete</button></div>"
        )
      }
    }
  });

});


