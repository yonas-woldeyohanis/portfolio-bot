# ai_service.py
import os
import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure AI
model = None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # Smart Model Selection (Flash is fast/free, Pro is stable)
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if 'models/gemini-1.5-flash' in available:
            model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            model = genai.GenerativeModel('gemini-pro')
        print(f"✅ AI Connected: {model.model_name}")
    except:
        model = genai.GenerativeModel('gemini-pro')
else:
    print("⚠️ No GEMINI_API_KEY found.")

# --- HERE IS YOUR DIGITAL TWIN CONTEXT ---
SYSTEM_PROMPT = """
You are the AI Assistant for **Yonas Woldeyohanis**, a professional Python Developer & Bot Specialist.
Your goal is to represent Yonas, explain his services, and generate creative ideas for clients.

**About Yonas:**
- **Role:** Full-stack Python Developer, Telegram Bot Expert.
- **Specialties:** 
  1. Telegram Bots (Aiogram, Python-Telegram-Bot).
  2. AI Integration (OpenAI, Gemini, LLMs).
  3. Web Development (Flask, Django).
  4. Deployment (Render, PythonAnywhere, VPS).
- **Contact:** @jonas_wjohn | +251996246990.

**Your Rules:**
1. **Be Helpful:** If the user asks about Yonas, sell his services professionally.
2. **Be Creative:** If the user asks for "Ideas", generate 3-5 unique, profitable bot ideas for their industry.
3. **Language:** Detect the user's language. If they ask in Amharic, answer in Amharic. If English, answer in English.
4. **Formatting:** Use Telegram Markdown (bold, lists) to make answers look good.
"""

async def ask_gemini(user_text):
    if not model:
        return "⚠️ AI Service is currently offline. Please contact Yonas directly."
    
    try:
        # We combine context + user question
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_text}"
        response = await model.generate_content_async(full_prompt)
        return response.text
    except Exception as e:
        return "Sorry, I am thinking too hard right now! Try again in a moment."