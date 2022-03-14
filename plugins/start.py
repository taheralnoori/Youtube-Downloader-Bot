from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔰 قناة البوت", url="https://t.me/engineering_electrical9")],
        [InlineKeyboardButton(
            "🗼 موسوعة المهندس الكهربائي", url="https://electrical-engineer-cc40b.web.app/")],
        [InlineKeyboardButton(
            "😴 مطور البوت", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
