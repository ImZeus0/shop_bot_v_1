from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import _

main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(_('👤 Мой профиль')),KeyboardButton(_('🔥 Актуальний товар'))],
    [KeyboardButton(_("🆘 Support")),KeyboardButton(_("❗️FAQ"))]
],resize_keyboard=True)