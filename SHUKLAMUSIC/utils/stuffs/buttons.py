# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums

try:  # coloured buttons (same ButtonStyle that the broadcast buttons use)
    from pyrogram.enums import ButtonStyle
except ImportError:
    try:
        from pyrogram.types import ButtonStyle
    except ImportError:
        ButtonStyle = None

# Colour pattern of every row of buttons, left to right: green, blue, red.
# Names: SUCCESS = green, PRIMARY = blue, DANGER = red, None = normal (no colour).
COLOR_PATTERN = ["SUCCESS", "PRIMARY", "DANGER"]


def _btn(text, callback_data, color=None):
    """A button with a colour. If this pyrogram version has no colour support, a normal button."""
    style = getattr(ButtonStyle, color, None) if (ButtonStyle is not None and color) else None
    if style is not None:
        try:
            return InlineKeyboardButton(text, callback_data=callback_data, style=style)
        except TypeError:  # pyrogram version does not know "style"
            pass
    return InlineKeyboardButton(text, callback_data=callback_data)


class BUTTONS(object):
    MBUTTON = [
        [_btn("ᴄʜᴀᴛ-ɢᴘᴛ", "mplus HELP_ChatGPT", COLOR_PATTERN[0]), _btn("ɢʀᴏᴜᴘs", "mplus HELP_Group", COLOR_PATTERN[1]), _btn("sᴛɪᴄᴋᴇʀs", "mplus HELP_Sticker", COLOR_PATTERN[2])],
        [_btn("ᴛᴀɢ-ᴀʟʟ", "mplus HELP_TagAll", COLOR_PATTERN[0]), _btn("ɪɴꜰᴏ", "mplus HELP_Info", COLOR_PATTERN[1]), _btn("ᴇxᴛʀᴀ", "mplus HELP_Extra", COLOR_PATTERN[2])],
        [_btn("ɪᴍᴀɢᴇ", "mplus HELP_Image", COLOR_PATTERN[0]), _btn("ᴀᴄᴛɪᴏɴ", "mplus HELP_Action", COLOR_PATTERN[1]), _btn("sᴇᴀʀᴄʜ", "mplus HELP_Search", COLOR_PATTERN[2])],
        [_btn("ғᴏɴᴛ", "mplus HELP_Font", COLOR_PATTERN[0]), _btn("ɢᴀᴍᴇs", "mplus HELP_Game", COLOR_PATTERN[1]), _btn("ᴛ-ɢʀᴀᴘʜ", "mplus HELP_TG", COLOR_PATTERN[2])],
        [_btn("ɪᴍᴘᴏsᴛᴇʀ", "mplus HELP_Imposter", COLOR_PATTERN[0]), _btn("ᴛʀᴜᴛʜ-ᴅᴀʀᴇ", "mplus HELP_TD", COLOR_PATTERN[1]), _btn("ʜᴀsᴛᴀɢ", "mplus HELP_HT", COLOR_PATTERN[2])],
        [_btn("ᴛᴛs", "mplus HELP_TTS", COLOR_PATTERN[0]), _btn("ғᴜɴ", "mplus HELP_Fun", COLOR_PATTERN[1]), _btn("ǫᴜᴏᴛʟʏ", "mplus HELP_Q", COLOR_PATTERN[2])],
        [_btn("◁", f"settings_back_helper", COLOR_PATTERN[0]), _btn("▷", f"managebot123 settings_back_helper", COLOR_PATTERN[1])],
    ]
    
