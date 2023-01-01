import main_menu

import qrcode


def generate_code(text):

    qr = qrcode.QRCode(version = 1,
                        error_correction = qrcode.constants.ERROR_CORRECT_L,
                        box_size = 10,
                        border = 4)

    qr.add_data(text)
    qr.make(fit=True)
    image = qr.make_image(fill_color = "black", back_color = "white")
    image.save("qrcode.png")

def main():
    
    text = input("Enter text to have generated into a QR code: ")
    generate_code(text)
    main_menu.display_main_menu()

if __name__ == "__main__":
    main()