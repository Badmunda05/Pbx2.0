import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

SUKH = getenv("SUKH", "mongodb+srv://Badmunda_13:badmunda50@cluster0.9oyzqux.mongodb.net/?retryWrites=true&w=majority")
