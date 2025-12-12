# idea_generator.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils import get_text, user_language

async def start_idea_generator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays the main industry selection menu for the idea generator."""
    user_id = update.message.from_user.id
    lang = user_language.get(user_id, 'en')
    
    generator_data = get_text('idea_generator', user_id)
    industries = generator_data['industries']
    
    keyboard = []
    for industry_key, industry_data in industries.items():
        button = InlineKeyboardButton(
            industry_data['button_text'],
            callback_data=f"idea_industry_{industry_key}_{lang}"
        )
        keyboard.append([button])
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(generator_data['title'], reply_markup=reply_markup)


async def industry_choice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the user's choice of industry and displays creative ideas."""
    query = update.callback_query
    await query.answer()
    
    # Data is 'idea_industry_INDUSTRYKEY_LANGUAGE'
    _, _, industry_key, lang = query.data.split('_')
    
    industry_data = get_text(f'idea_generator.industries.{industry_key}', query.from_user.id)
    
    # Format the ideas into a clean message
    message = f"*{industry_data['ideas_title']}*\n\n"
    for idea in industry_data['ideas']:
        message += f"✅ {idea}\n\n"
        
    back_button_text = get_text('idea_generator.back_button', query.from_user.id)
    
    keyboard = [[InlineKeyboardButton(back_button_text, callback_data=f"back_to_ideas_{lang}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text=message, parse_mode='Markdown', reply_markup=reply_markup)


async def back_to_industries_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the 'Back to Industries' button click."""
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    lang = user_language.get(user_id, 'en')
    
    generator_data = get_text('idea_generator', user_id)
    industries = generator_data['industries']
    
    keyboard = []
    for industry_key, industry_data in industries.items():
        button = InlineKeyboardButton(
            industry_data['button_text'],
            callback_data=f"idea_industry_{industry_key}_{lang}"
        )
        keyboard.append([button])
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=generator_data['title'], reply_markup=reply_markup)