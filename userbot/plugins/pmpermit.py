# pmpermit for LEGENDBOT.....

import asyncio
import io
import os
import time
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon import events, functions, Button, custom
from telethon.tl.functions.users import GetFullUserRequest
from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql
from userbot import ALIVE_NAME, PM_MSG, LEGEND_ID
from userbot.Config import Config
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
PM_TRUE_FALSE = Config.PM_DATA
from . import *
PM_PIC = os.environ.get("PM_PIC", None)
LEGENDPIC = (
    PM_PIC
    if PM_PIC
    else "https://telegra.ph/file/7b2fefb2c78c90734444d.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
DEFAULTUSER = ALIVE_NAME or "LEGEND"
myid = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={myid})"

LEGEND = (
    str(PM_MSG)
    if PM_MSG
    else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n THIS IS ILLEGAL AND REGARDED AS CRIME"
)
WARN_PIC = Config.PM_PIC or "https://telegra.ph/file/58df4d86400922aa32acd.jpg"
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
PM_ON_OFF = Config.PM_DATA
CSTM_PMP = Config.PM_MSG or "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
HELL_ZERO = "Go get some sleep retard. \n\n**Blocked !!**"
HELL_FIRST = (
    "**🔥 Hêllẞø† Prîvã†é Sêçürïty Prø†öçõl 🔥**\n\nThis is to inform you that "
    "{} is currently unavailable.\nThis is an automated message.\n\n"
    "{}\n\n**Please Choose Why You Are Here!!**".format(mention, CSTM_PMP)
)

 
if Var.PRIVATE_GROUP_ID is not None:

    @borg.on(admin_cmd(pattern="allow|.a|.approve ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit(
                    "αρρяονє∂ [{}](tg://user?id={}) τo ρм γου.".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('`Reply To User To Approve Him !`')
                return
            if not pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pmpermit_sql.approve(reply_s.sender_id, "Approved")
                await event.edit(
                        "✔️αρρяονє∂ [{}](tg://user?id={}) to pm γου.".format(firstname, reply_s.sender_id)
                    )
                await asyncio.sleep(3)
                await event.delete()
            elif pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit('`User ιѕ Already Approved !`')
                await event.delete()

                

    # Approve outgoing
    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if not chat.id in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")
                    bruh = "✔️αµƭσ αρρɾσѵε∂ ɓcµƶ σµƭɠσเɳɦ 🚶"
                    rko = await borg.send_message(event.chat_id, bruh)
                    await asyncio.sleep(3)
                    await rko.delete()

    @borg.on(admin_cmd(pattern="block|.blk ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1856561912:
                await event.edit(
                    "You tried to block my master😡. GoodBye for 100 seconds!🥱😴😪💤"
                )
                time.sleep(100)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "gєτ ℓοѕτ мγ мαѕτєя нαѕ ϐℓοϲκє∂ υ!!.\nϐℓοϲκє∂ [{}](tg://user?id={})".format(
                            firstname, chat.id
                        )
                    )
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))
        elif event.is_group:
            if chat.id == 1856561912:
                await event.edit(
                    "You tried to block my master😡. GoodBye for 100 seconds!🥱😴😪💤"
                )
                time.sleep(100)
            else:
                reply_s = await event.get_reply_message()
                if not reply_s:
                    await event.edit('`Reply To User To Block Him !`')
                    return
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                if pmpermit_sql.is_approved(event.chat_id):
                    pmpermit_sql.disapprove(event.chat_id)
                await event.edit("ϐℓοϲκє∂ [{}](tg://user?id={})".format(firstname, reply_s.sender_id))
                await event.client(functions.contacts.BlockRequest(reply_s.sender_id))
                await asyncio.sleep(3)
                await event.delete()

    @borg.on(admin_cmd(pattern="disallow|.da|.disapprove ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1856561912:
                await event.edit("Sorry, I Can't Disapprove My Master")
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "[{}](tg://user?id={}) disapproved to PM.".format(
                            firstname, chat.id
                        )
                    )
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('`Reply To User To DisApprove`')
                return
            if pmpermit_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pmpermit_sql.disapprove(reply_s.sender_id)
                await event.edit(
                    "∂ιѕαρρяονє∂ [{}](tg://user?id={}) το ρм υ.".format(firstname, reply_s.sender_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pmpermit_sql.is_approved(reply_s.sender_id):
                await event.edit('`User Not Approved Yet`')
                await event.delete()    
                

    @borg.on(admin_cmd(pattern="listallowed|.la"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Currently Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "No Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="[ℓєgєи∂ϐοτ]Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if not event.is_private:
            return
        if event.sender_id == bot.uid:
            return
        if str(event.sender_id) in DEVLIST:
            return
        if Config.LOGGER_ID is None:
            await bot.send_message(bot.uid, "Please Set `LOGGER_ID` For Working Of Pm Permit")
            return
        message_text = event.message.raw_text
        chat_ids = event.sender_id
        if HELL_FIRST == message_text:
            return
        sender = await event.client.get_entity(await event.get_input_chat())
        if chat_ids == bot.uid:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if pm_sql.is_approved(chat_ids):
            return
        if not pm_sql.is_approved(chat_ids):
            await do_pm_permit_action(chat_ids, event)
                                       
    async def do_pm_permit_action(chat_ids, event):
        if chat_ids not in PM_WARNS:
            PM_WARNS.update({chat_ids: 0})
        if PM_WARNS[chat_ids] == Config.MAX_SPAM:
            r = await event.reply(HELL_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_ids].delete()
            PREV_REPLY_MESSAGE[chat_ids] = r
            the_message = ""
            the_message += "#BLOCK\n\n"
            the_message += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
            the_message += f"Message Counts: {PM_WARNS[chat_ids]}\n"
            try:
                await bot.send_message(
                    entity=Config.LOGGER_ID,
                    message=the_message,
                    link_preview=False,
                    silent=True,
                )
                return
            except BaseException:
                pass
        
        botusername = Config.BOT_USERNAME
        tap = await bot.inline_query(botusername, "pm_warn")
        hel_ = await tap[0].click(event.chat_id)
        PM_WARNS[chat_ids] += 1
        if chat_ids in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_ids].delete()
        PREV_REPLY_MESSAGE[chat_ids] = hel_

NEEDIT = Config.INSTANT_BLOCK
if NEEDIT == "ENABLE":
    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await bot.get_entity(chat_id)
        if chat_id == bot.uid:
            return
        if chat_id == 1432756163:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if not pmpermit_sql.is_approved(chat_id):
            await bot(functions.contacts.BlockRequest(chat_id))

CmdHelp("ρмρєямιτ").add_command(
  "allow|.a|approve", "<pm use only>", "It allow the user to PM you."
).add_command(
  "disallow|.da|disapprove", "<pm use only>", "It disallows the user to PM. If user crosses the PM limit after disallow he/she will get blocked automatically"
).add_command(
  "block|.blk", "<pm use only>", "You know what it does.... Blocks the user"
).add_command(
  "listallowed|.la", None, "Gives you the list of allowed PM's list"
).add_command(
  "set var PM_DATA", "DISABLE", "Turn off pm protection by your userbot. Your PM will not be protected."
).add()
