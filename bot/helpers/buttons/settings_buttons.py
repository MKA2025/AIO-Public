from bot.helpers.translations import lang
from bot.helpers.database import fetch_data, insert_data
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Function to create an InlineKeyboardButton
def create_button(text: str, callback_data: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=callback_data)

# Some common button addon - Main menu and Close
exit_button = [
    [
        create_button(lang.MAIN_MENU_BUTTON, "main_menu"),
        create_button(lang.CLOSE_BUTTON, "close")
    ]
]

def main_menu_set():
    inline_keyboard = [
        [
            create_button(lang.TG_AUTH_BUTTON, "tgPanel")
        ],
        [
            create_button(lang.TIDAL_BUTTON, "tidalPanel")
        ],
        [
            create_button(lang.KKBOX_BUTTON, "kkboxPanel")
        ],
        [
            create_button(lang.QOBUZ_BUTTON, "qobuzPanel")
        ],
        [
            create_button(lang.DEEZER_BUTTON, "deezerPanel")
        ],
        [
            create_button(lang.SPOTIFY_BUTTON, "spotifyPanel")
        ],
        [
            create_button(lang.CLOSE_BUTTON, "close")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)

def tidal_menu_set():
    inline_keyboard = [
        [
            create_button(lang.AUTH_BUTTON, "ADA_tidal_panel")
        ],
        [
            create_button(lang.QUALITY_BUTTON, "QA_tidal")
        ],
        [
            create_button(lang.API_BUTTON, "apiTidal_panel")
        ]
    ]
    inline_keyboard = inline_keyboard + exit_button
    return InlineKeyboardMarkup(inline_keyboard)

# Example of using the database functions
def save_user_data(user_id: int, user_data: str):
    query = "INSERT INTO users (user_id, data) VALUES (?, ?)"
    insert_data(query, (user_id, user_data))

def get_user_data(user_id: int):
    query = "SELECT data FROM users WHERE user_id = ?"
    return fetch_data(query, (user_id,))
