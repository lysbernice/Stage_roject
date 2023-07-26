from django.contrib.auth.forms import UserCreationForm
from app.models import User

class UtilisateurForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'telephone',
            'username',
            'password1',
            'password2',
            'genre',
            'zone',
            'role',
            'is_staff'
        ]