from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, asyncio,whisper,imageio_ffmpeg,sys
from deep_translator import GoogleTranslator
import edge_tts
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
from PIL import Image

# --- Get User Inputs ---
print(" ****  Enter Your Topic  **** ")
topic = input("|---> ")

print(" ****  Enter Your Language (english/urdu)  **** ")
language = input("|---> ").lower()

# For Urdu, choose male/female voice
voice_choice = "ur-PK-UzmaNeural"  # default female
if language == "urdu":
    print("Choose Urdu voice: 1 = Female, 2 = Male")
    choice = input("|---> ")
    if choice == "2":
        voice_choice = "ur-PK-AsadNeural"

Url = "https://gemini.google.com/app"

# --- Selenium Setup ---
provider = Service(executable_path="Simple Python\\Projects\\Youtube Shorts\\chromedriver.exe")
driver = webdriver.Chrome(service=provider)
driver.get(Url)

# Wait for input box
prompt = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']"))
)

# Send topic to Gemini
prompt.send_keys(f"3 facts about {topic}, The facts should be short. before and after telling the facts start with intro and outro and straight-forward so that it fits in 40 sec video. "
                 "Every fact should start with Fact 1, 2, etc., and end like a short video conclusion.")
prompt.send_keys(Keys.ENTER)

# Wait for response dynamically
time.sleep(10)  # optional, can be replaced with dynamic wait
script_output = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.markdown"))
)

# Get Gemini text
script = script_output.text
print("\n **** Gemini Response **** \n")
print(script) 

driver.quit()  # Close Selenium early

# --- Text-to-Speech Function ---
def text_to_speech(text, filename="Script.mp3"):
    if language == "english":
        # gTTS for English
        from gtts import gTTS
        audio = gTTS(text=text, lang="en")
        audio.save(filename)
    elif language == "urdu":
        # Translate to Urdu first
        urdu_text = GoogleTranslator(source='auto', target='ur').translate(text)
        
        # Async function for Edge-TTS
        async def speak():
            communicate = edge_tts.Communicate(urdu_text, voice_choice)
            await communicate.save(filename)
        
        asyncio.run(speak())

    # Play audio
    os.system(f"start {filename}")  # Windows only

# --- Generate Audio ---
text_to_speech(script)
from selenium.webdriver.chrome.options import Options

# --- Selenium Setup with custom download folder ---
download_dir = r"C:\Users\mansoor\Desktop\Python\Simple Python\Projects\Youtube Shorts\images"
os.makedirs(download_dir, exist_ok=True)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,  # <- set your folder
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})

provider = Service(executable_path="Simple Python\\Projects\\Youtube Shorts\\chromedriver.exe")
driver = webdriver.Chrome(service=provider, options=chrome_options)

# Open DeepAI
driver.get("https://deepai.org/machine-learning-model/text2img?utm_source=chatgpt.com")

# --------------------------------------------------------------------------------------------------
# ---------- CONFIG ----------

# Prompts to generate
prompts = [
    f"Create a cinematic picture of {topic}",
    f"Create a cinematic picture of {topic} from the higher angle",
    f"Create a cinematic picture of {topic} at night ",
    f"Create a picture Inside {topic}",
    f"Create a picture with people around {topic}"
]

# Folder to save images
download_dir = r"Simple Python\Projects\Youtube Shorts\images"
os.makedirs(download_dir, exist_ok=True)

#input("⚠️ Please log in to DeepAI in the opened browser, then press Enter here to continue...")
time.sleep(3)  # wait for manual login

# Image downloader 
for idx, prompt_text in enumerate(prompts, start=1):
    # Wait for textarea
    input_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )

    # Enter prompt
    input_box.clear()
    input_box.send_keys(prompt_text)
    input_box.send_keys(Keys.ENTER)

    # Wait extra time after entering prompt (to let you scroll if needed)
    time.sleep(8)

    # Wait for the download button to appear
    download_button = WebDriverWait(driver, 180).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Download')]"))
    )

    # Click download
    download_button.click()
    print(f"✅ Prompt {idx} submitted and image download clicked.")

    # Wait extra time after download before next prompt
    time.sleep(6)

driver.quit()

import os

# Your images folder path
folder = r"Simple Python\Projects\Youtube Shorts\images"

# Allowed image extensions
image_exts = (".jpg", ".jpeg", ".png", ".webp", ".gif",".jfif")

# Find image files
images = [f for f in os.listdir(folder) if f.lower().endswith(image_exts)]

# Check and print result
if images:
    print(f"✅ Found {len(images)} image(s):")
    for img in images:
        print(f"All images should now be in: {download_dir}") 
        print(" -", img)

else:
    print("❌ No images found in the folder.")
    sys.exit() 

from PIL import Image

#-------------------------------------------------------------------------------------------------
#------ Image converter to JPG
from PIL import Image
import os
from moviepy.editor import *
import whisper
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings
import imageio_ffmpeg

#-------------------------------------------------------------------------------------------------
#------ Image converter to JPG (supports .jfif, .jpg, .png, .webp, .gif)

folder = r"Simple Python\Projects\Youtube Shorts\images"
os.makedirs(folder, exist_ok=True)

converted = []
counter = 1

for filename in os.listdir(folder):
    if filename.lower().endswith((".jfif", ".jpg", ".jpeg", ".png", ".webp", ".gif")):
        input_path = os.path.join(folder, filename)
        output_path = os.path.join(folder, f"pic{counter}.jpg")
        try:
            with Image.open(input_path) as img:
                img.convert("RGB").save(output_path, "JPEG")
                converted.append(output_path)
                counter += 1
            # ✅ Delete original file after successful conversion
            if input_path != output_path:
                os.remove(input_path)

        except Exception as e:
            print(f"Skipping {filename}: {e}")

print("✅ Converted files:", converted)

if not converted:
    print("❌ No images found or converted — stopping program.")
    sys.exit()

#-----------------------------------------------
# Video Editor
audio = AudioFileClip("Script.mp3")
duration = audio.duration  # duration in seconds (float)
time_pic = duration / 5

pictures = converted  # use actual converted images
time_pic = duration / len(pictures)  # automatically divide audio by number of images
clips = [ImageClip(img).set_duration(time_pic) for img in pictures]

final = concatenate_videoclips(clips)
final = final.set_audio(audio)
final.write_videofile("clips_with_audio.mp4", fps=24)

#-----------------------------------------------
# Final Video with Subtitles
change_settings({
    "IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.2-Q16-HDRI\magick.exe"
})

video = VideoFileClip("clips_with_audio.mp4")
audio = AudioFileClip("Script.mp3")
video = video.set_audio(audio)

model = whisper.load_model("tiny")
result = model.transcribe("Script.mp3")

subtitles_list = []
for seg in result["segments"]:
    start = seg["start"]
    end = seg["end"]
    text = seg["text"].strip()
    subtitles_list.append(((start, end), text))

def generator(txt):
    return TextClip(
        txt,
        fontsize=30,
        color='white',
        font='Arial',
        bg_color='black',
        size=(video.w * 0.9, None),
        method='caption',
        align='center'
    )

subtitles = SubtitlesClip(subtitles_list, generator).set_position(("center", "bottom"))
final_video = CompositeVideoClip([video, subtitles])
final_video.write_videofile(f"C:\\Users\\mansoor\\Desktop\\Shorts\\{topic}.mp4", fps=24)

import os

folder = r"Simple Python\Projects\Youtube Shorts\images"

# Your main program logic here...

# After the program ends, delete all images in the folder
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    # Only delete files (not subfolders)
    if os.path.isfile(file_path):
        os.remove(file_path)

print("All images deleted successfully!")
