from django.shortcuts import render
from actors.models import User
from actors.forms import UserForm

def home_view(request, *args, **kwargs):
    user_form = UserForm(request.GET or None)
    context = {
            "form": user_form
            }
    if user_form.is_valid():
        context = {
                "name": user_form['name'].value()
                }
        if user_form._meta.is_valid_user(form.name, form.pswd):
            return render(request, "main.html", context)
        else:
            return render(request, "wrong_pswd.html", context)
    return render(request, "home.html", context)


def main_view(request, *args, **kwargs):
    user_name = kwargs['name']
    this_user = User.objects.get(name=user_name)
    friends_obj = Friend.objects.filter(user=this_user)
    friends = [friend.name for friend in friends_obj]
    context = {
            "friends": friends,
            "user_name": user_name
            }
    return render(request, "main.html", context)

# Create your views here.
