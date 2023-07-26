import qrcode
from django.http import HttpResponse


def generate_qr_code(request):
    #Récuperer les informations de l'utilisateur a partir 
    user_info = "Informations sur l'utilisateur"
    
    #Generer le code QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CONNECT_l,
        box_size=10,
        border=4,
    )
    qr.add_data(user_info)
    qr.make(fit=True)
    
    #creer une image du QR code
    qr_image = qr.make_image(fill_color="red", black_color="bleu")
    
    #Enregistrer l'image dans un fichier (facultatif)
    qr_image_path = "qr_code_png"
    qr_image.save(qr_image_path)
    
    #Response l'image du QR code dans la reponse HTPP
    response = HttpResponse(content_type="image/png")
    qr_image.save(response, "PNG")
    
    return response
    
    