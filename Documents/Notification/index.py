import discord
import os
import time, datetime, sched
from discord.ext import commands, tasks
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


#Next, we create an instance of a Client. This is the connection to Discord.
#client = discord.Client()

#The @client.event() decorator is used to register an event. This is an asynchronous library, so things are done with callbacks. A callback is a function that is called when something else happens. In this code, the on_ready() event is called when the bot is ready to start being used. Then, when the bot receives a message, the on_message() event is called.
# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))
# def __init__(self):
#     self.client = discord.Client()
#     self.on_ready = self.client.event(self.on_ready)
#     self.on_message = self.client.event(self.on_message)
def send(message):
    message.channel.send('Stamina is full')
async def func1():
  await bot.wait_until_ready()
  channel = bot.get_channel(997185227757727757)
  await channel.send("GB NOW!")
async def func2():
  await bot.wait_until_ready()
  channel = bot.get_channel(997185227757727757)
  await channel.send("GB in 2 mins!")
async def func3():
  await bot.wait_until_ready()
  channel = bot.get_channel(997185227757727757)
  await channel.send("GB in 1 mins!")
#The on_message() event triggers each time a message is received but we don't want it to do anything if the message is from ourselves. So if the Message.author is the same as the Client.user the code just returns.
bot = commands.Bot(command_prefix="/")
@bot.event
async def on_message(message):
    if message.content.startswith("help"):
        await message.channel.send('NOTIFICATIONS:\nSekai\nResin\nGB')
#Next, we check if the Message.content starts with '$hello'. If so, then the bot replies with 'Hello!' to the channel it was used in.
    if message.content.startswith('Sekai'):
        t = 5 * 60 * 60
        while t:
            mins,secs = divmod(t, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            time.sleep(1)
            t -= 1
            if mins == 0 and secs == 0:
                await message.channel.send(timer)
        await message.channel.send('Stamina is full')


# @bot.event
# async def on_ready():
#   print('We have logged in as {0.user}'.format(bot))
#         #initializing scheduler
#   scheduler = AsyncIOScheduler(timezone = "US/Eastern")
#         #sends "Your Message" at 12PM and 18PM (Local Time)
#   scheduler.add_job(func1, CronTrigger(hour="14, 19", minute="0", second="0")) 
#   scheduler.add_job(func2, CronTrigger(hour="13, 18", minute="58", second="0")) 
#   scheduler.add_job(func3, CronTrigger(hour="13, 18", minute="59", second="0")) 
#         #starting the scheduler
#   scheduler.start()    
    
bot.run('OTk3MTc0MDA5MzI4MzI0Njc4.GlMtl_.T02tUPugnqOJCV_nu8LUEDB-nY08Tk3G8u2WFs')
