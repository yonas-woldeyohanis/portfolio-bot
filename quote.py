# quote.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from utils import get_text, user_language, send_main_menu
from config import ADMIN_USER_ID
from constants import TEXTS # <--- THIS WAS THE MISSING IMPORT

# Define the states for the conversation
PURPOSE, FEATURES, BUDGET, CONTACT = range(4)

async def start_quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the quote conversation and asks for the project purpose."""
    user_id = update.message.from_user.id
    # Ask the first question
    await update.message.reply_text(
        get_text('quote_flow.start_message', user_id),
        reply_markup=ReplyKeyboardRemove() # Temporarily remove the main menu
    )
    return PURPOSE

async def purpose_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the purpose and asks for features."""
    user_id = update.message.from_user.id
    # Save the user's response in a temporary storage
    context.user_data['purpose'] = update.message.text
    
    await update.message.reply_text(get_text('quote_flow.ask_features', user_id))
    return FEATURES

async def features_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the features and asks for the budget with buttons."""
    user_id = update.message.from_user.id
    context.user_data['features'] = update.message.text
    
    lang = user_language.get(user_id, 'en')
    
    # This part needs the 'TEXTS' dictionary, which is why the import was needed.
    keyboard = [
        [InlineKeyboardButton(TEXTS[lang]['quote_flow']['budget_1'], callback_data='budget_1')],
        [InlineKeyboardButton(TEXTS[lang]['quote_flow']['budget_2'], callback_data='budget_2')],
        [InlineKeyboardButton(TEXTS[lang]['quote_flow']['budget_3'], callback_data='budget_3')],
        [InlineKeyboardButton(TEXTS[lang]['quote_flow']['budget_4'], callback_data='budget_4')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(get_text('quote_flow.ask_budget', user_id), reply_markup=reply_markup)
    return BUDGET

async def budget_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the budget and asks for contact info."""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    # Get the text from the button that was pressed
    # We use query.data directly for the key now, which is simpler
    budget_text_key = query.data # 'budget_1', 'budget_2', etc.
    budget_text = get_text(f'quote_flow.{budget_text_key}', user_id)
    
    context.user_data['budget'] = budget_text
    
    await query.edit_message_text(text=f"Budget selected: {budget_text}")
    await context.bot.send_message(chat_id=user_id, text=get_text('quote_flow.ask_contact', user_id))
    
    return CONTACT

async def contact_received(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores contact, sends notification to admin, and ends conversation."""
    user_id = update.message.from_user.id
    context.user_data['contact'] = update.message.text

    # --- Send Notification to Admin ---
    # Using a try/except block makes it safer in case a field is missing
    try:
        admin_notification_text = get_text('quote_flow.admin_notification', 'en').format(
            purpose=context.user_data.get('purpose', 'N/A'),
            features=context.user_data.get('features', 'N/A'),
            budget=context.user_data.get('budget', 'N/A'),
            contact=context.user_data.get('contact', 'N/A')
        )
        await context.bot.send_message(chat_id=ADMIN_USER_ID, text=admin_notification_text, parse_mode='Markdown')
    except Exception as e:
        print(f"Error sending admin notification: {e}")

    # --- Send Confirmation to User and End ---
    await update.message.reply_text(get_text('quote_flow.end_message', user_id))
    
    await send_main_menu(update, context, user_id)
    
    # Clear the temporary data
    context.user_data.clear()
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user_id = update.message.from_user.id
    await update.message.reply_text(get_text('quote_flow.cancel_message', user_id))
    
    await send_main_menu(update, context, user_id)
    
    context.user_data.clear()
    return ConversationHandler.END