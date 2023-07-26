from django.db import models
from app.models import Commune


GENDER = (
    ('masculin', 'Masculin'),
    ('feminin', 'Feminin')
)
class Etudiant(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    nom = models.CharField("Nom", max_length=20)
    prenom = models.CharField("Prénom", max_length=20)
    genre = models.CharField("Genre", max_length=10, choices=GENDER)
    année_naissance = models.PositiveIntegerField("Année_naissance")
    
    def __str__(self) -> str:
        return self.nom+" "+self.prenom+" "+self.genre+" "+str(self.année_naissance) 
    
    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['nom', 'prenom','genre', 'année_naissance'],
                name = 'unique_etudiant'
            )
        ]
    