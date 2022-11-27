#Github.com/Vasusen-code

import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot

from telethon import events

from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

message = "Send me the message link you want to start saving from, as a reply to this message."
          
# To-Do:
# Make these codes shorter and clean
# ofc will never do it. 

process1 = []
timer = []

#Set timer to avoid spam
async def set_timer(event, list1, list2):
    now = time.time()
    list2.append(f'{now}')
    list1.append(f'{event.sender_id}')
    await event.client.send_message(event.chat_id, 'You can start a new process again after 1 minute.')
    await asyncio.sleep(60)
    list2.pop(int(timer.index(f'{now}')))
    list1.pop(int(process1.index(f'{event.sender_id}')))
    
#check time left in timer
async def check_timer(event, list1, list2):
    if f'{event.sender_id}' in list1:
        index = list1.index(f'{event.sender_id}')
        last = list2[int(index)]
        present = time.time()
        return False, f"You have to wait {60-round(present-float(last))} seconds more to start a new process!"
    else:
        return True, None

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply("Processing!")
    s, t = await check_timer(event, process1, timer) 
    if s == False:
        return await edit.edit(t)
    if 't.me/+' in link:
        q = await join(userbot, link)
        await edit.edit(q)
        await set_timer(event, process1, timer) 
        return 
    if 't.me/' in link:
        await get_msg(userbot, Bot, event.sender_id, edit.id, link, 0)
        await set_timer(event, process1, timer) 
        
