from superos.supercmds.cmdhelp import CmdHelp
from . import *
@bot.on(admin_cmd(pattern="hey ?(.*)"))
async def hi(event):
    giveVar = event.text
    ult = giveVar[4:5]
    if not ult:
        ult = "🌺"
    await edit_or_reply(
        event,
        f"{ult}✨✨{ult}✨{ult}{ult}{ult}\n{ult}✨✨{ult}✨✨{ult}✨\n{ult}{ult}{ult}{ult}✨✨{ult}✨\n{ult}✨✨{ult}✨✨{ult}✨\n{ult}✨✨{ult}✨{ult}{ult}{ult}\n☁☁☁☁☁☁☁☁",
   )
CmdHelp("hey").add_command(
'hey', None, 'Use and See'
).add()
