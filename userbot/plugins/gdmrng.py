from . import *

@bot.on(admin_cmd(pattern="gm(.*)"))
async def xd(event):
    await event.edit("Sending To all Group good Morning")
    themessage = event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        lol = 0
        done = 0
        if tele.is_group:
            chat = tele.id
            try:
                await bot.send_message(chat, f"🅶🅾🅾🅳 🅼🅾🆁🅽🅸🅽🅶.")
                done += 1
            except:
                lol += 1
                pass
    await event.reply(f"I hope your morning is as bright and gorgeous as your smile.")


CmdHelp("GM").add_command(
    ".gm", None, "Wishs Good moning in all groups"
).add()