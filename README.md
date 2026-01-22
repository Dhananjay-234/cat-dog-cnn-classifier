# 🐱🐶 Cat vs Dog Image Classification using CNN

This project implements a **Convolutional Neural Network (CNN)** to classify images as **Cat** or **Dog**.
The model was trained on the **Cats vs Dogs dataset** and deployed using a **Python-based GUI** that allows users to upload an image and view the prediction along with confidence.

---

## 📌 Project Features

* CNN-based binary image classification (**Cat / Dog**)
* Dataset splitting into training and validation sets
* Removal of corrupted images from dataset
* GUI for image upload and prediction
* Prediction confidence display

---

## 🧠 Model Overview

* **Model Type:** Convolutional Neural Network (CNN)
* **Classification:** Binary (Cat vs Dog)
* **Input Size:** 150 × 150 RGB images
* **Output:** Probability score for Cat or Dog
* **Training Type:** Supervised learning

---

## 📂 Project Structure

* `gui.py` – GUI for image upload and prediction
* `split_dataset.py` – Script to split dataset into training and validation sets
* `clean_images.py` – Script to remove corrupted images
* `requirements.txt` – Required Python libraries
* `README.md` – Project documentation

⚠️ Dataset and trained model file are **not included** in this repository due to GitHub size limitations.

---

## 🔗 External Resources

### 📦 Trained CNN Model

The trained CNN model file is hosted externally due to size constraints.

**Download Trained Model (.h5):** <https://www.dropbox.com/scl/fi/kidyc69tv8wysvsvj7beb/cat_dog_cnn.h5?rlkey=asib51z7koj3zjgzwk7mpb6ce&st=zamosgen&dl=0>

After downloading, place the file in the project root directory and name it:
**cat_dog_cnn.h5**

---

### 🗂️ Dataset Used

This project uses the **Cats vs Dogs Dataset**.

**Dataset Download Link:**
[https://www.kaggle.com/competitions/dogs-vs-cats/data](https://www.kaggle.com/competitions/dogs-vs-cats/data)

Dataset structure after extraction:

* PetImages

  * Cat
  * Dog

---

## ⚙️ Setup & Installation

* Install required dependencies
  `pip install tensorflow pillow numpy`

* Split the dataset
  `python split_dataset.py`

* Clean corrupted images
  `python clean_images.py`

* Run the GUI application
  `python gui.py`

---

## 🖥️ GUI Functionality

* Upload an image (`.jpg`, `.png`, `.jpeg`)
* The system predicts **CAT** or **DOG**
* Confidence percentage is displayed with the prediction

---

## ⚠️ Known Limitations

* The model is trained only on cats and dogs
* Non-cat/dog images may still be classified with high confidence
* Binary classifiers always predict one of the trained classes

---

## 🚀 Future Improvements

* Add an **Unknown / Neither** class
* Improve generalization using more diverse data
* Deploy the model as a web application
* Add real-time webcam-based prediction

---

## 🧑‍🎓 Academic / Internship Note

This project was developed as part of **machine learning practice** to understand CNN training workflow, dataset preprocessing, model evaluation, and GUI-based deployment of machine learning models.



