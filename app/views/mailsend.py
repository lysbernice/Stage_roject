from django.core.mail import send_mail
from django.conf import settings
import string
from io import BytesIO
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from django.http import HttpResponse
import qrcode
import json
import io
from PIL import Image
from datetime import datetime
from qrcode.constants import ERROR_CORRECT_L
from app.models import Rendez_vous
from reportlab.pdfgen import canvas


def date_generate ():
    dates = Rendez_vous.objects.values('date_delivrance')
    for i in range(0,len(dates)):
        date_delivrance = list(dates[i].values())[0]
    
    occurance = Rendez_vous.objects.filter(date_delivrance = date_delivrance).count()
    date = {}
    date[date_delivrance]=occurance
    return date

def test():
    dates = date_generate()
    if dates.values() <=9:
        pass
    else:
        pass
# def EmailConfirmation (request, mail):
#     dates = Rendez_vous.objects.filter(email = mail).values('date_delivrance')
#     for i in range(0,len(dates)):
#         date_delivrance = list(dates[i].values())[0]
#     send_mail(
#         subject="Confirmation de votre demande de document",
#         from_email=None,
#         message='Votre demande a été envoyée avec succés, vous devez donc payer le montant exigés afin de récupérer votre document le {}.'.format(date_delivrance),
#         recipient_list=[mail],
#         fail_silently=False
#     )

# def EmailConfirmation(request, email):
   
#     dates = date_generate()
#     date_delivrance = list(dates.keys())[0]
#     # bets = Rendez_vous.objects.filter(email = mail)
#     bets = Rendez_vous.objects.values('id')
#     count = Rendez_vous.objects.all().count()
#     ids=[]
#     for i in range(count):
#         ids.append(list(bets[i].values())[0])
#     bets = Rendez_vous.objects.filter(id = ids[count - 1])
#     nom = list(bets.values('nom'))[0]
#     nom = list(nom.values())[0]
#     prenom = list(bets.values('prenom'))[0]
#     prenom = list(prenom.values())[0]
#     type_documents = list(bets.values('type_documents'))[0]
#     type_documents = list(type_documents.values())[0]
    
#     # Créer un PDF à partir du message avec la mise en forme spécifiée
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter)
#     styles = getSampleStyleSheet()
    
#       # Titre principal
#     title_style = ParagraphStyle(name='TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=10, fontName='Helvetica-Bold')
#     title = Paragraph("<u>Récépissé de Demande de document</u>", title_style)
#     # Petit paragraphe en bas du titre
#     paragraph_style = ParagraphStyle(name='ParagraphStyle', parent=styles['Normal'], alignment=1)
#     paragraph = Paragraph("<b>En réponse à votre demande de document, vous êtes invité(e) à vous présenter à notre Bureau de l'evaluation, les dates suivantes : {}</b>".format(date_delivrance), paragraph_style)
    
#      # Informations sur l'utilisateur
#     user_info_style = ParagraphStyle(name='UserInfoStyle', parent=styles['Normal'], alignment=0, spaceAfter=10)
#     user_info = Paragraph("Nom: <b>{}</b><br/>Prénom: <b>{}</b><br/>Email: <b>{}</b><br/>Type de document demandé: <b>{}</b><br/>Date de rendez-vous: <b>{}</b>".format(nom, prenom, email, type_documents, date_delivrance), user_info_style)

#     # Génération du QR code
#     qr_code = qrcode.make(f"Nom: {nom}\nPrénom: {prenom}\nEmail:{email}\nType de document demandé: {type_documents}\nDate de rendez-vous: {date_delivrance}")
#     #qr_code_path = "qr_code.png"
#     qr_code_path = "./QRCode/qr_code.png"
#     qr_code.save(qr_code_path)
    
#     # Créer une image à partir du fichier PNG du code QR
#     qr_code_img = ImageReader(qr_code_path)

#     # Créer un objet BytesIO à partir des données binaires de l'image
#     qr_code_data = io.BytesIO(qr_code_img.getData())

#     # Créer une instance de ImageReader à partir de l'objet BytesIO
#     qr_code_reader = ImageReader(qr_code_data)
    
#     # Ajout des éléments au PDF
#     elements = [title, Spacer(1, 20), paragraph, Spacer(1, 20), user_info, Spacer(1, 20), Image(qr_code_reader, width=50*mm, height=50*mm)]
#     doc.build(elements)
    
#     # Convertir le PDF en bytes
#     pdf = buffer.getvalue()
#     buffer.close()
    
#     # Envoyer l'e-mail avec le PDF en pièce jointe
#     email = EmailMessage(
#         subject="Confirmation de votre demande de document",
#         body='Votre demande a été envoyée avec succés, vous devez donc payer le montant exigés afin de récupérer votre document le {}.'.format(date_delivrance),
#         from_email=None,
#         to=[email],
#     )
#     email.attach("document.pdf", pdf, "application/pdf")
#     email.send()

# def EmailConfirmation(request, email):
   
#     dates = date_generate()
#     date_delivrance = list(dates.keys())[0]
#     # bets = Rendez_vous.objects.filter(email = mail)
#     bets = Rendez_vous.objects.values('id')
#     count = Rendez_vous.objects.all().count()
#     ids=[]
#     for i in range(count):
#         ids.append(list(bets[i].values())[0])
#     bets = Rendez_vous.objects.filter(id = ids[count - 1])
#     nom = list(bets.values('nom'))[0]
#     nom = list(nom.values())[0]
#     prenom = list(bets.values('prenom'))[0]
#     prenom = list(prenom.values())[0]
#     type_documents = list(bets.values('type_documents'))[0]
#     type_documents = list(type_documents.values())[0]
    
#     # Créer un PDF à partir du message avec la mise en forme spécifiée
#     buffer = BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter)
#     styles = getSampleStyleSheet()
    
#       # Titre principal
#     title_style = ParagraphStyle(name='TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=10, fontName='Helvetica-Bold')
#     title = Paragraph("<u>Récépissé de Demande de document</u>", title_style)
#     # Petit paragraphe en bas du titre
#     paragraph_style = ParagraphStyle(name='ParagraphStyle', parent=styles['Normal'], alignment=1)
#     paragraph = Paragraph("<b>En réponse à votre demande de document, vous êtes invité(e) à vous présenter à notre Bureau de l'evaluation, les dates suivantes : {}</b>".format(date_delivrance), paragraph_style)
    
#      # Informations sur l'utilisateur
#     user_info_style = ParagraphStyle(name='UserInfoStyle', parent=styles['Normal'], alignment=0, spaceAfter=10)
#     user_info = Paragraph("Nom: <b>{}</b><br/>Prénom: <b>{}</b><br/>Email: <b>{}</b><br/>Type de document demandé: <b>{}</b><br/>Date de rendez-vous: <b>{}</b>".format(nom, prenom, email, type_documents, date_delivrance), user_info_style)

#     # Génération du QR code
#     qr_code = qrcode.make(f"Nom: {nom}\nPrénom: {prenom}\nEmail:{email}\nType de document demandé: {type_documents}\nDate de rendez-vous: {date_delivrance}")
#     #qr_code_path = "qr_code.png"
#     qr_code_path = "./QRCode/qr_code.png"
#     qr_code.save(qr_code_path)
    
#     # Créer un nouveau PDF
#     pdf_buffer = BytesIO()
#     pdf = canvas.Canvas(pdf_buffer)
#     pdf.drawString(50, 700, f"Nom : {nom}")
#     pdf.drawString(50, 680, f"Prénom : {prenom}")
#     pdf.drawString(50, 660, f"Email : {email}")
#     pdf.drawString(50, 640, f"Type de document demandé : {type_documents}")
#     pdf.drawString(50, 620, f"Date de rendez-vous : {date_delivrance}")
#     qr_code_path = "./QRCode/qr_code.png"
#     pdf.drawImage(qr_code_path, 100, 100, 50)
#     pdf.save()

#     # Convertir le PDF en bytes
#     pdf_bytes = pdf_buffer.getvalue()
    
#     # Envoyer l'e-mail avec le PDF en pièce jointe
#     email = EmailMessage(
#         subject="Confirmation de votre demande de document",
#         body='Votre demande a été envoyée avec succés, vous devez donc payer le montant exigés afin de récupérer votre document le {}.'.format(date_delivrance),
#         from_email=None,
#         to=[email],
#     )
#     email.attach("document.pdf", pdf_bytes, "application/pdf")
#     email.send()


def EmailConfirmation(request, email):
   
    dates = date_generate()
    date_delivrance = list(dates.keys())[0]
    # bets = Rendez_vous.objects.filter(email = mail)
    bets = Rendez_vous.objects.values('id')
    count = Rendez_vous.objects.all().count()
    ids=[]
    for i in range(count):
        ids.append(list(bets[i].values())[0])
    bets = Rendez_vous.objects.filter(id = ids[count - 1])
    nom = list(bets.values('nom'))[0]
    nom = list(nom.values())[0]
    prenom = list(bets.values('prenom'))[0]
    prenom = list(prenom.values())[0]
    type_documents = list(bets.values('type_documents'))[0]
    type_documents = list(type_documents.values())[0]
    
    # Créer un PDF à partir du message avec la mise en forme spécifiée
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
      # Titre principal
    title_style = ParagraphStyle(name='TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=10, fontName='Helvetica-Bold')
    title = Paragraph("<u>Récépissé de Demande de document</u>", title_style)
    # Petit paragraphe en bas du titre
    paragraph_style = ParagraphStyle(name='ParagraphStyle', parent=styles['Normal'], alignment=1)
    paragraph = Paragraph("<b>En réponse à votre demande de document, vous êtes invité(e) à vous présenter à notre Bureau de l'evaluation, les dates suivantes : {}</b>".format(date_delivrance), paragraph_style)
    
     # Informations sur l'utilisateur
    user_info_style = ParagraphStyle(name='UserInfoStyle', parent=styles['Normal'], alignment=0, spaceAfter=10)
    user_info = Paragraph("Nom: <b>{}</b><br/>Prénom: <b>{}</b><br/>Email: <b>{}</b><br/>Type de document demandé: <b>{}</b><br/>Date de rendez-vous: <b>{}</b>".format(nom, prenom, email, type_documents, date_delivrance), user_info_style)

    # Génération du QR code
    qr_code = qrcode.make(f"Nom: {nom}\nPrénom: {prenom}\nEmail:{email}\nType de document demandé: {type_documents}\nDate de rendez-vous: {date_delivrance}")
    #qr_code_path = "qr_code.png"
    qr_code_path = "./QRCode/qr_code.png"
    qr_code.save(qr_code_path)
    
    # Créer un nouveau PDF
    pdf_buffer = BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)
    
    # Titre principal
    pdf.setFont('Helvetica-Bold', 18)
    pdf.drawCentredString(300, 750, "Récépissé de Demande de document")

    
   # Petit paragraphe en bas du titre
    pdf.setFont('Helvetica', 12)
    text = "Vous êtes invité(e) à vous présenter à notre Bureau avec ce document, à la date suivante : {}".format(date_delivrance)
    pdf.drawString(50, 700, text)
    
   # Informations sur l'utilisateur
    pdf.drawString(50, 650, f"Nom : {nom}")
    pdf.drawString(50, 630, f"Prénom : {prenom}")
    pdf.drawString(50, 610, f"Email : {email}")
    pdf.drawString(50, 590, f"Type de document demandé : {type_documents}")
    pdf.drawString(50, 570, f"Date de rendez-vous : {date_delivrance}")

    qr_code_path = "./QRCode/qr_code.png"
    new_width = int(qr_code.size[0] * 0.7)
    new_height = int(qr_code.size[1] * 0.7)
    qr_x = 50
    qr_y = 100
    pdf.drawImage(qr_code_path, qr_x, qr_y, width=new_width, height=new_height)
    pdf.save()

    # Convertir le PDF en bytes
    pdf_bytes = pdf_buffer.getvalue()
    
    # Envoyer l'e-mail avec le PDF en pièce jointe
    email = EmailMessage(
        subject="Confirmation de votre demande de document",
        body='Votre demande a été envoyée avec succés, vous devez donc payer le montant exigés afin de récupérer votre document le {}.'.format(date_delivrance),
        from_email=None,
        to=[email],
    )
    email.attach("document.pdf", pdf_bytes, "application/pdf")
    email.send()
