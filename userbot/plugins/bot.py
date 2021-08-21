from userbot import *
from LEGENDBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={legend})"


PM_IMG = "https://telegra.ph/file/71339ef5c1b34cffa6cb5.jpg"
pm_caption ="**ℓєgєи∂ϐοτ Is οиℓιиє**\n\n"

pm_caption += f"**┏━━━━━━━━━━━━━┓**\n"
pm_caption += f"        𖤍✞︎t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎𖤍\n"
pm_caption += f"**┣🌷 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣🌷 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣🌷 𝖑𝖊ɠêɳ̃dẞø✞︎ : {LEGENDversion}**\n"
pm_caption += f"**┣🌷 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣🌷 𝙾𝚠𝚗𝚎𝚛     : [ℓεɠεɳ∂](https://t.me/Legend_Mr_Hacker)**\n"
pm_caption += f"**┣🌷 𝙶𝚛𝚘𝚞𝚙     : [𝙶𝚛𝚘𝚞𝚙](https://t.me/Legend_Userbot)**\n"
pm_caption += f"**┗━━━━━━━━━━━━━┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/LEGEND-OS/LEGENDBOT) 🔹 [📜ℓιϲєиѕє📜](https://github.com/LEGEND-OS/LEGENDBOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("𝚋𝚝𝚊𝚕𝚟").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'bot', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Are u alive?'
).add()
