from . import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from . import *
from telethon import TelegramClient
from superos.Config.Config import Config
from superos.utils import load_module, start_assistant
from superos import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")

hl = Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"



LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()


import glob
path = 'superos/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if LOAD_ASSISTANT == True:
    path = "superos/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                start_assistant(shortname.replace(".py", ""))
            except Exception as er:
                print(er)

print(f"""『🔱🇱 🇪 🇬 🇪 🇳 🇩 B O T 🔱』➙𖤍࿐ IS ON!!! LEGEND VERSION :- {LEGENDversion}
TYPE :- " .gpromote @Legend_Mr_Hacker " OR .legend OR .ping CHECK IF I'M ON!
╔════❰LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - LEGEND
║┣⪼{LEGEND_PIC}
║┣⪼ CREATOR -@Legend_Mr_Hacker
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
