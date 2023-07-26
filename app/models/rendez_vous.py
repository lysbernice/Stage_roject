from django.db import models


GENDER = (
    ('masculin', 'Masculin'),
    ('feminin', 'Feminin')
)

TYPE_DOCUMENTS = (
    ('attestation de réussite', 'Attestation de réussite'),
    ('relèvé des points', 'Relèvé des points'),
    ('attestation de participation au concours National', 'Attestation de participation au concours National'),
    ('attestation de participation à l_examen d_etat', 'Attestation de participation à l_examen d_etat')
)

class Rendez_vous(models.Model):
    nom = models.CharField("Nom", max_length=20)
    prenom = models.CharField("Prenom", max_length=20)
    email = models.EmailField("Email", max_length=100)
    gender = models.CharField("Genre", max_length=10, choices=GENDER)
    code_centre = models.PositiveIntegerField("Code_centre")
    code_participation = models.PositiveIntegerField("Code_participation")
    code_ecole = models.PositiveIntegerField("Code_école")
    type_documents = models.CharField("Type de document", max_length=50, choices=TYPE_DOCUMENTS)
    edition = models.PositiveIntegerField("Edition")
    date_demande = models.DateField("Date de demande", auto_now_add=True)
    date_delivrance = models.DateField("Date de delivrance",null=True, blank=True)
    
    
    def __str__(self) -> str:
        return self.nom+" "+self.prenom+" "+self.type_documents+" "+self.edition
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nom', 'prenom', 'code_centre', 'code_participation', 'code_ecole', 'type_documents', 'edition'],
                name = 'unique.rendez_vous'
            )
        ]
    