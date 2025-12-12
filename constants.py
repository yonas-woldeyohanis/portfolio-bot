# constants.py

# This is a dictionary of dictionaries.
# The outer keys are 'en' for English and 'am' for Amharic.
TEXTS = {
    'en': {
        'welcome_selected': "Great! You've selected English.",
        'main_menu_prompt': "How can I help you today? 👇",
        
        # --- Main Menu Buttons ---
        'portfolio_btn': "Portfolio 📂",
        'services_btn': "Services I Offer 🛠️",
        'about_btn': "About Me 👤",
        'quote_btn': "Request a Quote 📝",
        'contact_btn': "Contact Me 📞",
        'inspire_btn': "Inspire Me! 💡",
        
        # --- NEW "ABOUT ME" CONTENT ---
        'about_me_content': {
            'title': "👤 *About Me*\n\nHello! I'm Jonas, a passionate and dedicated Telegram bot developer based in Ethiopia.",
            'body': "My goal is to create bots that are not just functional, but also intuitive, reliable, and enjoyable to use. I believe a great bot can transform a business by automating tasks and creating meaningful user engagement.",
            'points_title': "\n*My Core Principles:*",
            'points': [
                {"heading": "🔹 Clean & Efficient Code", "body": "I write well-structured code that is easy to maintain and scale."},
                {"heading": "🔸 User-Centric Design", "body": "The user experience is my top priority. Bots should be simple and logical."},
                {"heading": "🔹 Reliable Solutions", "body": "I build robust bots that you can depend on to work 24/7."}
            ],
            'footer': "\nHave a project in mind? Let's bring your idea to life!"
        },

        'portfolio_response': "Here are some of the projects I'm proud of:",
        'services_response': "I build a variety of bots to solve different problems. Here's what I can do:",
        'contact_response': "You can reach me through the following channels:",
        'portfolio_projects': {
            'wedding_bot': {
                'title': "Tame & Keariyam Wedding Bot 💍",
                'image_url': "https://i.imgur.com/example1.png",
                'description': "A comprehensive wedding bot that provides guests with all the necessary information, including event schedules, locations, gift registries, and an interactive RSVP feature.",
                'features': "✓ Event Reminders\n✓ Interactive Location Sharing\n✓ Guest RSVP System\n✓ Digital Photo Album",
                'demo_link': "https://t.me/your_wedding_bot_demo_link"
            },
            'pure_love_bot': {
                'title': "Pure Love Bot ❤️",
                'image_url': "https://i.imgur.com/example2.png",
                'description': "An entertainment bot designed to engage and support university students with relationship advice, fun quizzes, and helpful materials.",
                'features': "✓ Daily Content Delivery\n✓ User-friendly Menus\n✓ Quiz & Game Functionality\n✓ Privacy Focused",
                'demo_link': "https://t.me/@TrueLoveSupport_bot"
            },
        },
        'quote_flow': {
            'start_message': "📝 Let's get started on your quote! To cancel at any time, just type /cancel.\n\nFirst, please describe the main purpose of your bot. What problem will it solve?",
            'ask_features': "Great! Now, please list the key features you'd like your bot to have. (e.g., user registration, payment processing, admin panel, etc.)",
            'ask_budget': "Understood. What is your estimated budget for this project?",
            'ask_contact': "Perfect. Lastly, please provide your name and a contact method (like your Telegram username or email) so I can send you the detailed proposal.",
            'end_message': "✅ Thank you! Your request has been sent. I will review it and get back to you within 24 hours.",
            'cancel_message': "Quote request cancelled. You can start again anytime from the main menu.",
            'admin_notification': "🔔 New Quote Request!\n\n*Purpose:* {purpose}\n*Features:* {features}\n*Budget:* {budget}\n*Contact:* {contact}",
            'budget_1': "< $250", 'budget_2': "$250 - $500", 'budget_3': "$500 - $1000", 'budget_4': "> $1000",
        },
        'services_info': {
            'title': "🛠️ *Services I Offer*\n\nI specialize in creating custom Telegram bots to automate tasks, engage users, and grow businesses. I can build:",
            'tiers': [
                {'name': "🔹 Basic Bots", 'desc': "Perfect for simple tasks like sending automated announcements, providing information (FAQs), or managing groups."},
                {'name': "🔸 Advanced Bots", 'desc': "For more complex needs, including integration with databases, accepting user input (like your quote bot!), and connecting to external APIs."},
                {'name': "♦️ E-commerce & Payment Bots", 'desc': "Full-fledged bots that can showcase products, manage a shopping cart, and securely process payments using providers like Stripe or Telegram Payments."}
            ]
        },
        'contact_info': {
            'text': "I'm always open to discussing new projects or collaborations. Feel free to reach out directly!",
            'tg_button': "Chat on Telegram 💬",
            'call_button': "Call Me 📞"
        },
        'idea_generator': {
            'title': "🤖 Select an industry below to get some creative bot ideas!",
            'back_button': "« Back to Industries",
            'industries': {
                'restaurant': {
                    'button_text': "Restaurant / Cafe 🍽️", 'ideas_title': "💡 Bot Ideas for a Restaurant:",
                    'ideas': ["*Reservation Bot:* Allow customers to book tables directly through Telegram, view the menu, and even pre-order.", "*Loyalty Program Bot:* Create a digital stamp card. After a certain number of orders, the bot can issue a discount coupon.", "*Feedback Bot:* Automatically send a short survey to customers after their visit to collect valuable feedback."]
                },
                'education': {
                    'button_text': "Education / Tutoring 🎓", 'ideas_title': "💡 Bot Ideas for Education:",
                    'ideas': ["*Quiz Bot:* Create interactive quizzes for students to test their knowledge on a subject, with instant results.", "*Course Reminder Bot:* Send students reminders about upcoming classes, assignment deadlines, and exam schedules.", "*FAQ Bot:* Instantly answer common questions about course details, admission processes, or campus facilities."]
                },
                'real_estate': {
                    'button_text': "Real Estate 🏠", 'ideas_title': "💡 Bot Ideas for Real Estate:",
                    'ideas': ["*Property Listing Bot:* Allow clients to filter available properties by location, price, and size, and view photos directly in chat.", "*Appointment Booking Bot:* Let potential buyers schedule property viewings with an agent based on their availability.", "*Mortgage Calculator Bot:* Provide a simple tool for clients to estimate their monthly mortgage payments."]
                }
            }
        },
    },

    'am': {
        'welcome_selected': "በጣም ጥሩ! አማርኛን መርጠዋል።",
        'main_menu_prompt': "ዛሬ እንዴት ልረዳዎት እችላለሁ? 👇",

        # --- Main Menu Buttons ---
        'portfolio_btn': "የስራ ዝርዝር 📂",
        'services_btn': "የማቀርባቸው አገልግሎቶች 🛠️",
        'about_btn': "ስለ እኔ 👤",
        'quote_btn': "ዋጋ ለመጠየቅ 📝",
        'contact_btn': "ያግኙኝ 📞",
        'inspire_btn': "ሀሳብ ስጠኝ! 💡",

        # --- IMPROVED AMHARIC "ABOUT ME" CONTENT ---
        'about_me_content': {
            'title': "👤 *ስለ እኔ*\n\nሰላም! እኔ ዮናስ እባላለሁ፤ በኢትዮጵያ ውስጥ የምገኝ የቴሌግራም ቦት አበልጻጊ (developer) ነኝ።",
            'body': "ዋና አላማዬ ጠቃሚ ብቻ ሳይሆኑ ለአጠቃቀም ቀላል፣ አስተማማኝ እና አስደሳች የሆኑ ቦቶችን መፍጠር ነው። አንድ ምርጥ ቦት ስራዎችን በራስ-ሰር በማከናወን እና ከተጠቃሚዎች ጋር ጠንካራ ግንኙነት በመፍጠር የንግድ ስራን መለወጥ ይችላል ብዬ አምናለሁ።",
            'points_title': "\n*የስራ መርሆዎቼ:*",
            'points': [
                {"heading": "🔹 ንፁህ እና ቀልጣፋ ኮድ", "body": "ለማስተዳደር እና ለማሳደግ ቀላል የሆነ፣ በደንብ የተዋቀረ ኮድ እጽፋለሁ።"},
                {"heading": "🔸 ተጠቃሚ-ተኮር ንድፍ", "body": "የተጠቃሚ ምቾት ቀዳሚ ትኩረቴ ነው። ቦቶች ቀላል እና ለመረዳት የሚችሉ መሆን አለባቸው።"},
                {"heading": "🔹 አስተማማኝ መፍትሄዎች", "body": "ያለማቋረጥ እንዲሰሩ ሁልጊዜ ሊተማመኑባቸው የሚችሉ ጠንካራ ቦቶችን እገነባለሁ።"}
            ],
            'footer': "\nየሚያስቡት ፕሮጀክት አለ? ሀሳብዎን ወደ እውነታ እንለውጠው!"
        },
        
        'portfolio_response': "የምኮራባቸውን ጥቂት ፕሮጀክቶች ከዚህ በታች ይመልከቱ:",
        'services_response': "የተለያዩ ችግሮችን የሚፈቱ ዘመናዊ ቦቶችን እሰራለሁ። ከዚህ በታች የማቀርባቸውን አገልግሎቶች ይመልከቱ:",
        'contact_response': "በእነዚህ መንገዶች በቀላሉ ሊያገኙኝ ይችላሉ:",
        'portfolio_projects': {
            'wedding_bot': {
                'title': "የታሜ እና የከሪያም የሰርግ ቦት 💍",
                'image_url': "https://i.imgur.com/example1.png",
                'description': "ለእንግዶች የፕሮግራም መርሃ ግብር፣ የቦታ መረጃ፣ የስጦታ ዝርዝር እና በይነተገናኝ የምላሽ መስጫ (RSVP) ያሉ ሁሉንም አስፈላጊ መረጃዎችን የሚያቀርብ ዘመናዊ የሰርግ ቦት።",
                'features': "✓ የፕሮግራም ማስታወሻ\n✓ በይነተገናኝ የቦታ ማጋሪያ\n✓ የእንግዳ ምላሽ መስጫ\n✓ ዲጂታል የፎቶ አልበም",
                'demo_link': "https://t.me/Tame_Kearyam_weddingbot"
            },
            'pure_love_bot': {
                'title': "Pure Love Bot ❤️",
                'image_url': "https://i.imgur.com/example2.png",
                'description': "ለዩኒቨርሲቲ ተማሪዎች የፍቅር ምክሮችን፣ አዝናኝ ጥያቄዎችን እና ጠቃሚ መረጃዎችን በማቅረብ እንዲዝናኑ የተነደፈ ቦት ነው።",
                'features': "✓ ዕለታዊ የይዘት አቅርቦት\n✓ ለአጠቃቀም ምቹ ምናሌዎች\n✓ የፈተና እና የጨዋታ አማራጮች\n✓ የተጠቃሚን ግላዊነት የሚጠብቅ",
                'demo_link': "https://t.me/@TrueLoveSupport_bot"
            },
        },
        'quote_flow': {
            'start_message': "📝 የዋጋ ጥያቄዎን እንጀምር! ሂደቱን በማንኛውም ጊዜ ለማቆም /cancel ብለው ይጻፉ።\n\nበመጀመሪያ፣ እባክዎ የቦትዎን ዋና አላማ ይግለጹልኝ። ምን አይነት ችግር እንዲፈታ ነው የፈለጉት?",
            'ask_features': "በጣም ጥሩ! አሁን፣ እባክዎ ቦትዎ እንዲኖራቸው የሚፈልጓቸውን ቁልፍ ገፅታዎች ይዘርዝሩ። (ምሳሌ: የተጠቃሚ ምዝገባ፣ የክፍያ ሂደት፣ የአስተዳዳሪ ገጽ፣ ወዘተ)",
            'ask_budget': "ገባኝ። ለዚህ ፕሮጀክት የገመቱት በጀት ምን ያህል ነው?",
            'ask_contact': "አብዛኛውን ጨርሰናል! በመጨረሻም፣ ዝርዝር የዋጋ መረጃውን እንድልክልዎ እባክዎ ስምዎን እና መገኛዎን (የቴሌግራም ስም ወይም ኢሜል) ያስገቡ።",
            'end_message': "✅ እናመሰግናለን! ጥያቄዎ ደርሶኛል። መረጃውን መርምሬ በ24 ሰዓት ውስጥ መልስ እሰጣለሁ።",
            'cancel_message': "የዋጋ ጥያቄው ተሰርዟል። ከዋናው ምናሌ በማንኛውም ጊዜ እንደገና መጀመር ይችላሉ።",
            'admin_notification': "🔔 አዲስ የዋጋ ጥያቄ!\n\n*አላማ:* {purpose}\n*ገፅታዎች:* {features}\n*በጀት:* {budget}\n*መገኛ:* {contact}",
            'budget_1': "< $250", 'budget_2': "$250 - $500", 'budget_3': "$500 - $1000", 'budget_4': "> $1000",
        },
        'services_info': {
            'title': "🛠️ *የማቀርባቸው አገልግሎቶች*\n\nስራዎችን በራስ-ሰር ለመስራት፣ ተጠቃሚዎችን ለማሳተፍ እና የንግድ ስራዎችን ለማሳደግ የተነደፉ የቴሌግራም ቦቶችን በመስራት ላይ ልዩ ትኩረት አደርጋለሁ። ከምሰራቸው መካከል:",
            'tiers': [
                {'name': "🔹 መሰረታዊ ቦቶች", 'desc': "ራስ-ሰር ማስታወቂያዎችን ለመላክ፣ መረጃዎችን ለማቅረብ (FAQ) ወይም ግሩፖችን ለማስተዳደር ፍቱን ናቸው።"},
                {'name': "🔸 የላቁ ቦቶች", 'desc': "ከተለያዩ ዳታቤዞች ጋር መገናኘት፣ ከተጠቃሚዎች መረጃን መቀበል (እንደዚሁ የዋጋ መጠየቂያ ቦት!) እና ከሌሎች የውጭ ኤፒአይዎች ጋር መገናኘትን የመሳሰሉ ውስብስብ ፍላጎቶችን ያሟላሉ።"},
                {'name': "♦️ የንግድ እና የክፍያ ቦቶች", 'desc': "ምርቶችን የሚያሳዩ፣ የግብይት ጋሪን የሚያስተዳድሩ እና እንደ Stripe ወይም Telegram Payments ያሉ የክፍያ አማራጮችን በመጠቀም ደህንነቱ የተጠበቀ ክፍያ የሚፈጽሙ ሙሉ ቦቶች።"}
            ]
        },
        'contact_info': {
            'text': "ስለ አዲስ ፕሮጀክቶች ለመወያየት ሁል ጊዜ ዝግጁ ነኝ። በቀጥታ ሊያገኙኝ ይችላሉ!",
            'tg_button': "በቴሌግራም ያውሩኝ 💬",
            'call_button': "ይደውሉልኝ 📞"
        },
        'idea_generator': {
            'title': "🤖 የፈጠራ የቦት ሀሳቦችን ለማግኘት ከታች አንዱን ዘርፍ ይምረጡ!",
            'back_button': "« ወደ ዘርፎች ዝርዝር ተመለስ",
            'industries': {
                'restaurant': {
                    'button_text': "ሬስቶራንት / ካፌ 🍽️", 'ideas_title': "💡 ለሬስቶራንት የሚሆኑ የቦት ሀሳቦች:",
                    'ideas': ["*የቦታ ማስያዣ ቦት:* ደንበኞች በቴሌግራም በቀጥታ ጠረጴዛ እንዲይዙ፣ ምናሌዎችን እንዲያዩ እና እንዲያዙ ያስችላል።", "*የታማኝነት ፕሮግራም ቦት:* ዲጂታል የሽልማት ካርድ ይፈጥራል። ከተወሰኑ ግዢዎች በኋላ ቦቱ የቅናሽ ኩፖን ይሰጣል።", "*የአስተያየት መስጫ ቦት:* ከጉብኝታቸው በኋላ አጭር የዳሰሳ ጥናት በመላክ ጠቃሚ አስተያየቶችን ይሰበስባል።"]
                },
                'education': {
                    'button_text': "ትምህርት / ስልጠና 🎓", 'ideas_title': "💡 ለትምህርት የሚሆኑ የቦት ሀሳቦች:",
                    'ideas': ["*የፈተና ቦት:* ተማሪዎች እውቀታቸውን እንዲፈትሹ የሚያግዙ በይነተገናኝ ጥያቄዎችን ከፈጣን ውጤት ጋር ያቀርባል።", "*የፕሮግራም ማስታወሻ ቦት:* ስለሚመጡ ክፍሎች፣ የቤት ስራ ቀነ-ገደቦች እና የፈተና መርሃ ግብሮች ማስታወሻዎችን ይልካል።", "*የተደጋጋሚ ጥያቄዎች ቦት:* ስለ ኮርስ ዝርዝሮች፣ የምዝገባ ሂደቶች ወይም የካምፓስ መረጃዎች ለሚነሱ ጥያቄዎች ፈጣን መልስ ይሰጣል።"]
                },
                'real_estate': {
                    'button_text': "ሪል እስቴት 🏠", 'ideas_title': "💡 ለሪል እስቴት የሚሆኑ የቦት ሀሳቦች:",
                    'ideas': ["*የንብረት ዝርዝር ቦት:* ደንበኞች ያሉትን ንብረቶች በቦታ፣ በዋጋ እና በመጠን እንዲያጣሩ እና ፎቶዎችን እንዲያዩ ያስችላቸዋል።", "*የቀጠሮ ማስያዣ ቦት:* ገዢዎች በወኪሉ የጊዜ ሰሌዳ ላይ በመመርኮዝ የንብረት ጉብኝት ቀጠሮ እንዲይዙ ያስችላቸዋል።", "*የብድር ማስያ ቦት:* ደንበኞች ወርሃዊ የብድር ክፍያዎቻቸውን ለመገመት የሚያስችል ቀላል መሳሪያ ያቀርባል።"]
                }
            }
        },
    }
}