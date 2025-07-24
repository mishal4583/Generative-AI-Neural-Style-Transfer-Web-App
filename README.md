# 🎨 Neural Style Transfer Web App

Welcome to Task 5 of my Generative AI Internship at Prodigy InfoTech!

This project demonstrates **Neural Style Transfer (NST)** using TensorFlow Hub and provides a user-friendly Streamlit web interface to blend the artistic style of one image with the content of another.

---

## 🚀 Features

* **✨ Upload your own images:** Upload any **content image** (e.g., your photo) and a **style image** (e.g., a Van Gogh painting) to generate a new artistic rendition.
* **🖼️ Real-time Neural Style Transfer:** Powered by TensorFlow Hub's `magenta/arbitrary-image-stylization-v1-256` model.
* **⚙️ Adjustable blending:** Tune style vs. content dynamically in the code for experimentation.
* **💾 Download final stylized images:** Save your creations directly from the app.
* **🎯 Simple & modular architecture:** Core style transfer logic is cleanly separated in `API.py` for easy maintenance.

---

## 🛠 Tech Stack

| Layer   | Technology                                     |
| :------ | :--------------------------------------------- |
| Backend | Python, TensorFlow, TensorFlow Hub, NumPy, OpenCV |
| Web App | Streamlit                                      |
| Others  | Matplotlib (for saving/downloads), Pillow (image handling) |

---

## 📂 Folder Structure

.
├── Main.py          # Streamlit app UI & server
├── API.py           # Core style transfer logic using TensorFlow Hub
├── model/           # TensorFlow Hub model directory (loaded at runtime)
├── requirements.txt # Python dependencies
└── README.md


---

## 🚀 Running Locally

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/mishal4583/Generative-AI-Neural-Style-Transfer-Web-App](https://github.com/mishal4583/Generative-AI-Neural-Style-Transfer-Web-App)
    cd neural-style-transfer-app
    ```

2.  **Set Up Python Environment**

    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # OR On macOS/Linux:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit App**

    ```bash
    streamlit run Main.py
    ```

    Then open your browser at `http://localhost:8501`.

---

## 🔍 How It Works

The app takes in a content image and a style image. It processes them using a pre-trained TensorFlow Hub model (`magenta/arbitrary-image-stylization-v1-256`), producing a new image that retains the original structure (content) but reflects the artistic style.

The actual transformation is handled by:

```python
outputs = hub_module(tf.constant(content_image), tf.constant(style_image))

where hub_module is loaded via:
Python

hub_module = hub.load(model_path)

📜 Notes

    This project uses a TensorFlow Hub model saved locally (in ./model).

    You can also directly load it from the hub link if preferred: https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2

👨‍💻 Author

Mishal KS
