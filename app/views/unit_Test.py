from django.test import TestCase, Client
from django.core.mail import EmailMessage
from unittest.mock import patch
from io import BytesIO
from app.models import Rendez_vous
from app.views import generate_qr_code, send_confirmation_email

class SendConfirmationEmailTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = 'test@example.com'
        self.rendez_vous = Rendez_vous.objects.create(nom='Doe', prenom='John', email=self.email, type_documents='passeport', date_delivrance='2022-01-01')
    
    @patch('app.views.generate_qr_code')
    @patch('app.views.EmailMessage')
    def test_send_confirmation_email(self, mock_email_message, mock_generate_qr_code):
        # Configurez le mock pour renvoyer une image QR code factice
        qr_code_bytes = b'fake qrcode bytes'
        mock_generate_qr_code.return_value = BytesIO(qr_code_bytes)

        # Appelez la vue pour envoyer l'e-mail de confirmation
        response = send_confirmation_email(self.client, self.email)

        # Vérifiez que la réponse HTTP contient le PDF en pièce jointe
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="document.pdf"')
        self.assertEqual(response.content, mock_email_message.return_value.attach.call_args[0][1])

        # Vérifiez que le message e-mail a été correctement configuré
        mock_email_message.assert_called_once_with(
            subject='Confirmation de votre demande de document',
            body='Votre demande a été envoyée avec succés, vous devez donc payer le montant exigés afin de récupérer votre document le 2022-01-01.',
            from_email=None,
            to=[self.email],
        )
        mock_email_message.return_value.attach.assert_called_once_with('document.pdf', response.content, 'application/pdf')

        # Vérifiez que le code QR a été correctement généré
        mock_generate_qr_code.assert_called_once_with('Doe', 'John', self.email, 'passeport', '2022-01-01')
        self.assertEqual(mock_generate_qr_code.return_value.getvalue(), qr_code_bytes)