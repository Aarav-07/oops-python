import qrcode

# Get data from user
data = input("Enter text/URL for QR code: ")
file_name = input("Enter name for QR code image (without extension): ")

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create image from QR code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the image
qr_image.save(f"{file_name}.png")
print(f"QR code has been saved as {file_name}.png")