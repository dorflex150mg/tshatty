from django import forms

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
               "name",
               "password"
               ]
        widgets = {
               "password" : forms.PasswordInput()
               }

        def is_valid_user(fname, fpassword):
            user_model = User.objects.get(name=fname)
            if(user_model.password == user_form['password'].value()):
                return True
            return False
