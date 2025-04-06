# decoder.py
from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    for obj in decoded_objects:
        print(f"Data: {obj.data.decode('utf-8')}")
        print(f"Type: {obj.type}")

if __name__ == "__main__":
    image_path = input("Enter the path to the QR code image: ")
    decode_qr_code(image_path)
