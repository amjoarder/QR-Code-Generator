import qrcode
from PIL import Image
import qrcode.constants
#we can change the look of the QR Code.
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4
    )

qr.add_data("https://just.edu.bd/notices")

qr.make(fit=True)

img = qr.make_image(fill_color = "red", back_color = "yellow")

img.save("JUST_Notice.png")