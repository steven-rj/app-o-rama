import main_menu

import qrcode
import os.path


def generate_code(text, path):

    qr = qrcode.QRCode(version = 1,
                        error_correction = qrcode.constants.ERROR_CORRECT_L,
                        box_size = 10,
                        border = 4)

    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color = "black", back_color = "white")
    file = path + "\qrcode.png"
    image.save(file)
    if os.path.exists(file):
        print("QR image created successfully!")
    else:
        print("Error creating QR image!")
    


def get_download_path():

    file_path = input("Enter path to save the QR code: ")
    return file_path


def main():
    
    text = input("Enter text to have generated into a QR code: ")
    path = get_download_path()
    generate_code(text, path)
    main_menu.display_main_menu()

if __name__ == "__main__":
    main()