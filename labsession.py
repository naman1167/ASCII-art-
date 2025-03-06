import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext, messagebox
from pyfiglet import figlet_format
from termcolor import colored
from PIL import Image, ImageDraw, ImageFont

def generate_ascii():
    msg = msg_entry.get()
    color = color_var.get()
    font_name = font_var.get()
    theme = theme_var.get()
    save_format = save_var.get()

    try:
        ascii_art = figlet_format(msg, font=font_name)
        colored_ascii = colored(ascii_art, color=color)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, colored_ascii)

        if save_format in ["txt", "both"]:
            save_as_txt(ascii_art)
        if save_format in ["png", "both"]:
            save_as_png(ascii_art, theme=theme)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_as_txt(ascii_art, filename="ascii_output.txt"):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            f.write(ascii_art)
        messagebox.showinfo("Saved", f"ASCII art saved as {file_path}")

def save_as_png(ascii_art, filename="ascii_output.png", theme="dark"):
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        lines = ascii_art.split("\n")
        font = ImageFont.load_default()
        line_height = 15
        img_width = max([len(line) for line in lines]) * 10
        img_height = len(lines) * line_height + 20

        bg_color, text_color = ("black", "green") if theme == "dark" else ("white", "gray")
        img = Image.new("RGB", (img_width, img_height), bg_color)
        draw = ImageDraw.Draw(img)

        y_offset = 10
        for line in lines:
            draw.text((10, y_offset), line, fill=text_color, font=font)
            y_offset += line_height

        img.save(file_path)
        messagebox.showinfo("Saved", f"ASCII art saved as {file_path}")

# GUI Setup
root = tk.Tk()
root.title("ASCII Art Generator")

# Set full screen
root.attributes('-fullscreen', True)

#Style
style = ttk.Style()
style.configure('TLabel', padding=(10, 5), font=('Arial', 12))
style.configure('TCombobox', padding=(10, 5), font=('Arial', 12))
style.configure('TButton', padding=(10, 5), font=('Arial', 12))

msg_label = ttk.Label(root, text="Message:")
msg_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
msg_entry = ttk.Entry(root, width=40, font=('Arial', 12))
msg_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

color_label = ttk.Label(root, text="Color:")
color_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
color_var = ttk.Combobox(root, values=["red", "green", "yellow", "blue", "magenta", "cyan", "white"], style='TCombobox')
color_var.grid(row=1, column=1, padx=10, pady=10)
#Removed the "random" option.
color_var.set("green")

font_label = ttk.Label(root, text="Font:")
font_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
font_list = ['slant', 'banner', 'block', 'bubble', 'digital', 'ivrit', 'mini', 'script', 'shadow', 'smscript', 'smshadow', 'smslant']
font_var = ttk.Combobox(root, values=font_list, style='TCombobox')
font_var.grid(row=2, column=1, padx=10, pady=10)
font_var.set("banner")

theme_label = ttk.Label(root, text="Theme:")
theme_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
theme_var = ttk.Combobox(root, values=["dark", "light"], style='TCombobox')
theme_var.grid(row=3, column=1, padx=10, pady=10)
theme_var.set("dark")

save_label = ttk.Label(root, text="Save As:")
save_label.grid(row=4, column=0, sticky="w", padx=10, pady=10)
save_var = ttk.Combobox(root, values=["txt", "png", "both", "none"], style='TCombobox')
save_var.grid(row=4, column=1, padx=10, pady=10)
save_var.set("both")

generate_button = ttk.Button(root, text="Generate ASCII", command=generate_ascii, style='TButton')
generate_button.grid(row=5, column=0, columnspan=4, padx=10, pady=20)

output_text = scrolledtext.ScrolledText(root, width=60, height=15, font=('Courier', 12))
output_text.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()