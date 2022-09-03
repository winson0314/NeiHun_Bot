from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
   jdata = json.load(jfile)

class Event(Cog_Extension):
   @commands.Cog.listener()
   async def on_member_join(self,member):
      print(f'{member} 加入囉!')
      channel = self.bot.get_channel(int(jdata['Welcome_channel']))
      await channel.send(f'{member} 加入囉!')

   @commands.Cog.listener()
   async def on_member_remove(self,member):
      print(f'{member} 離開了!')
      channel = self.bot.get_channel(int(jdata['Leave_channel']))
      await channel.send(f'{member} 離開了!')

   @commands.Cog.listener()
   async def on_message(self,msg):
      str = msg.content
      for i in range(4):         
         if (jdata["keyword"][i]) in str and msg.author != self.bot.user:
            await msg.channel.send('哈囉!')
   
   @commands.Cog.listener()
   async def on_command_error(self,ctx,error):
      if hasattr(ctx.command,'on_error'):
         return

      if isinstance(error, commands.errors.MissingRequiredArgument):
         await ctx.send("﹝錯誤﹞遺失參數!")
      elif isinstance(error, commands.errors.CommandNotFound):
         await ctx.send("﹝錯誤﹞沒這指令啦!")
      else:
         await ctx.send("﹝錯誤﹞發生錯誤囉!")

def setup(bot):
 bot.add_cog(Event(bot))
