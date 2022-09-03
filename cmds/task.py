import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime
import random

with open('setting.json','r',encoding='utf8') as jfile:
 jdata = json.load(jfile)


class Task(Cog_Extension):
 def __init__(self,msg, *args, **kwargs):
     super().__init__(msg,*args, **kwargs)

     self.counter = 0

     async def interval():
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(1005803699312017498)
        a = 0
        while not self.bot.is_closed():
            cc = random.choice(jdata['combocheer'])   #cc=combocheer 
            await self.channel.send(f'哈囉!我已經連續運作{a}天不斷線了!{cc}')
            await asyncio.sleep(86400) #單位:秒
            a += 1
        else:
            pass

     self.bg_task = self.bot.loop.create_task(interval())

     async def xmastime_task():
         await self.bot.wait_until_ready()
         self.channel = self.bot.get_channel(1005645650433675344)
         while not self.bot.is_closed():
             now_time = datetime.datetime.today().strftime('%m%d%H%M%S')
             with open('setting.json','r',encoding='utf8') as jfile:
                 jdata = json.load(jfile)
             if now_time == jdata['xmastime'] and self.counter == 0:
                 await self.channel.send(f'<@&{jdata["holiday_mention"]}> 各位!Merry Xmas!!!')
                 self.counter == 1
                 await asyncio.sleep(2)
                 self.counter == 0
             else:
                 await asyncio.sleep(1)
                 pass
    
     async def halloweentime_task():
         await self.bot.wait_until_ready()
         self.channel = self.bot.get_channel(1005645650433675344)
         while not self.bot.is_closed():
             now_time = datetime.datetime.today().strftime('%m%d%H%M%S')
             with open('setting.json','r',encoding='utf8') as jfile:
                 jdata = json.load(jfile)
             if now_time == jdata['halloweentime'] and self.counter == 0:
                 await self.channel.send(f'<@&{jdata["holiday_mention"]}> 各位!Happy Halloween!!!')
                 self.counter == 1
                 await asyncio.sleep(2)
                 self.counter == 0
             else:
                 await asyncio.sleep(1)
                 pass
             
     self.bg_task = self.bot.loop.create_task(xmastime_task())

     self.bg_task = self.bot.loop.create_task(halloweentime_task())

def setup(bot):
   bot.add_cog(Task(bot))
