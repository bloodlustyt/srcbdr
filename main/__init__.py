#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29422510
API_HASH = "9e83ca8d7423f852122bfe01e53c2fa0"
BOT_TOKEN = "5851808236:AAEPIZn6Jw4Nb-ZUpLsplT7FppjwW34_m1I"
SESSION = "BQB8-BuFnXqx83CuHvsqav_sTwriVJNhJoWtB183mLkMnKHawyF4HBS1Kf6_dn0PDvHkO50phW-ZhIsIRU9nNx-mXhT1rMuor1J1KRTtyYMYXDXepKfbGhN7FVyDgyB8wFBKmNAeVIa1C-h4-lZDq-uZChNT94iLKAnRfmQ2n3QHfniL7nSI7KiV2a8QqSWCaj6XPI6ZXvFU2ifgiJazGaAErT7jYfJWOV4igFF_q4iMPkvU-hMwbm1pBhVLjMhswAIldcdD-jpu1IQRn2bACFZFSoSMwINY8HrB4sgAui3P0NFflu3CHSau4lwpXbUGCHv3oi3fisgCAUGbXIwvmUsFAAAAAV4EZzAA"
FORCESUB = "rumblebots"
AUTH = 5033931317

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
