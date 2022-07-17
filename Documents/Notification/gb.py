import discord
import os
import time, datetime, sched
from discord.ext import commands, tasks
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

bot = commands.Bot(command_prefix="/")

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

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))
        #initializing scheduler
  scheduler = AsyncIOScheduler(timezone = "US/Eastern")
        #sends "Your Message" at 12PM and 18PM (Local Time)
  scheduler.add_job(func1, CronTrigger(hour="14, 19", minute="0", second="0")) 
  scheduler.add_job(func2, CronTrigger(hour="13, 18", minute="58", second="0")) 
  scheduler.add_job(func3, CronTrigger(hour="13, 18", minute="59", second="0")) 
        #starting the scheduler
  scheduler.start()    
  
bot.run('OTk3NzQ1NjkyNjE5NTkxNzQx.GPTY-j.3HX5wJGGAt8yUMRzfjZW_-2H40a8WsleC-jk_w')
