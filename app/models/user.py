from django.db import models
from phone_field import PhoneField
from app.models import Zone
from django.contrib.auth.models import AbstractUser

ROLE = (
    ('administrateur','Administrateur'),
    ('organisateur','Organisateur'),
    ('agent_de_saisie','Agent de saisie'),
    ('receptioniste','Receptioniste')
)
GENDER = (
    ('masculin', 'Masculin'),
    ('feminin', 'Feminin')
)
class User(AbstractUser):
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    genre = models.CharField("Genre", max_length=10, choices=GENDER)
    telephone = PhoneField("Téléphone", blank = True)
    role = models.CharField("Rôle", max_length=20, choices=ROLE)
    
    
    def __str__(self) -> str:
        return self.role+": "+self.nom+""+self.prenom
    