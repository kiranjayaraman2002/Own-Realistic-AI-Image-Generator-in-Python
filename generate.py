from datetime import datetime
import time
import os
import uuid
from PIL import Image
import requests


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

                # Crop watermark/artifacts (adjust as needed)
                image = Image.open(image_save_path)
                image = image.crop((0, 0, image.width, image.height - 48))
                cropped_image = image.crop((0, 0, image.width, image.height - 100))
                cropped_image.save(image_save_path)

                return image_save_path
            else:
                print(f"Retrying... Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}. Retrying...")
        time.sleep(5)  # Avoid rate-limiting


if __name__ == "__main__":
    prompts = [
        " men with baby elephant "
        # Add your own prompts here!
    ]

    save_path = "generated_images"
    os.makedirs(save_path, exist_ok=True)

    for prompt in prompts:
        image_path = generate_images_pollynation_ai(prompt, save_path)
        print(f"Generated: {image_path}")


# https://medium.com/@tomasstakeviius/creating-your-own-realistic-ai-image-generator-in-python-for-free-no-api-keys-required-f2f8d2b00d35
# Creating Your Own Realistic AI Image Generator in Python — For Free (No API Keys Required)

