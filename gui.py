import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("cat_dog_cnn.h5")
IMG_SIZE = 150

def upload_and_predict():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
        )
        if not file_path:
            return

        img = Image.open(file_path).resize((IMG_SIZE, IMG_SIZE))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0][0]

        p_dog = float(prediction)
        p_cat = 1.0 - p_dog

        if p_cat > p_dog:
            label = "CAT"
            confidence = p_cat * 100
        else:
            label = "DOG"
            confidence = p_dog * 100

        result_label.config(
            text=f"Prediction: {label}\nConfidence: {confidence:.2f}%",
            fg="green"
        )

        display_img = ImageTk.PhotoImage(img)
        image_label.config(image=display_img)
        image_label.image = display_img

    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Cat vs Dog Recognition")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="Cat vs Dog Classifier", font=("Arial", 18, "bold")).pack(pady=10)
image_label = tk.Label(root)
image_label.pack(pady=10)

tk.Button(
    root,
    text="Upload Image",
    command=upload_and_predict,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white"
).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
