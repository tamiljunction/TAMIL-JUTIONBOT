## Mandatory Imports
```python3
None
```
There is None Mandatory Imports. Because Var, bot and command are already automatically imported.

## Explanation
The Mandatory Imports are now automatically imported.

### Formation
Now I will show a short script to show the formation of the desired script.
```python3
from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from LEGENDBOT import CmdHelp

@bot.on(admin_cmd(pattern="Legendo$", outgoing=True))
@bot.on(sudo_cmd(pattern="Legendo$", allow_sudo=True))
async def Legendo_world(event):
    if event.fwd_from:
        return
    await eor(event, "**HELLO WORLD**")

CmdHelp("Legendo").add_command(
  "Legendo", None, "Hello World Edit."
).add()
```
