"""handlers/keywords.py — Arabic keyword replies for group chats."""

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from handlers.errors import handle_errors


LINKS = {
    "الخدمات الطلابية": "https://del-portal.kfu.edu.sa/",
    "البلاك بورد": "https://bblms.kfu.edu.sa/webapps/login/",
    "المناقشات": "https://del-portal.kfu.edu.sa/vls/",
    "البانر": "https://services.kfu.edu.sa/banner/",
    "التقويم": "https://www.kfu.edu.sa/ar/Deans/E-Learning/Pages/Interactive_Calender.aspx",
    "الدرايف": "https://drive.google.com/drive/folders/1ntddDMjYMZVdoJ8DDE-A89FkEjbnz6iZ",
}


GROUPS = {
    "المستجدين": "https://t.me/alsultan011",
    "الاستفسارات": "https://t.me/alsultan116",
    "إدارة عامة مستوى ثاني": "https://t.me/ss_2026s",
    "إدارة أعمال مستوى ثاني": "https://t.me/Alsultana3mal",
    "موارد بشرية مستوى ثاني": "https://t.me/alsultan117",
    "إدارة عامة مستوى ثالث": "https://t.me/alsultan03",
}


@handle_errors
async def keyword_handler(client: Client, message: Message) -> None:
    if not message.text:
        return

    text = message.text.strip().lower()

    if "بلاك بورد" in text:
        await message.reply_text(
            "🎓 <b>نظام البلاك بورد</b>\n\n"
            f"🔗 {LINKS['البلاك بورد']}"
        )

    elif "المناقشات" in text or "منتديات النقاش" in text:
        await message.reply_text(
            "📝 <b>منتديات النقاش</b>\n\n"
            f"🔗 {LINKS['المناقشات']}"
        )

    elif "الخدمات الطلابية" in text or "الخدمات الطلابيه" in text:
        await message.reply_text(
            "🎓 <b>الخدمات الطلابية</b>\n\n"
            f"🔗 {LINKS['الخدمات الطلابية']}"
        )

    elif "البانر" in text or "بانر" in text:
        await message.reply_text(
            "🏫 <b>نظام البانر</b>\n\n"
            f"🔗 {LINKS['البانر']}"
        )

    elif "التقويم" in text:
        await message.reply_text(
            "📅 <b>التقويم</b>\n\n"
            f"🔗 {LINKS['التقويم']}"
        )

    elif "الدرايف" in text or "درايف" in text:
        await message.reply_text(
            "📁 <b>الدرايف</b>\n\n"
            f"🔗 {LINKS['الدرايف']}"
        )

    elif "القروبات" in text or "قروبات" in text:
        groups_text = (
            "👥 <b>قروبات السلطان</b>\n\n"
            f"🆕 <a href=\"{GROUPS['المستجدين']}\">قروب المستجدين</a>\n"
            f"💬 <a href=\"{GROUPS['الاستفسارات']}\">قروب الاستفسارات</a>\n"
            f"📚 <a href=\"{GROUPS['إدارة عامة مستوى ثاني']}\">إدارة عامة مستوى ثاني</a>\n"
            f"💼 <a href=\"{GROUPS['إدارة أعمال مستوى ثاني']}\">إدارة أعمال مستوى ثاني</a>\n"
            f"👤 <a href=\"{GROUPS['موارد بشرية مستوى ثاني']}\">موارد بشرية مستوى ثاني</a>\n"
            f"📚 <a href=\"{GROUPS['إدارة عامة مستوى ثالث']}\">إدارة عامة مستوى ثالث</a>"
        )

        await message.reply_text(groups_text)


def register(app: Client) -> None:
    app.add_handler(
        MessageHandler(
            keyword_handler,
            filters.text & filters.group
        )
    )