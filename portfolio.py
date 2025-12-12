# portfolio.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils import get_text, user_language

# A placeholder image in case one is missing from constants.py
FALLBACK_IMAGE_URL = "https://i.imgur.com/gYf2K3f.png" 

async def show_portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    lang = user_language.get(user_id, 'en')
    
    projects = get_text('portfolio_projects', user_id)
    keyboard = []
    
    for project_key, project_data in projects.items():
        button_title = project_data.get('title', project_key)
        # --- FIX: We now use a colon ':' as the separator ---
        button = InlineKeyboardButton(button_title, callback_data=f"project:{project_key}:{lang}")
        keyboard.append([button])
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(get_text('portfolio_response', user_id), reply_markup=reply_markup)

async def portfolio_detail_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # --- FIX: We now split by the colon ':' ---
    _, project_key, lang = query.data.split(':')
    
    project = get_text(f'portfolio_projects.{project_key}', query.from_user.id)
    
    title = project.get('title', "Project Details")
    description = project.get('description', "No description available.")
    image_url = project.get('image_url', FALLBACK_IMAGE_URL)
    demo_link = project.get('demo_link')

    caption = f"*{title}*\n\n{description}"
    
    keyboard = [
        # --- FIX: Use a colon ':' here too ---
        [InlineKeyboardButton("Key Features ✨", callback_data=f"features:{project_key}:{lang}")],
    ]
    
    if demo_link:
        keyboard.append([InlineKeyboardButton("Try a Demo 🚀", url=demo_link)])
        
    # --- FIX: Use a colon ':' for consistency ---
    keyboard.append([InlineKeyboardButton("« Back to Projects", callback_data=f"back_to_portfolio:{lang}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=query.effective_chat.id,
        photo=image_url,
        caption=caption,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )
    
    await query.message.delete()

async def portfolio_features_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    # --- FIX: Split by the colon ':' ---
    _, project_key, lang = query.data.split(':')
    
    project = get_text(f'portfolio_projects.{project_key}', query.from_user.id)
    
    title = project.get('title', "Project Features")
    features = project.get('features', "No feature list available.")

    text = f"*{title}* - Key Features:\n\n{features}"
    # --- FIX: Use a colon ':' here too ---
    keyboard = [[InlineKeyboardButton("« Back to Project Details", callback_data=f"project:{project_key}:{lang}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_caption(caption=text, parse_mode='Markdown', reply_markup=reply_markup)

async def back_to_portfolio_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    lang = user_language.get(user_id, 'en')
    
    projects = get_text('portfolio_projects', user_id)
    keyboard = []
    
    for project_key, project_data in projects.items():
        button_title = project_data.get('title', project_key)
        # --- FIX: Use a colon ':' here as well ---
        button = InlineKeyboardButton(button_title, callback_data=f"project:{project_key}:{lang}")
        keyboard.append([button])
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.delete()
    await query.message.chat.send_message(get_text('portfolio_response', user_id), reply_markup=reply_markup)