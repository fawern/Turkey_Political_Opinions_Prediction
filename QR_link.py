import pyqrcode

url = "https://docs.google.com/forms/d/e/1FAIpQLSfzatWes3vOafZreTRKMuGLVu4SW93-vWBZhTF7I2I9If4yyQ/viewform?usp=sf_link"

qr_code = pyqrcode.create(url)

qr_code.svg('form_link.svg', scale=5)