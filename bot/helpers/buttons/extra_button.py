from bot.helpers.translations import lang
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

close_button = [
    [
        InlineKeyboardButton(text=lang.CLOSE_BUTTON, callback_data="close")
    ]
]

def get_music_button(user_id: int, links: list, item_id: int):
    inline_keyboard = []
    
    # Check if links are empty
    if not links:
        inline_keyboard.append(
            [
                InlineKeyboardButton(text="No links available", callback_data="close")
            ]
        )
    else:
        for index, link in enumerate(links):
            inline_keyboard.append(
                [
                    InlineKeyboardButton(
                        text=lang.GET_MUSIC_BUTTON.format(index),
                        url=link
                    )
                ]
            )
    
        inline_keyboard.append(
            [
                InlineKeyboardButton(
                    text=lang.REDOWNLOAD_BUTTON,
                    callback_data=f"GET_{user_id}_{item_id}"
                )
            ]
        )
    
    inline_keyboard = inline_keyboard + close_button
    return InlineKeyboardMarkup(inline_keyboard)

# Add error handling for lang attributes
try:
    # Example usage of lang attributes
    lang.GET_MUSIC_BUTTON
except AttributeError:
    print("Error: Missing translation for GET_MUSIC_BUTTON")
