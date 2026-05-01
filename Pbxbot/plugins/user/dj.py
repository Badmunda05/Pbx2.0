from pyrogram import Client, filters
from pyrogram.types import Message
from pydub import AudioSegment
import os
import random
import time
from . import *

@on_message("dj", allow_stan=True)
async def bass_boost_command(client, message):
    try:
        # Check if there is a reply to the command
        if message.reply_to_message and message.reply_to_message.audio:
            original_audio = message.reply_to_message.audio
            file_id = original_audio.file_id

            # Download the audio file
            audio_path = await client.download_media(file_id)

            # Apply bass boost effect
            boosted_audio = apply_bass_boost(audio_path)

            # Send the boosted audio as a reply
            await message.reply_audio(audio=boosted_audio)

            # Clean up temporary files
            os.remove(audio_path)
            os.remove(boosted_audio)

        else:
            await message.reply_text("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴡɪᴛʜ .ᴅᴊ ᴛᴏ ᴀᴘᴘʟʏ ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ʙᴏᴏꜱᴛ ᴇꜰꜰᴇᴄᴛ.")
    except Exception as e:
        await message.reply_text(f"🚫")

def apply_bass_boost(audio_path):
    # Load audio file using pydub
    audio = AudioSegment.from_file(audio_path)

    # Apply bass boost effect (adjust the gain according to your preference)
    boosted_audio = audio.low_pass_filter(250).high_pass_filter(100).apply_gain(40)

    # Save the boosted audio as a temporary file
    boosted_audio_path = "ᴅᴊ.mp3"
    boosted_audio.export(boosted_audio_path, format="mp3")

    return boosted_audio_path

