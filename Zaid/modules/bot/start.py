from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    " ✦𝗛𝗘𝗬..! 𝗠𝗔𝗦𝗧𝗘𝗥..!!👋!\n\n✦ 𝗜'𝗠 𝗔 𝗣𝗢𝗪𝗘𝗥𝗙𝗨𝗟 𝗕𝗟𝗢𝗢𝗗𝗬 𝗗𝗔𝗗𝗗𝗬 𝗜𝗗 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗛𝗘𝗟𝗣𝗘𝗥?\n\n‣ 𝗜 𝗖𝗔𝗡 𝗛𝗘𝗟𝗣 𝗬𝗢𝗨 𝗧𝗢 𝗛𝗢𝗦𝗧 𝗬𝗢𝗨𝗥 𝗟𝗘𝗙𝗧 𝗖𝗟𝗜𝗘𝗡𝗧𝗦.\n\n‣ 𝗛𝗘𝗟𝗣𝗘𝗥 ✦: [sᴇssɪᴏɴ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴇʀ ʀᴏʙᴏᴛ](https://t.me/StringSesssionGeneratorRobot) \n\n‣ 𝗧𝗛𝗜𝗦 𝗜𝗦 𝗦𝗣𝗘𝗖𝗜𝗔𝗟𝗟𝗬 𝗙𝗢𝗥 𝗚𝗔𝗡𝗗𝗨 𝗣𝗘𝗢𝗣𝗟𝗘'𝗦(ʟᴀᴢʏ)\n\n‣ 𝗡𝗢𝗪 /clone {send your PyroGram String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("⚡𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥⚡", url="t.me/SHIVANSH39"),
            ],
            [
                InlineKeyboardButton("⚡𝗨𝗣𝗗𝗔𝗧𝗘𝗦⚡", url="t.me/SHIVANSH474"),
            ],
            [
                InlineKeyboardButton("⚡𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡", url="t.me/selfishworld47"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

# © By itzshukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("𝑺𝑨𝑩𝑨𝑹 𝑲𝑨𝑹𝑶...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" 💘уσυя ∂α∂∂у ιѕ яєα∂у ƒσя ƒυ¢кιηg ❥ {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
