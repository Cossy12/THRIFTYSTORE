


function DirectionsToggle(){
    var el = $('#dir-toggle');
    var dir_table = $('#dir-table')
    if (dir_table.attr("hidden") == "hidden") {
      dir_table.fadeIn()
      dir_table.removeAttr("hidden")
      el.html('hide <a href="javascript:void(0)" onclick="DirectionsToggle()">here')
    } else {
      dir_table.fadeOut()
      dir_table.attr("hidden", "hidden")
      el.html('click <a href="javascript:void(0)" onclick="DirectionsToggle()">here')
    }
  }
  
  
  function ShowAlert(title, message, type, redirect){
      
      if (redirect){
        toastr[type](message, title, {
            positionClass: 'toast-bottom-right',
            closeButton: true,
            progressBar: true,
            newestOnTop: true,
            rtl: $("body").attr("dir") === "rtl" || $("html").attr("dir") === "rtl",
            timeOut: 7500,
            onHidden: function () {
              window.location.assign(redirect);
            }
        });
      }
      else{
        toastr[type](message, title, {
            positionClass: 'toast-bottom-right',
            closeButton: true,
            progressBar: true,
            newestOnTop: true,
            rtl: $("body").attr("dir") === "rtl" || $("html").attr("dir") === "rtl",
            timeOut: 7500,
  
        });
  
      }
     
  };
  
  function showPword() {
    var x = document.getElementsByClassName("password");
    for (let i = 0; i < x.length; i++){
        if (x[i].type === "password") {
          x[i].type = "text";
        } else {
          x[i].type = "password";
        }
    }
  }
  
  var temp_button_text;
  
  function CustomFormSubmitPost(e){
      var el = $(e);
      temp_button_text = el.text()
      el.attr('disabled', 'disabled').text("").append('<class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Loading...');
  };
  
  function CustomFormSubmitResponse(e){
      var el = $(e);
      el.removeAttr('disabled').text(temp_button_text);
  };
  
  
  
  "use strict";
  var FormControls = function () {
  
      var usersignup = function () {
  
          var form = $('#signupform')
          form.submit(function(event){
              event.preventDefault();
              CustomFormSubmitPost($('#signupform button[type=submit]'));
  
              grecaptcha.ready(function() {
                grecaptcha.execute(recaptcha_site_key, {action: "/"}).then(function(token) {
  
              
                  var formdata = form.serialize() 
                  $.ajax({
                      url: form.attr("action"),
                      method: form.attr("method"),
                      data: formdata,
                  }) 
              })
              })
  
          })    
      };
  

  
  
      return {
          init: function() { 
              usersignup();
              usersignin(); 
          }
      };
  }();
  

