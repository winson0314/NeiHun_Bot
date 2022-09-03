import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random

class Guess(Cog_Extension):
    @commands.command()
    async def guess(self, ctx):

        win = 0
        
        # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        global lowernumber
        global highernumber
        
        await ctx.send('歡迎來到終極密碼!請從100以上的數字(限定100的倍數)，選一個數字本場遊戲的範圍(1~X)吧!(機會數計算方式:機會數=5+(X/100))')
        
        c = await self.bot.wait_for('message', check = check)

        a = int(c.content)

        lowernumber = 1
        highernumber = a
        
        number = random.randint(lowernumber, highernumber)
        print(number)

        d = 5+(a/100)

        b = int(d)
        
        await ctx.send(f"設定完畢!你有{b}次機會，範圍是1~{a}!請開始從範圍中挑選數字!")
        
        for i in range(0,b):    
            response = await self.bot.wait_for('message', check = check)
            
            try : 
                guess = int(response.content) 
            except:
                await ctx.send("請「單獨」輸入「整數數字」!扣除一次機會!")
                continue
                
            if guess == number : 
                await ctx.send("猜對了!恭喜!")
                win += 1
                break
            
            if guess < lowernumber :
                await ctx.send("超出範圍(過小)，扣除一次機會!")
            else:
                if guess > highernumber :
                    await ctx.send("超出範圍(過大)，扣除一次機會!")
                else:
                    if guess < number:
                        lowernumber = guess
                        await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
                        
                    if guess > number :
                        highernumber = guess
                        await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
        
        if win == 0:
            await ctx.send(f"次數用完囉!答案是{number}!下次再努力吧!")
               
def setup(bot):
    bot.add_cog(Guess(bot))