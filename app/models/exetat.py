from django.db import models
from app.models import Section_cours



class Exetat(models.Model):
    section_cours = models.ForeignKey(Section_cours, on_delete=models.CASCADE)
    edition = models.PositiveIntegerField("Edition")
    
    
    def __str__(self) -> str:
        return str(self.edition)
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint
            (
                fields = ['edition'],
                name = 'unique.exetat'
            )
        ]
    
    