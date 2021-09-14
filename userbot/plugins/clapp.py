import asyncio
from . import *
@LEGEND.on(admin_cmd(pattern="clapp"))
async def _(event):
  await event.edit("👐👏👐👏 👐👏")
  await asyncio.sleep(1)
  await event.edit("👐👏👐👏👐👏👐")
CmdHelp("clapp").add_command(
  'clapp', None, 'Use and See'
).add()
