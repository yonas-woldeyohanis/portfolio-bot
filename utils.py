# utils.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from constants import TEXTS
import functools # Import functools for the new get_text

# This dictionary will hold the user's chosen language.
user_language = {}

# --- THIS IS THE CORRECTED FUNCTION ---
def get_text(key, user_id):
    """
    Returns the text in the user's chosen language.
    Supports nested keys using dot notation (e.g., 'quote_flow.start_message').
    """
    lang = user_language.get(user_id, 'en') # Default to 'en' if not set
    try:
        # Split the key by '.' and traverse the dictionary
        return functools.reduce(lambda d, k: d[k], key.split('.'), TEXTS[lang])
    except (KeyError, TypeError):
        # If the key is not found, return the key itself as an indicator
        print(f"Warning: Text key '{key}' not found for language '{lang}'.")
        return key

async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, user_id):
    """Sends the main menu keyboard."""
    lang = user_language.get(user_id, 'en')
    
    # Define the keyboard layout
    keyboard = [
        [TEXTS[lang]['portfolio_btn'], TEXTS[lang]['services_btn']],
        [TEXTS[lang]['about_btn'], TEXTS[lang]['contact_btn']],
        [TEXTS[lang]['inspire_btn']], # <-- ADD THIS NEW ROW
        [TEXTS[lang]['quote_btn']]   # <-- Move quote button to its own row
    ]
    
    # Create the ReplyKeyboardMarkup
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    
    await update.effective_chat.send_message(
        text=get_text('main_menu_prompt', user_id),
        reply_markup=reply_markup
    )