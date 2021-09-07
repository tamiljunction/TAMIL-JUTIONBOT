"""Send Chat Actions
Syntax: .fake <option>
        fake options: Options for fake



import asyncio

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp

@borg.on(admin_cmd(pattern="fake ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with borg.action(event.chat_id, action):
        await asyncio.sleep(86400)  # type for 10 seconds



CmdHelp("ƒακє").add_command(
  'fake', '<action>', 'This shows the fake action in the group  the actions are typing, contact, game ,location, voice, round, video, photo, document.'
).add_command(
  'gbam', '<reason> (optional)', 'Fake gban. Just for fun🤓'
).add_command(
  'picgen', None, 'Gives a fake face image'
).add()
