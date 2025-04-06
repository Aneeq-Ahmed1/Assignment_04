import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4,  
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{filename}.png")
    print(f"QR Code generated and saved as {filename}.png")

if __name__ == "__main__":
    data = input("Enter the data to encode (e.g., URL or text): ")
    filename = input("Enter the filename to save the QR code: ")
    generate_qr_code(data, filename)
