# 🎥 Automated YouTube Shorts Generator

This Python project automates the creation of short informative videos.  
It:
1. Uses **Selenium** to fetch short scripts (facts) from Gemini.
2. Converts the script into **text-to-speech audio** (supports English & Urdu).
3. Downloads and processes **AI-generated images**.
4. Converts and merges images into a video with background audio.
5. Adds **subtitles** using Whisper AI.
6. Outputs a ready-to-upload MP4 short video.

---

## ⚡ Requirements

Make sure you have **Python 3.10+** installed.  
You also need **Google Chrome** and the matching **ChromeDriver**.

---

## 📦 Installation

Open **PowerShell/Command Prompt** and run:

```powershell
# Selenium (automation)
    pip install selenium

# Whisper (speech-to-text)
    pip install -U openai-whisper

# MoviePy (video editing)
    pip install moviepy

# Google Translate wrapper  
    pip install deep-translator

# gTTS (text-to-speech for English)
    pip install gTTS

# Edge-TTS (text-to-speech for Urdu)
    pip install edge-tts

# Pillow (image processing)
    pip install pillow

# ImageIO for FFMPEG handling   
    pip install imageio_ffmpeg

# Ensure FFMPEG is installed (needed by moviepy & whisper)
    pip install imageio[ffmpeg]

### Under Construction
 -Still Working on it 