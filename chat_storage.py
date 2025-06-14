import json
import os

FILE_PATH = "chat_history.json"

def save_conversation(user_msg, bot_resp):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            chat_history = json.load(f)
    else:
        chat_history = []

    chat_history.append({"user": user_msg, "bot": bot_resp})
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(chat_history, f, ensure_ascii=False, indent=4)

def load_conversation():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
