from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"لا يدعم حاليًا سوى Youtube Single (بدون قائمة تشغيل) فقط أرسل عنوان URL على Youtube"
    await message.reply_text(helptxt)
