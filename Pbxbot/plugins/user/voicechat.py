import uuid

from pyrogram import Client
from pyrogram.raw import base
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.phone import (
    CreateGroupCall,
    DiscardGroupCall,
    ExportGroupCallInvite,
    GetGroupParticipants,
)
from pyrogram.types import Message

from . import HelpMenu, Symbols, group_only, Pbxbot, on_message


@on_message("startvc", chat_type=group_only, admin_only=True, allow_stan=True)
async def startvc(client: Client, message: Message):
    if len(message.command) > 1:
        call_name = await Pbxbot.input(message)
    else:
        call_name = "Pbxbot VC"

    Pbx = await Pbxbot.edit(message, "Starting Voice Chat...")
    try:
        await client.invoke(
            CreateGroupCall(
                peer=(await client.resolve_peer(message.chat.id)),
                random_id=int(str(uuid.uuid4().int)[:8]),
                title=call_name,
            )
        )
        await Pbxbot.delete(Pbx, "Voice Chat started!")
    except Exception as e:
        await Pbxbot.error(Pbx, str(e))


@on_message("endvc", chat_type=group_only, admin_only=True, allow_stan=True)
async def endvc(client: Client, message: Message):
    Pbx = await Pbxbot.edit(message, "Ending Voice Chat...")

    try:
        full_chat: base.messages.ChatFull = await client.invoke(
            GetFullChannel(channel=(await client.resolve_peer(message.chat.id)))
        )
        await client.invoke(DiscardGroupCall(call=full_chat.full_chat.call))
        await Pbxbot.delete(Pbx, "Voice Chat ended!")
    except Exception as e:
        await Pbxbot.error(Pbx, str(e))


@on_message("vclink", chat_type=group_only, allow_stan=True)
async def vclink(client: Client, message: Message):
    Pbx = await Pbxbot.edit(message, "Getting Voice Chat link...")

    try:
        full_chat: base.messages.ChatFull = await client.invoke(
            GetFullChannel(channel=(await client.resolve_peer(message.chat.id)))
        )

        invite: base.phone.ExportedGroupCallInvite = await client.invoke(
            ExportGroupCallInvite(call=full_chat.full_chat.call)
        )
        await Pbxbot.delete(Pbx, f"Voice Chat Link: {invite.link}")
    except Exception as e:
        await Pbxbot.error(Pbx, f"`{e}`")


@on_message("vcmembers", chat_type=group_only, admin_only=True, allow_stan=True)
async def vcmembers(client: Client, message: Message):
    Pbx = await Pbxbot.edit(message, "Getting Voice Chat members...")

    try:
        full_chat: base.messages.ChatFull = await client.invoke(
            GetFullChannel(channel=(await client.resolve_peer(message.chat.id)))
        )
        participants: base.phone.GroupParticipants = await client.invoke(
            GetGroupParticipants(
                call=full_chat.full_chat.call,
                ids=[],
                sources=[],
                offset="",
                limit=1000,
            )
        )
        count = participants.count
        text = f"**Total Voice Chat Members:** `{count}`\n\n"
        for participant in participants.participants:
            text += f"{Symbols.bullet} `{participant.peer.user_id}`\n"

        await Pbx.edit(text)
    except Exception as e:
        await Pbxbot.error(Pbx, str(e))


HelpMenu("voicechat").add(
    "startvc",
    "<vc name (optional)>",
    "Start a voice chat in the group with the given name (optional)",
    "startvc Pbxbot 2.0 VC",
    "Only admins with manage voice chats permission can use this command.",
).add(
    "endvc",
    None,
    "End the voice chat in the group",
    "endvc",
    "Only admins with manage voice chats permission can use this command.",
).add(
    "vclink",
    None,
    "Get the invite link of currennt group's voice chat.",
    "vclink",
).add(
    "vcmembers",
    None,
    "Get the list of members in current group's voice chat.",
    "vcmembers",
    "Only admins with manage voice chats permission can use this command.",
).info(
    "Manage Voice Chats",
).done()
