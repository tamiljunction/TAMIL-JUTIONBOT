from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

LEGEND_pic = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
LEGEND_caption += f"        ♥️ẞø✞︎ ẞ✞︎α✞︎µѕ♥️ \n"
LEGEND_caption += f"•⚜️• Øաղ̃ҽ̈ɾ          : {mention}\n\n"
LEGEND_caption += f"•📍• 𝖑𝖊ɠêɳ̃dẞø✞︎  : {LEGENDversion}\n"
LEGEND_caption += f"•📍• ✞︎ҽ̀lҽ́ƭhøղ̃     : `{version.__version__}`\n"
LEGEND_caption += f"•📍• 𝚄ρƭเɱε         : `{uptime}`\n"
LEGEND_caption += f"•📍• 𝖦ɾσµρ           : [𝔾ɾσµρ](t.me/Legend_Userbot)\n"  

#-------------------------------------------------------------------------------

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(alive):
    if hell.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    await bot.send_file(alive.chat_id, LEGEND_pic, caption=LEGEND_caption)
    await alive.delete()

msg = f"""
**⚡ 𝖑𝖊ɠêɳ̃dẞø† ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**𝖑𝖊ɠêɳ̃dẞø† :**  `{LEGENDversion}`
**𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗  :**  **{version.__version__}**
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def hell_a(event):
    try:
        hell = await bot.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
