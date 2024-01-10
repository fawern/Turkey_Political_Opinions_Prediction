import pyqrcode

url = "https://docs.google.com/forms/d/e/1FAIpQLScEV8Q6D1_QA_QuBblvNX6LMa8tSxxdVIECr5atU2H6c51cdw/viewform?usp=sf_link"

qr_code = pyqrcode.create(url)

qr_code.svg('form_link.svg', scale=5)