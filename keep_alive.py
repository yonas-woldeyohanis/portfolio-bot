from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is Alive and Running on Render!"

def run():
    # Render assigns a random port to the PORT environment variable
    # We defaults to 10000 locally
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def start_server():
    t = Thread(target=run)
    t.start()
    