import tkinter as tk
from tkinter import Label, Button, Entry
from PIL import Image, ImageTk
import random
from diffusers import StableDiffusionPipeline
from tkinter import ttk
import time

pipe = StableDiffusionPipeline.from_pretrained("hf-internal-testing/tiny-stable-diffusion-torch")

def generate_image():
    prompt = description_entry.get()
    generate_button.config(state=tk.DISABLED)  
    status_label.config(text="Génération de l'image...", fg="blue")
    spinner.start() 
    
    root.after(100, generate_image_in_thread, prompt)

def generate_image_in_thread(prompt):
    try:
        image = pipe(prompt).images[0]

        img = ImageTk.PhotoImage(image)
        
        result_label.config(image=img)
        result_label.image = img
        
        status_label.config(text="Image générée", fg="green")
    except Exception as e:
        status_label.config(text=f"Erreur : {str(e)}", fg="red")
    finally:
        spinner.stop()
        generate_button.config(state=tk.NORMAL)
        description_entry.focus_set()

root = tk.Tk()
root.title("Interface Tkinter")

title_label = Label(root, text="Tkinter Application UI", font=("Arial", 16))
title_label.pack(pady=10)

description_label = Label(root, text="Description :")
description_label.pack(pady=5)
description_entry = Entry(root, width=50)
description_entry.insert(0, "Entrez la description ici")
description_entry.pack(pady=5)

generate_button = Button(root, text="Generate image", command=generate_image)
generate_button.pack(pady=10)

spinner = ttk.Progressbar(root, mode="indeterminate")

status_label = Label(root, text="", fg="black")
status_label.pack()

result_label = Label(root, text="Zone d'affichage de l'image", width=300, height=300, bg="gray")
result_label.pack(pady=10)

root.mainloop()
