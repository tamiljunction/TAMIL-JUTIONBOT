import asyncio
import time

from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@bot.on(admin_cmd(pattern="song ?(.*)"))
@bot.on(sudo_cmd(pattern="song ?(.*)", allow_sudo=True))
async def _(event):
    query = event.text[6:]
    max_results = 1
    if query == "":
        return await eor(event, "__Please give a song name to search.__")
    legend = await eor(event, f"__Searching for__ `{query}`")
    legen_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = legen_[0], legen_[1], legen_[2], legen_[3], legen_[4]
    thumb_name = f'thumb{LOGO1}'
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, 'wb').write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await legend.edit("**Fetching Song**")
        with YoutubeDL(song_opts) as somg:
            legend_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(legend, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(legend, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(legend, "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`")
    except MaxDownloadsReached:
        return await eor(legend, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(legend, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(legend, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eod(legend, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(legend, "`There was an error during info extraction.`")
    except Exception as e:
        return await eor(legend, f"{str(type(e)): {str(e)}}")
    c_time = time.time()
    await legend.edit(f"**🎶 Preparing to upload song 🎶 :** \n\n{legend_data['title']} \n**By :** {legend_data['uploader']}")
    await event.client.send_file(
        event.chat_id,
        f"{legend_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**✘ Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {legend_mention}",
        thumb=thumb_name,
        attributes=[
            DocumentAttributeAudio(
                duration=int(legend_data["duration"]),
                title=str(legend_data["title"]),
                performer=perf,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{legend_data['title']}.mp3")
        ),
    )
    await legend.delete()
    os.remove(f"{legend_data['id']}.mp3")
