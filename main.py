# main.py

import logging
from keep_alive import start_server
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ConversationHandler
)
from idea_generator import start_idea_generator, industry_choice_handler, back_to_industries_handler
# Import our project-specific files
from config import BOT_TOKEN
from constants import TEXTS
from utils import get_text, user_language, send_main_menu
from portfolio import portfolio_detail_handler, portfolio_features_handler, back_to_portfolio_handler
from quote import start_quote, purpose_received, features_received, budget_received, contact_received, cancel
from quote import PURPOSE, FEATURES, BUDGET, CONTACT

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# --- Command and Callback Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with two inline buttons to choose a language."""
    keyboard = [
        [InlineKeyboardButton("English 🇬🇧", callback_data="lang_en")],
        [InlineKeyboardButton("አማርኛ 🇪🇹", callback_data="lang_am")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose your language: / እባክዎ ቋንቋዎን ይምረጡ:", reply_markup=reply_markup)

async def language_choice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery, sets the language, and displays the main menu."""
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    chosen_language = query.data.split('_')[1]
    user_language[user_id] = chosen_language

    await query.edit_message_text(text=get_text('welcome_selected', user_id))
    await send_main_menu(update, context, user_id)


# --- THIS IS THE HANDLER FOR ALL NON-CONVERSATION BUTTONS ---
async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles messages from the main menu buttons that are NOT the start of a conversation."""
    from portfolio import show_portfolio

    user_id = update.message.from_user.id
    received_text = update.message.text
    lang = user_language.get(user_id, 'en')

    # A dictionary mapping button text to functions
    button_map = {
        TEXTS[lang]['portfolio_btn']: show_portfolio,
        TEXTS[lang]['services_btn']: show_services,
        TEXTS[lang]['about_btn']: show_about,
        TEXTS[lang]['contact_btn']: show_contact,
        TEXTS[lang]['inspire_btn']: start_idea_generator,
    }

    # If the received text is a known button, call its function
    if received_text in button_map:
        await button_map[received_text](update, context)
    else:
        # Optional: Handle other text messages when not in a conversation
        await update.message.reply_text("Please use one of the buttons below.")

# Placeholder functions for simple menu options
async def show_services(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    services_data = get_text('services_info', user_id)
    message = services_data['title'] + "\n\n"
    for tier in services_data['tiers']:
        message += f"*{tier['name']}*\n{tier['desc']}\n\n"
    await update.message.reply_text(message, parse_mode='Markdown')

# In main.py, replace the old show_about function with this one.

async def show_about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Formats and sends the structured 'About Me' information."""
    user_id = update.message.from_user.id

    # Get the entire 'about_me_content' dictionary
    about_data = get_text('about_me_content', user_id)

    # Build the response string piece by piece
    message = about_data['title'] + "\n\n"
    message += about_data['body']
    message += "\n" + about_data['points_title'] + "\n"

    # Loop through the points and add them
    for point in about_data['points']:
        message += f"\n*{point['heading']}*\n{point['body']}\n"

    message += about_data['footer']

    await update.message.reply_text(message, parse_mode='Markdown')

async def show_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    contact_data = get_text('contact_info', user_id)
    my_telegram_username = "jonas_wjohn"
    my_phone_number = "+251996246990"
    keyboard = [[InlineKeyboardButton(contact_data['tg_button'], url=f"https://t.me/{my_telegram_username}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    full_text = f"{contact_data['text']}\n\n*Phone:* `{my_phone_number}`"
    await update.message.reply_text(text=full_text, reply_markup=reply_markup, parse_mode='Markdown')


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    # --- THE CORRECTED CONVERSATION HANDLER ---
    # We extract the core text without emojis for a robust Regex match
    quote_en = TEXTS['en']['quote_btn'].split(' ')[0]
    quote_am = TEXTS['am']['quote_btn'].split(' ')[0]

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(
            filters.Regex(f"^({quote_en}|{quote_am})"), # <-- THIS IS THE FIX
            start_quote
        )],
        states={
            PURPOSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, purpose_received)],
            FEATURES: [MessageHandler(filters.TEXT & ~filters.COMMAND, features_received)],
            BUDGET: [CallbackQueryHandler(budget_received, pattern="^budget_")],
            CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, contact_received)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # --- Add handlers in the correct order of priority ---
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(language_choice_handler, pattern="^lang_"))
    application.add_handler(conv_handler)

    # Portfolio, Idea Generator, etc. callback handlers
    application.add_handler(CallbackQueryHandler(portfolio_detail_handler, pattern="^project_"))
    application.add_handler(CallbackQueryHandler(portfolio_features_handler, pattern="^features_"))
    application.add_handler(CallbackQueryHandler(back_to_portfolio_handler, pattern="^back_to_portfolio_"))
    application.add_handler(CallbackQueryHandler(industry_choice_handler, pattern="^idea_industry_"))
    application.add_handler(CallbackQueryHandler(back_to_industries_handler, pattern="^back_to_ideas"))

    # The general main menu handler (fallback for non-quote buttons)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_handler))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    start_server()  # <--- ADD THIS LINE HERE
    print("🌍 Web Server started for Render!")
    main()