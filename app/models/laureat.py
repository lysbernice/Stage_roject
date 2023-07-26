from django.db import models
from app.models import Etudiant, Exetat


class Laureat(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    exetat = models.ForeignKey(Exetat, on_delete=models.CASCADE)
    code_centre = models.PositiveIntegerField("code_centre")
    code_participation = models.PositiveIntegerField("code_participation")
    code_ecole = models.PositiveIntegerField("code_école")
    
    
    def __str__(self) -> str:
        return self.etudiant.nom+" "+self.etudiant.prenom+" Exetat : "+str(self.exetat.edition)+" Code centre : "+str(self.code_centre)+" Code Participation : "+str(self.code_participation)+" Code école : "+str(self.code_ecole)+" "+str(self.edition)
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint
            (
                fields = ['code_centre', 'code_participation', 'code_ecole', 'exetat'],
                name = 'unique.laureat'
            )
        ]
    