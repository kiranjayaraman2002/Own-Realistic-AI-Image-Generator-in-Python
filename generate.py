import streamlit as st
from datetime import datetime
import time
import os
import uuid
from PIL import Image
import requests

# Function to generate image
def generate_images_pollynation_ai(prompt, save_path):
    prompt += str(uuid.uuid4())  # Ensure unique prompts to bypass caching
    formatted_prompt = prompt.replace(" ", "-")
    url = f"https://image.pollinations.ai/prompt/{formatted_prompt}"

    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                image_save_name = f"img_{timestamp}.png"
                image_save_path = os.path.join(save_path, image_save_name)
                os.makedirs(os.path.dirname(image_save_path), exist_ok=True)

                with open(image_save_path, 'wb') as f:
                    f.write(response.content)

                # Crop watermark/artifacts
                image = Image.open(image_save_path)
                image = image.crop((0, 0, image.width, image.height - 48))
                cropped_image = image.crop((0, 0, image.width, image.height - 100))
                cropped_image.save(image_save_path)

                return image_save_path
            else:
                st.warning(f"Retrying... Status code: {response.status_code}")
        except requests.RequestException as e:
            st.error(f"Request failed: {e}. Retrying...")
        time.sleep(5)

# Streamlit UI
st.set_page_config(page_title="AI Image Generator", page_icon="🎨", layout="centered")

st.title("🎨 AI Image Generator (Pollinations)")
st.write("Enter a prompt below and generate AI images for free (no API key required).")

prompt = st.text_input("📝 Enter your prompt", "A man with baby elephant")
save_path = "generated_images"

if st.button("Generate Image"):
    with st.spinner("⏳ Generating your image... Please wait."):
        image_path = generate_images_pollynation_ai(prompt, save_path)
        if image_path:
            st.success("✅ Image Generated Successfully!")
            st.image(image_path, caption="Generated Image", use_column_width=True)
            with open(image_path, "rb") as file:
                st.download_button("📥 Download Image", file, file_name=os.path.basename(image_path))




