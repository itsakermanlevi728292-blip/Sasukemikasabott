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
from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app

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
            return InlineKeyboardButton(text=text, callback_data=callback_data, style=style)
        except TypeError:  # pyrogram version does not know "style"
            pass
    return InlineKeyboardButton(text=text, callback_data=callback_data)


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        _btn(_["BACK_PAGE"], "mbot_cb", COLOR_PATTERN[0]),
        _btn(_["BACK_BUTTON"], "settingsback_helper", COLOR_PATTERN[1]),
        _btn(_["NEXT_PAGE"], "mbot_cb", COLOR_PATTERN[2]),
    ]
    mark = second if START else first

    # 15 help buttons: 5 rows x 3 buttons. H_B_1 ... H_B_15, colours follow COLOR_PATTERN.
    rows = []
    for r in range(5):
        row = []
        for c in range(3):
            n = r * 3 + c + 1
            row.append(_btn(_[f"H_B_{n}"], f"help_callback hb{n}", COLOR_PATTERN[c]))
        rows.append(row)
    rows.append(mark)
    return InlineKeyboardMarkup(rows)


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
    
