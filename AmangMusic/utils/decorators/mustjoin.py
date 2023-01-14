from pyrogram.errors import ChatAdminRequired, ChatWriteForbidden, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from AmangMusic import app
from config import MUST_JOIN


def subcribe(func):
    async def wrapper(_, message: Message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
        if not MUST_JOIN: 
            return
        try:
            try:
                await app.get_chat_member(MUST_JOIN, message.from_user.id)
            except UserNotParticipant:
                if MUST_JOIN.isalpha():
                    anjay = "https://t.me/" + MUST_JOIN
                else:
                    chat_info = await app.get_chat(MUST_JOIN)
                    chat_info.invite_link
                try:
                    await message.reply(
                        f"Hallo {rpk}. Agar Bisa Menggunakan Bot Anda Harus Masuk Ke Channel Updates Bot Terlebih Dahulu!. Silahkan Klik Tombol Di Bawah Untuk Join Ke Channel Update Bot.",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton("💌 Join Channel Bot", url="https://t.me/idcryptoofficial")]]
                        ),
                    )
                    await message.stop_propagation()
                except ChatWriteForbidden:
                    pass
        except ChatAdminRequired:
            await message.reply(
                f"Saya bukan admin di chat MUST_JOIN chat : {MUST_JOIN} !"
            )
        return await func(_, message)

    return wrapper
