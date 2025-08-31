from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_kb =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пофиль🥷', callback_data='profil')],
    [InlineKeyboardButton(text='Купить ключ🔑', callback_data='byu_vpn')]
])

back_kb =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад🔚', callback_data='back')]
])