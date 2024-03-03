import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import qrcode

# Function to generate QR Code
def generate_qr():
    input_data = text_input.get()
    if input_data.strip() == "":
        messagebox.showerror("Error", "Input cannot be empty")
        return
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("temp_qr.png")

        # Display QR Code
        img = Image.open("temp_qr.png")
        img = img.resize((250, 250), Image.Resampling.LANCZOS)
        qr_img = ImageTk.PhotoImage(img)
        qr_label.config(image=qr_img)
        qr_label.image = qr_img  # Keep a reference!
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {e}")

# Function to save QR Code
def save_qr():
    input_data = text_input.get()
    if input_data.strip() == "":
        messagebox.showerror("Error", "Input cannot be empty")
        return
    try:
        file_path = f"{input_data[:10].replace(' ', '_')}.png"
        qr = qrcode.make(input_data)
        qr.save(file_path)
        messagebox.showinfo("QR Generator", f"QR Code saved as {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save QR Code: {e}")

# Main application window
app = tk.Tk()
app.title('QR Code Generator')
app.geometry('400x500')  # Width x Height

# Label
label = ttk.Label(app, text="Enter URL or Text:")
label.pack(pady=10)

# Text input
text_input = ttk.Entry(app, width=40)
text_input.pack(pady=10)

# Generate Button
generate_button = ttk.Button(app, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Save Button
save_button = ttk.Button(app, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

# QR Code Display Label
qr_label = ttk.Label(app)
qr_label.pack(pady=10)

# Run the app
app.mainloop()