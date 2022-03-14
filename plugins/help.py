from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"حاليًا يدعم فقط Youtube Single (بدون قائمة تشغيل) فقط أرسل Youtube Url 🌚"
    await message.reply_text(helptxt)
