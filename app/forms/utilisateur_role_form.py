from django.contrib.auth.forms import UserChangeForm 
from app.models import User



class UserEditForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ['role']