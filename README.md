# Own Realistic AI Image Generator in Python (No API Keys Required)

Generate high-quality, realistic AI images for free using Python — no paid APIs or subscriptions needed.

This project uses the public image generation endpoint from [pollinations.ai](https://pollinations.ai) and processes the results with Python. It's fast, customizable, and perfect for creative experimentation.

---

## 🚀 Features

🛠️ Tech Stack

Frontend/UI: Streamlit (interactive Python web app framework)

Backend: Python

✅ User can enter any text prompt

✅ Fetches image from Pollinations AI API

✅ Ensures unique images using UUID-based prompt handling

✅ Cleans images (removes watermark/artifacts using Pillow cropping)

✅ Saves generated images locally (generated_images folder)

✅ Preview inside Streamlit app

✅ Download button for users to save the generated image

## Libraries Used:

requests → API calls to Pollinations

uuid → ensure unique prompts to avoid cache issues

datetime, os → saving images with timestamp names

PIL (Pillow) → cropping watermarks/artifacts from images

time → retry logic for failed API requests


## 🔑 Key Functionality (Flow)

Input Prompt → User enters a description in the text box.

API Request → Prompt is formatted and sent to Pollinations API.

Image Handling →

Image is saved with timestamp.

Cropping removes watermark/extra artifacts.

Display → The final image is shown on the page.

Download → User can download the generated image.

## 📂 Project Structure

AI-Image-Generator/
│── app.py                # Main Streamlit application
│── generated_images/     # Folder where generated images are saved
│── requirements.txt      # Dependencies
│── README.md             # Documentation

🚀 How to Run

Clone repo & install dependencies:

pip install streamlit pillow requests


Run Streamlit app:

streamlit run app.py


Open browser at http://localhost:8501/

💡 Example Prompt

👉 “A futuristic city with flying cars at sunset”
The app will generate an AI image matching the description.

🎯 Why This Project is Useful (Interview Points)

Shows knowledge of API integration (Pollinations API).

Demonstrates frontend + backend skills using Streamlit.

Handles file management and image processing.

Includes error handling + retry logic.

Provides downloadable outputs for end users.



