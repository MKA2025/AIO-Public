from bot.helpers.translations import lang
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Some common button addon - Main menu and Close
exit_button = [
    [
        InlineKeyboardButton(text=lang.MAIN_MENU_BUTTON, callback_data="main_menu"),
        InlineKeyboardButton(text=lang.CLOSE_BUTTON, callback_data="close")
    ]
]

def main_menu_set():
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=lang.TG_AUTH_BUTTON,
                callback_data="tgPanel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.TIDAL_BUTTON,
                callback_data="tidalPanel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.KKBOX_BUTTON,
                callback_data="kkboxPanel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.QOBUZ_BUTTON,
                callback_data="qobuzPanel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.DEEZER_BUTTON,
                callback_data="deezerPanel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.SPOTIFY_BUTTON,
                callback_data="spotifyPanel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.CLOSE_BUTTON,
                callback_data="close"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard)

def tidal_menu_set():
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=lang.AUTH_BUTTON,
                callback_data="ADA_tidal_panel"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.QUALITY_BUTTON,
                callback_data="QA_tidal"
            )
        ],
        [
            InlineKeyboardButton(
                text=lang.API_BUTTON,
                callback_data="apiTidal_panel"
            )
        ]
    ]
    inline_keyboard = inline_keyboard + exit_button
    return InlineKeyboardMarkup(inline_keyboard)

# ... (other functions remain unchanged)

def common_auth_set(provider):
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=lang.ADD_AUTH_BUTTON,
                callback_data=f"ADA_{provider}_add"
            ),
            InlineKeyboardButton(
                text=lang.REMOVE_AUTH_BUTTON,
                callback_data=f"RMA_{provider}_warn"
            )
        ]
    ]
    inline_keyboard = inline_keyboard + exit_button
    return InlineKeyboardMarkup(inline_keyboard)

# Add error handling for lang attributes
try:
    # Example usage of lang attributes
    lang.MAIN_MENU_BUTTON
except AttributeError:
    print("Error: Missing translation for MAIN_MENU_BUTTON")
