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

from pyrogram.types import InlineKeyboardButton
import config
from SHUKLAMUSIC import app

# Coloured buttons need a Pyrogram version that knows ButtonStyle (Kurigram, PyroTGFork...).
# On an older Pyrogram the buttons simply stay grey and the bot keeps working.
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    ButtonStyle = None


def _btn(color=None, **kwargs):
    """color: "GREEN", "RED" or "BLUE". Falls back to a normal button if the library can't colour it."""
    names = {"GREEN": "SUCCESS", "RED": "DANGER", "BLUE": "PRIMARY"}
    if color and ButtonStyle is not None:
        try:
            return InlineKeyboardButton(style=getattr(ButtonStyle, names[color]), **kwargs)
        except (TypeError, AttributeError):
            pass
    return InlineKeyboardButton(**kwargs)


def start_panel(_):
    buttons = [
        [
            _btn(
                "GREEN",
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
            _btn("GREEN", text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            # Add me in your group: green
            _btn(
                "GREEN",
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            # Owner: red, About: green
            _btn("RED", text=_["S_B_5"], user_id=config.OWNER_ID),
            _btn("GREEN", text=_["S_B_10"], callback_data="shiv_Shashank"),
        ],
        [
            # Support: green, Update: blue
            _btn("GREEN", text=_["S_B_2"], url=config.SUPPORT_CHAT),
            _btn("BLUE", text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        # Help and commands: green
        [_btn("GREEN", text=_["S_B_4"], callback_data="settings_back_helper")],
    ]
    return buttons
    
