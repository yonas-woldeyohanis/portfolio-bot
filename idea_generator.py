# idea_generator.py
from telegram import Update
from telegram.ext import ContextTypes

async def start_idea_generator(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Invites the user to use the AI Brain."""
    
    text = (
        "💡 **AI Idea Generator & Chat**\n\n"
        "I have upgraded my brain! 🧠\n\n"
        "Instead of choosing from a list, **just type what you need right here.**\n\n"
        "Examples:\n"
        "• _'Give me bot ideas for a Pharmacy'_\n"
        "• _'How much for a shopping bot?'_\n"
        "• _'Write a proposal for a delivery system'_\n\n"
        "**Go ahead, type your question now! 👇**"
    )
    
    # We don't need buttons/handlers anymore because main.py will catch the text
    await update.message.reply_text(text, parse_mode='Markdown')

# We can remove industry_choice_handler and back_to_industries_handler 
# because we don't need them anymore!
async def industry_choice_handler(update, context): pass
async def back_to_industries_handler(update, context): pass