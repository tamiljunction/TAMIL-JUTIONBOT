
import json
import re

import requests

from userbot import *
from LEGENDBOT.utils import *
from userbot.cmdhelp import CmdHelp


async def callAPI(search_str):
    query = """
    query ($id: Int,$search: String) { 
      Media (id: $id, type: ANIME,search: $search) { 
        id
        title {
          romaji
          english
        }
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          chapters
          volumes
          season
          type
          format
          status
          duration
          averageScore
          genres
          bannerImage
      }
    }
    """
    variables = {"search": search_str}
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={"query": query, "variables": variables})
    return response.text


async def formatJSON(outData):
    msg = ""
    jsonData = json.loads(outData)
    res = list(jsonData.keys())
    if "errors" in res:
        msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
    else:
        jsonData = jsonData["data"]["Media"]
        if "bannerImage" in jsonData.keys():
            msg += f"[〽️]({jsonData['bannerImage']})"
        else:
            msg += "〽️"
        title = jsonData["title"]["romaji"]
        link = f"https://anilist.co/anime/{jsonData['id']}"
        msg += f"[{title}]({link})"
        msg += f"\n\n**τγρє** : {jsonData['format']}"
        msg += f"\n**gєияєѕ** : "
        for g in jsonData["genres"]:
            msg += g + " "
        msg += f"\n**ѕτατυѕ** : {jsonData['status']}"
        msg += f"\n**єριѕο∂є** : {jsonData['episodes']}"
        msg += f"\n**γєαя** : {jsonData['startDate']['year']}"
        msg += f"\n**ѕϲοяє** : {jsonData['averageScore']}"
        msg += f"\n**∂υяατιοи** : {jsonData['duration']} min\n\n"
        # https://t.me/Legend_Userbot/19496
        cat = f"{jsonData['description']}"
        msg += " __" + re.sub("<br>", "\n", cat) + "__"
        return msg


@bot.on(admin_cmd(pattern="anilist (.*)"))
@bot.on(sudo_cmd(pattern="anilist (.*)", allow_sudo=True))
async def anilist(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "ѕєαяϲнιиg ϐяο")
    result = await callAPI(input_str)
    msg = await formatJSON(result)
    await event.edit(msg, link_preview=True)


CmdHelp("αиιℓιѕτ").add_command(
  'anilist', '<anime name>', 'Shows you the details of the anime'
).add()
