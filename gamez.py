from discord.ext import commands
import discord, time, random

class gamez(commands.Cog):
    '''gamez'''
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name='GUN')
    async def GUN(self, ctx: commands.Context):
        '''its the classic game of russian roulette theres a 1 in 6 chance that you or someone else is gonna die (you can put someones username after the command and it still works) (that canonically makes them play the game because i said so) use the command to see how lucky you or your friends are!'''
        file = discord.File("gun cock.mp3", filename="gun cock.mp3") # you have to type the filename twice for some reason
        await ctx.send(file=file)
        time.sleep(1) 
        gun = random.randint(1, 6)
        if gun == 1:
            file = discord.File("BANG.wav", filename="BANG.wav") 
            await ctx.send(file=file)
            await ctx.send('(your body collapses and there is a pool of blood on the floor)')
            await ctx.send('(type GUN to play again)')
        else:
                file = discord.File("gun dryfire!.mp3", filename="gun dryfire!.mp3=") 
                await ctx.send(file=file) 
                await ctx.send('you win!')
                await ctx.send('(type GUN to play again)')
             

    @commands.command(name='lotto')
    async def lotto(self, ctx: commands.Context, *, text: str):
        '''based on a 4d singaporean lottery! (make sure to type a 4 digit number after the command $lottery or then this command wont work'''
        won = False
        for i in range(23):
            if random.randint(0,9999)  == int(text):
                won = True
        if won:
            await ctx.send('YOU JUST WON THE LOTTO')
            file = discord.File('YOU WON THE LOTTO MATE!.MP3', filename='YOU WON THE LOTTO MATE!.MP3')
            await ctx.send(file=file)
        else:
            await ctx.send('you lost')
            file = discord.File('f in chat.wav', filename='f in chat.wav')
            await ctx.send(file=file)

def setup(bot: commands.Bot):
    bot.add_cog(gamez(bot))        

