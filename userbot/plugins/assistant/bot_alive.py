from telethon import events
from . import *
from userbot import ALIVE_NAME
from userbot import bot
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"
PM_IMG = "https://telegra.ph/file/404bdfb481fba8ca7bef3.jpg"
pm_caption = "『Lêɠêɳ̃dẞø†』Is Ôñĺîne \n\n"
pm_caption += "➥ Ôwñêř ~ {legend_mention}\n"
pm_caption += "╭──────────────
pm_caption += "┣─ Ťêlethon: `1.15.0` \n"
pm_caption += "┣─ 『Lêɠêɳ̃dẞø†』: `{LEGENDversion}` \n"
pm_caption += f"┣─ Çhâññel: [Channel](https://t.me/Its_LegendBot) \n"
pm_caption += "┣─ **License** : [GNU General Public License v3.0](github.com/LEGEND-OS/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += "┣─ Copyright: By [ 『Lêɠêɳ̃dẞø†』 ](https://t.me/Legend_Userbot)\n"
pm_caption += "┣─ [Assistant By 『Lêɠêɳ̃dẞøy』](https://t.me/Its_LegendBoy)"
pm_caption += "╰──────────────
pm_caption += "»»» [『Lêɠêɳ̃dẞø†』](https://t.me/Legend_Userbot) «««"
# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
