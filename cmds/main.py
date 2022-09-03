import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json

with open('setting.json','r',encoding='utf8') as jfile:
 jdata = json.load(jfile)

class Main(Cog_Extension):
  @commands.command()
  async def ping(self,ctx):
    await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

  @commands.command()
  async def about(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於我", color=0xff7b00)
    embed.set_author(name="BOT", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="創建者", value="奈虹靈波NeiHun", inline=False)
    embed.add_field(name="開發公司", value="無(自創)", inline=False)
    embed.add_field(name="功能", value="綜合(詳細內容請見「h!help_all」)", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def help_all(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="指令總覽", description="全部的指令一覽表", color=0xe5f505)
    embed.set_author(name="NeiHun_Bot", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="講解:", value="如果要觀看詳細的指令說明，請輸入「h!xxxx_help」(叉叉為該指令的名稱，如:「h!ping」的說明請輸入「h!ping_help」)", inline=False)
    embed.add_field(name="h!help_all", value="指令一覽表", inline=False)
    embed.add_field(name="h!ping", value="顯示ping值(四捨五入到整數位)", inline=False)
    embed.add_field(name="h!開發", value="隨機發出一張開發者(奈虹、七彗)的平台(不一定是Discord)大頭照", inline=False)
    embed.add_field(name="h!貓咪", value="隨機發出一張有關貓咪的圖片", inline=False)
    embed.add_field(name="h!about", value="這個機器人的介紹", inline=False)
    embed.add_field(name="h!sayd [訊息] (通常管管使用)", value="請機器人複誦訊息(原訊息刪除)", inline=False)
    embed.add_field(name="h!load/h!unload/h!reload (通常開發者使用)", value="重新讀取某程式碼資料夾", inline=False)
    embed.add_field(name="h!add [數字] [數字]", value="將兩個整數相加並回報結果", inline=False)
    embed.add_field(name="h!round [數字] [位數]", value="將一個數四捨五入到...位(格式請看「h!round_help」)", inline=False)
    embed.add_field(name="h!guess", value="終極密碼!", inline=False)
    embed.add_field(name="h!help", value="程式碼資料夾及功能名稱一覽", inline=False)
    embed.add_field(name="機器人官方使用教學影片", value="https://www.youtube.com/watch?v=dQw4w9WgXcQ", inline=False)
    embed.set_footer(text="指令持續更新中!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def ping_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!ping", color=0xFF00FF)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於ping值", value="簡單來說ping值在這裡的意思指的是「機器人判斷延遲時長」，一般使用的單位為「毫秒」，本機器人使用的單位也是毫秒，並已四捨五入到整數位!", inline=False)
    embed.add_field(name="更多內容/參考資料", value="https://blog.trendmicro.com.tw/?p=71287", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def 開發_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!開發", color=0x008080)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令", value="沒想到你會想看看這個奇怪的指令有什麼解說www。好吧，由於開發者是一個有億點點自戀的貓咪，另一方面，他也是一個喜歡被關注的感覺(當然是正面的關注)，所以開發了這個指令，但相信一定很少!很少!!人會用的。", inline=False)
    embed.add_field(name="指令內容", value="當送出指令，機器人將會傳出「隨機一張」開發者的社群頭貼。", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def 貓咪_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!貓咪", color=0x800000)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令", value="貓咪當然會喜歡貓咪的!所以這個指令一定為了滿足貓奴們以及貓咪們的心靈，製造出來也是不可避免的吧?", inline=False)
    embed.add_field(name="指令內容", value="當送出指令，機器人將會傳出「隨機一張」有關貓咪的圖片。", inline=False)
    embed.add_field(name="更多內容/參考資料", value="https://zh.m.wikipedia.org/zh-tw/%E7%8C%AB , https://www.youtube.com/watch?v=xs7YVsp7Af8", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def sayd_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!sayd", color=0xF0F8FF)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="此指令使用方式", value="首先先打出「h!sayd」，之後打出一個空格，空格後直接輸入你想要複誦的內容(如:「h!sayd haha」)，送出後機器人將發送一則確認訊息(為了方便檢舉訊息及後續偵查)，接著把你的要求訊息刪除，最後再送出你所要的內容。", inline=False)
    embed.add_field(name="指令內容", value="當送出指令，機器人將會傳出一則確認訊息(格式:【發送訊息者的mention】已送出機器人複誦訊息要求!)，然後才會送出你所要求的複誦內容。", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def load_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!load", color=0xC0C0C0)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令", value="load顧名思義就是載入一個東西，在這裡是將一個程式碼檔案上載，所以除非是要測試或保養機器人，這個功能很少在使用，使用的人也只會是開發者。", inline=False)
    embed.add_field(name="此指令的使用方式", value="先輸入「h!load」，然後空格，之後直接輸入要上載的檔案名稱(不需副檔名)(如:上載「abc.py」，則輸入:「h!load abc」)。如果機器人傳送訊息顯示:「Loaded ... done!」就是成功囉!", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def unload_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!unload", color=0x808000)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令", value="unload顧名思義就是載出一個東西，在這裡是將一個程式碼檔案載出，所以除非是要測試或保養機器人，這個功能很少在使用，使用的人也只會是開發者。", inline=False)
    embed.add_field(name="此指令的使用方式", value="先輸入「h!unload」，然後空格，之後直接輸入要載出的檔案名稱(不需副檔名)(如:載出「abc.py」，則輸入:「h!unload abc」)。如果機器人傳送訊息顯示:「Un - Loaded ... done!」就是成功囉!", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def reload_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!reload", color=0xC0C0C0)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令", value="reload顧名思義就是重新載入一個東西，在這裡是將一個程式碼檔案重載，所以除非是要測試或保養機器人，這個功能很少在使用，使用的人也只會是開發者。", inline=False)
    embed.add_field(name="此指令的使用方式", value="先輸入「h!reload」，然後空格，之後直接輸入要重載的檔案名稱(不需副檔名)(如:重載「abc.py」，則輸入:「h!reload abc」)。如果機器人傳送訊息顯示:「Re - loaded ... done!」就是成功囉!", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def guess_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!guess", color=0x00FFFF)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令遊戲", value="「終極密碼」想必是大家耳熟能詳的經典遊戲，規則也簡單:從範圍中選擇1個整數數字，如果選擇的數字小於「終極密碼」，範圍將縮小至「1到你選擇的數字」，數字大於則反之，在限定的次數內猜中密碼就獲勝了!", inline=False)
    embed.add_field(name="指令內容", value="發出指令後，依照機器人指示直接輸入整數的阿拉伯數字，以1~100為例，如此一來就有6次機會，在這6次機會中猜出正確的密碼即為獲勝!", inline=False)
    embed.add_field(name="更多內容/參考資料", value="https://zh.wikipedia.org/wiki/%E7%B5%82%E6%A5%B5%E5%AF%86%E7%A2%BC", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def add_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!add [數字] [數字]", color=0xC0C0C0)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令", value="目前這個指令只能計算兩個整數的和，格式則是在「h!add」之後用空格隔開兩數(第一個數字和開頭指令也需用一個空格隔開)", inline=False)
    embed.add_field(name="指令內容", value="發出指令後，機器人會回答「:[數字1]加上[數字2]等於[和]喔!」", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def round_help(self,ctx):
    timestamp=datetime.datetime.today().strftime(r'%I:%M %p')
    embed=discord.Embed(title="關於h!round [數字] [位數]", color=0x00FF00)
    embed.set_author(name="指令講解", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYyspfgC_wMT1hWkVRykwgfx_PDnhTWeFD_g&usqp=CAU")
    embed.add_field(name="關於此指令(重要)", value="數字可以填整數，位數請填你要四捨五入的位數:0(整數)、1(十位數)、2(百位數)......-1(小數點後1位)、-2(小數點後2位)......依此類推", inline=False)
    embed.add_field(name="指令內容", value="發出指令後，機器人會回答:「[數字]的四捨五入結果為:[結果]」", inline=False)
    embed.add_field(name="更多內容/參考資料", value="無", inline=False)
    embed.set_footer(text="奈虹祝你有個美好的一天!" + "     " + str(timestamp))
    await ctx.send(embed=embed)

  @commands.command()
  async def sayd(self,ctx,*,msg) :
   author = ctx.message.author.mention
   print(author)
   await ctx.send(f"{author} 已送出機器人複誦訊息要求!")
   await ctx.message.delete()
   await ctx.send(msg)

  @commands.command()
  async def add(self,ctx,num:int,num2:int):
   await ctx.send(f'{num}加上{num2}等於{num+num2}喔!')

  @commands.command()
  async def round(self,ctx,num:float,digit:int):
    digit = 10 ** digit
    numb = num
    numb /= digit
    n = round(numb)
    n *= digit
    await ctx.send(f'你的四捨五入結果為:{n}')
  
  @round.error
  async def round_error(self,ctx,error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
      await ctx.send("﹝錯誤﹞請輸入參數!")
    elif isinstance(error, commands.errors.BadArgument):
      await ctx.send("﹝錯誤﹞請輸入正確的數值(被計算的數值須為一個「數字」；位數須為一個「整數」)!")
    else:
      await ctx.send("﹝錯誤﹞出現錯誤喔!")

def setup(bot):
  bot.add_cog(Main(bot))