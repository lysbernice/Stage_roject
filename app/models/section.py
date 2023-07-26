from django.db import models



class Section(models.Model):
    nom=models.CharField("Nom", max_length=20, unique=True)
    
    
    def __str__(self) -> str:
        return self.nom