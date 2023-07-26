from django.db import models
from app.models import Section
from app.models import Cours


class Section_cours(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    
    
    
    def __str__(self) -> str:
            return self.section.nom+" - "+self.cours.nom