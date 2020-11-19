from aiogram import types
from typing import Tuple, Any

from aiogram.contrib.middlewares.i18n import I18nMiddleware
from config import I18N_DOMAIN,LOCALES_DIR,BASE_DIR

async def get_lang(id_user):
    pass

class ASLMidlleware(I18nMiddleware):
    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale

def setup_middleware(dp):
    i18n = ASLMidlleware(I18N_DOMAIN,LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n