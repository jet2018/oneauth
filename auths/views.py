from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import  TemplateView
from auths.models import Company, Application
from auths.modules import generate_random_string, Check_username_holder
from .models import Profile
from django.core import  serializers
import jwt

@csrf_exempt
def authorize(request, sec_key):
    """
    Authenticate a user
    """
    try:
        check_application = Application.objects.get(token=sec_key)
        if request.method == "POST" or request.is_ajax():
            """ 
            Check password.
            This assumes one has already CheckEmailOrUsernameOrPhone to check email or phone or username
            This will check the password and then release token
            """
            get_password = request.POST.get("password")
            get_username = request.POST.get("username")

            user = auth.authenticate(username=get_username, password = get_password)
            if user is not None:
                # add the user in subscribers
                if not check_application.subscribers.filter(id=user.id).exists():
                    check_application.subscribers.add(user)
                else:
                    pass

                # will handle 2fA from here

                data = {
                    "avatar": user.profile.avatar.url if user.profile.avatar else None,
                    "full_name": user.get_full_name(),
                    "username": user.username,
                    "email": user.email if user.email else None,
                    "id": user.pk,
                    "phone": user.profile.phone if user.profile.phone else None
                }
                 # release a jwt token
                token = jwt.encode(payload=data, key=generate_random_string(60))
                application = serializers.serialize("json", [check_application], fields=("redirect_url", ""))
                return JsonResponse({"token": token, "application":application})
        else:
            pass
    except Application.DoesNotExist:
            return redirect("auths:unknown_token")
    return render(request, 'auths/authorise.html', {'application': check_application, "token":check_application.token})


def CheckEmailOrUsernameOrPhone(request):
    if request.method == 'POST' or request.is_ajax():
        username = request.POST.get("username")
        check_user = dict()

        user = None
        # handle with email
        if username is not None:
            user = Check_username_holder(username, Profile)

        user_to_json = dict()
        profile = dict()

        if user:
            found_user = user.user
            message="Account found"
            user_to_json = serializers.serialize('json', [found_user], fields=("first_name", "last_name", "email", "username" ))
            profile = serializers.serialize('json', [user], fields=("avatar", "phone"))
        else:
            message = "No user account is associated with the given details"
        return JsonResponse({"message": message, "user": user_to_json, "profile":profile})

def Check_User_Password(request):
    if request.method == "POST" or request.is_ajax():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return JsonResponse({"message": "Login successful"})
        else:
            return JsonResponse({"message": "Login failed, password is wrong"})
    return render(request, "auths/authorise.html", {"token":False})


class Error_Unknown_Token(TemplateView):
    # error handling page
    template_name = "errors/unknown_token.html"

class SplashScreen(TemplateView):
    # splash screen
    template_name ="splash.html"