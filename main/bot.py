import discord
from discord.ext import commands
import json
import os

with open('setting.json','r',encoding='utf8') as jfile:
   jdata = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='h!',intents = intents)

@bot.event
async def on_ready():
   print("^^bot is online^^")
   channel = bot.get_channel(int(1001733565056290876))
   await channel.send(f'{bot.user} 上線囉!請多多指教(OYO)')

@bot.command()
async def load(ctx,extension):
   bot.load_extension(f'cmds.{extension}')
   await ctx.send(f'Loaded {extension} done!')

@bot.command()
async def unload(ctx,extension):
   bot.unload_extension(f'cmds.{extension}')
   await ctx.send(f'Un - Loaded {extension} done!')

@bot.command()
async def reload(ctx,extension):
   bot.reload_extension(f'cmds.{extension}')
   await ctx.send(f'Re - loaded {extension} done!')

for filename in os.listdir('./cmds'):
   if filename.endswith('.py'):
      bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
  bot.run(jdata['TOKEN'])
