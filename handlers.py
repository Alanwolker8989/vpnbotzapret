from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import keybaord as kb
from database import add_user

router = Router()
CHANNEL_USERNAME = '@newsvpnzapret'


# Проверка статуса подписки
async def check_subscription(user_id: int, bot) -> bool:
    member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
    return member.status in ["member", "administrator", "creator"]


# /start
@router.message(CommandStart())
async def cmd_start(message: Message, bot):
    if not await check_subscription(message.from_user.id, bot):
        await message.answer(
            "🚫 Чтобы пользоваться ботом, подпишись на наш новостной канал:",
            reply_markup=kb.sub_kb
        )
        return

    # если подписан
    add_user(message.from_user.id, message.from_user.username)
    await message.answer(
        f"👋 Приветствую, <b>{message.from_user.first_name}</b>!\n\n"
        "Добро пожаловать в <b>VPN ZapretaNet</b> 🛡\n\n"
        "С нами твой интернет будет:\n"
        "<i>• без блокировок ❌</i>\n"
        "<i>• без медленного интернета 🐌</i>\n\n"
        "<b>Быстро. Стабильно. Анонимно 🥷</b>\n\n",
        parse_mode="HTML",
        reply_markup=kb.menu_kb
    )


# Кнопка "Проверить подписку"
@router.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery, bot):
    if await check_subscription(callback.from_user.id, bot):
        add_user(callback.from_user.id, callback.from_user.username)
        await callback.message.edit_text(
            f"👋 Приветствую, <b>{callback.from_user.first_name}</b>!\n\n"
            "Добро пожаловать в <b>VPN ZapretaNet</b> 🛡\n\n"
            "С нами твой интернет будет:\n"
            "<i>• без блокировок ❌</i>\n"
            "<i>• без медленного интернета 🐌</i>\n\n"
            "<b>Быстро. Стабильно. Анонимно 🥷</b>\n\n",
            parse_mode="HTML",
            reply_markup=kb.menu_kb
        )
    else:
        await callback.answer("❌ Ты ещё не подписан!", show_alert=True)


# Остальные твои хендлеры (профиль, назад, тарифы, FAQ)
@router.callback_query(F.data == 'profil')
async def profils(callback: CallbackQuery):
    await callback.answer("Профиль обновлён ✅")
    await callback.message.edit_text(
        "<b>ВАШ ПРОФИЛЬ🥷</b>\n\n"
        f"<b>Имя:</b> {callback.from_user.first_name}\n"
        f"<b>Текущий тариф:</b> <i>не подключён</i>\n"
        f"<b>Статус анонимности:</b> <i>активен</i>\n\n"
        "<blockquote>Доступ к настройкам ограничен, ведутся работы.</blockquote>",
        parse_mode="HTML",
        reply_markup=kb.back_kb
    )


@router.callback_query(F.data == 'back')
async def go_back(callback: CallbackQuery):
    await callback.answer("Возврат в меню 🔄")
    await callback.message.edit_text(
        f"👋 Приветствую, <b>{callback.from_user.first_name}</b>!\n\n"
        "Добро пожаловать в <b>VPN ZapretaNet</b> 🛡\n\n"
        "С нами твой интернет будет:\n"
        "<i>• без блокировок ❌</i>\n"
        "<i>• без медленного интернета 🐌</i>\n\n"
        "<b>Быстро. Стабильно. Анонимно 🥷</b>\n\n",
        parse_mode="HTML",
        reply_markup=kb.menu_kb
    )


@router.callback_query(F.data == 'byu_vpn')
async def byu_vp(callback: CallbackQuery):
    await callback.message.edit_text(
        'Список Тарифов:\n'
        'Временно в разработке...',
        reply_markup=kb.back_kb
    )


@router.callback_query(F.data == 'faq_info')
async def info_faq(callback: CallbackQuery):
    await callback.message.edit_text(
        "❓ *FAQ*\n\n"
        "💳 *Почему оплата криптой?*\n"
        "- Крипта позволяет обходить блокировки и ограничения.\n"
        "- Анонимно — без карт и паспортов.\n"
        "- Быстро — перевод за пару минут.\n\n"
        "💸 *Будет ли оплата рублями?*\n"
        "Нет. Банковские платежи = блокировки и проверки. Мы делаем упор на приватность и стабильность.\n\n"
        "🪙 *Какая крипта принимается?*\n"
        "Сейчас — USDT и TON.\n\n"
        "📘 *А если я не умею пользоваться криптой?*\n"
        "В сети полно гайд-инструкций, а процесс проще, чем кажется. Один раз разобрался — дальше всё быстро и удобно.",
        parse_mode="Markdown", reply_markup=kb.back_kb
    )
