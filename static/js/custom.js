let user = {}
let profile = {}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrf_token = getCookie('csrftoken')

function CheckUsername(){
    var username = $("#username").val()
    var url = $("#username_div").data("url")
    $.ajax({
        data:{
            username
        },
        url: url,
        type: "POST",
        dataType: "json",
        headers: {
            "X-CSRFToken":csrf_token
        },
        beforeSend: ()=>{
            $("#username_btn").text("Checking...")
        },
        success: (res) =>{
            let resp_to_object = JSON.parse(res.user)
            user = resp_to_object[0]
            if(res.message === "Account found"){
                console.log(user)
                $("#welcome_text").removeClass("d-none").text("Welcome "+user.fields.username.toUpperCase()+" "+user.fields.first_name.toUpperCase() +" "+user.fields.last_name.toUpperCase()).addClass("display-6 text-center text-info")
                $("#username_btn").fadeOut("easing")
               $("#username_div").fadeOut("easing")
                $("#password_btn").removeClass("d-none").fadeIn("easing")
               $("#password_div").removeClass("d-none").fadeIn("easing")
            }
        },
        complete: ()=>{
            $("#username_btn").text("Next")
        }
    })
}

function NormalLogin(){
    var password = $("#password").val()
    var url = $("#password_div").data("url")
    $.ajax({
        data:{
            password,
            "username": user.fields.username
        },
        url: url,
        type: "POST",
        dataType: "json",
        headers: {
            "X-CSRFToken":csrf_token
        },
        beforeSend: ()=>{
            $("#password_btn").text("Logging...")
        },
        success: (res) =>{

            if(res.message === "Login successful"){
               window.location.href="/"
            }
        },
        complete: ()=>{
            $("#username_btn").text("Login")
        }
    })
}