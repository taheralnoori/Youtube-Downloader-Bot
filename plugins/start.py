from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔰 قناة البوت", url="https://t.me/engineering_electrical9")],
        [InlineKeyboardButton(
            "🗼 موسوعة المهندس الكهربائي", url="https://electrical-engineer-cc40b.web.app/")],
        [InlineKeyboardButton(
            "😴 مطور البوت", url="https://t.me/ta_ja199")]
    ])
    welcomed = f"😇 مرحبا  <b>{message.from_user.first_name}</b>\nانا بوت اقوم بتنزيل اي فيديو على اليوتيوب 🔴\n 😎كل ما عليك هو ارسال رابط  فيديو من اليوتيوب الي\nوبعدها اختار الصيغة ملف (mp3 & mp4) وبعدها الدقة وانتظر 😉\nMade by:@ta_ja199 👨‍💻"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
