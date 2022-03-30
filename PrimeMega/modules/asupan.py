# ⚠️ © @greyyvbss 

# ⚠️ Don't Remove Credits

import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from PrimeMega.events import register

from PrimeMega import telethn as tbot, ubot2                 

@register(pattern="^/asupan ?(.*)")

async def _(event):

    memeks = await event.reply("**Ntar dulu lagi di cariin 😑**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@WikiModeAsupan", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Inget dosa kak, tapi gpp🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Asupannya gaada komsol")

@register(pattern="^/cewedesah ?(.*)")

async def _(event):

    memeks = await event.reply("**Ntar dulu lagi di cariin 😑**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@desahancewesangesange", filter=InputMessagesFilterVoice

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Inget dosa kak, tapi gpp🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Wah gk ada, tambahin akhlak dulu gih_-")

@register(pattern="^/cowodesah ?(.*)")

async def _(event):

    memeks = await event.reply("**Ntar dulu lagi di cariin 😑**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@desahancowokkkk", filter=InputMessagesFilterVoice

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Inget dosa kak, tapi gpp🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Wah gk ada, tambahin akhlak dulu gih_-")
