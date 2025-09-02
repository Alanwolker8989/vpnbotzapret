from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Профиль🥷', callback_data='profil'),
        InlineKeyboardButton(text='Купить ключ🔑', callback_data='byu_vpn')
    ],
    
    [InlineKeyboardButton(text='Тех.поддержка👨🏻‍💻', url='https://t.me/TheRYXION')],
    [InlineKeyboardButton(text='FAQ', callback_data='faq_info')]
    
])

back_kb =InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад🔚', callback_data='back')]
])


sub_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🔔 Подписаться", url="https://t.me/newsvpnzapret")],
    [InlineKeyboardButton(text="✅ Проверить подписку", callback_data="check_sub")]
])


