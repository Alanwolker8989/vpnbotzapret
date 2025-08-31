from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import keybaord as kb
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Приветствую, <b>{message.from_user.first_name}</b>!\n\n"
        "Добро пожаловать в <b>VPN ZapretaNet</b> 🛡\n\n"
        "С нами твой интернет будет:\n"
        "<i>• блокировки ❌</i>\n"
        "<i>• медленный интернет 🐌</i>\n\n"
        "<b>Быстро. Стабильно. Анонимно 🥷</b>\n\n",
        parse_mode="HTML",
        reply_markup=kb.menu_kb
    )

# кнопка профиля
@router.callback_query(F.data == 'profil')
async def profils(callback: CallbackQuery):
    await callback.answer("Профиль обновлён ✅")
    await callback.message.edit_text(
        "<b>ВАШ ПРОФИЛЬ🥷</b>\n\n"
        f"<b>Имя:</b> {callback.from_user.first_name}\n"
        f"<b>Текущий тариф:</b> <i>не подключён</i>\n"
        f"<b>Статус анонимности:</b> <i>активен</i>\n\n"
        "<blockquote>Доступ к настройкам ограничен ведутся работы.</blockquote>",
        parse_mode="HTML",
        reply_markup=kb.back_kb  # или kb.menu_kb, если кнопки нужны
    )
    
# кнопка назад для профиля     
@router.callback_query(F.data == 'back')
async def go_back(callback: CallbackQuery):
    await callback.answer("Возврат в меню 🔄")
    await callback.message.edit_text(
        f"👋 Приветствую, <b>{callback.from_user.first_name}</b>!\n\n"
        "Добро пожаловать в <b>VPN ZapretaNet</b> 🛡\n\n"
        "С нами твой интернет будет:\n"
        "<i>• блокировки ❌</i>\n"
        "<i>• медленный интернет 🐌</i>\n\n"
        "<b>Быстро. Стабильно. Анонимно 🥷</b>\n\n",
        parse_mode="HTML",
        reply_markup=kb.menu_kb
    )
    
    
@router.callback_query(F.data == 'byu_vpn')
async def byu_vp(callback: CallbackQuery):
    await callback.message.answer(
        'Список Тарифов:\n'
        'Временно в разработке...',
        reply_markup=kb.back_kb
    )