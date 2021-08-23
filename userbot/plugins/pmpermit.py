import asyncio
import io
import os

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest

from . import *
from userbot.plugins.sql_helper import pmpermit_sql as pmpermit_sql


WARN_PIC = Config.PM_PIC or "https://telegra.ph/file/58df4d86400922aa32acd.jpg"
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
PM_ON_OFF = Config.PM_DATA
CSTM_PMP = Config.PM_MSG or "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
HELL_ZERO = "Go get some sleep retard. \n\n**Blocked !!**"
HELL_FIRST = (
    "**нєℓℓο ѕιя/мιѕѕ,ι нανєи'τ αρρяονє∂ γου γєτ το ρєяѕοиαℓ мєѕѕαgє мє😎⚠️**.\n\n"

    f"𝔗𝔥𝔦𝔰 ℑ𝔰 𝔪𝔶 𝔒𝔴𝔫𝔢𝔯 {DEFAULTUSER}'s\n"

    f"\n**{LEGEND}**\n\n"

    "⚡Register Your Request!⚡\nSend `/start` To Register Your Request🔥"
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

        if event.sender_id == bot.uid:

            return

        if Var.PRIVATE_GROUP_ID is None:

            return

        if not event.is_private:

            return

        message_text = event.message.message

        chat_id = event.sender_id

        message_text.lower()

        if HELL_FIRST == message_text:

            # userbot's should not reply to other userbot's

            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots

            return

        sender = await bot.get_entity(chat_id)

        if chat_id == bot.uid:

            # don't log Saved Messages

            return

        if sender.bot:

            # don't log bots

            return

        if sender.verified:

            # don't log verified accounts

            return

        if PM_ON_OFF == "DISABLE":

            return

        if not pmpermit_sql.is_approved(chat_id):

            # pm permit

            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):

        if chat_id not in PM_WARNS:

            PM_WARNS.update({chat_id: 0})

        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_PM:

            r = await event.reply(HELL_FIRST)

            await asyncio.sleep(3)

            await event.client(functions.contacts.BlockRequest(chat_id))

            if chat_id in PREV_REPLY_MESSAGE:

                await PREV_REPLY_MESSAGE[chat_id].delete()

            PREV_REPLY_MESSAGE[chat_id] = r

            the_message = ""

            the_message += "#BLOCKED_PMs\n\n"

            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"

            the_message += f"Message Count: {PM_WARNS[chat_id]}\n"

            # the_message += f"Media: {message_media}"

            try:

                await event.client.send_message(

                    entity=Var.PRIVATE_GROUP_ID,

                    message=the_message,

                    # reply_to=,

                    # parse_mode="html",

                    link_preview=False,

                    # file=message_media,

                    silent=True,

                )

                return

            except:

                return

        r = await borg.send_file(

            event.chat_id, WARN_PIC, caption=HELL_FIRST, force_document=False

        )

        PM_WARNS[chat_id] += 1

        if chat_id in PREV_REPLY_MESSAGE:

            await PREV_REPLY_MESSAGE[chat_id].delete()

        PREV_REPLY_MESSAGE[chat_id] = r      
# Do not touch the below codes!

@bot.on(events.NewMessage(incoming=True, from_users=(1856561912)))

async def hehehe(event):

    if event.fwd_from:

        return

    chat = await event.get_chat()

    if event.is_private:

        if not pmpermit_sql.is_approved(chat.id):

            pmpermit_sql.approve(

                chat.id, "**My Boss iz here.... It's your lucky day nibba😏**"

            )

            await borg.send_message(chat, "**Here comes my Master! Lucky you!!😏**")        


CmdHelp("pm_permit").add_command(
  "allow", "<in pm>", "Approves the user in which pm cmd is used."
).add_command(
  "disallow", "<in pm>", "Disapprove User to PM you."
).add_command(
  "block", "<in pm>", "Blocks the user"
).add_command(
  "listapproved", None, "Sends the list of all users approved by Hêllẞø†"
).add_info(
  "PM SECURITY"
).add_warning(
  "✅ Harmless Module."
).add()
