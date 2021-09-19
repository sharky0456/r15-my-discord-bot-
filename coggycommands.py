from discord.ext import commands
from discord import Member
import discord
import time

class coggy_commands(commands.Cog):
    '''commands that are coggy! (jk lmao they are just commands using cogs)'''
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="setstatus")
    @commands.is_owner()
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """this sets the bots status and only the mod can use this command."""
        await self.bot.change_presence(activity=discord.Game(name=text))
        
    @commands.command(name="whatsmahpingrn?")
    async def ping(self, ctx: commands.Context):
        """get accurate ping results from your mate R15 :)"""
        start_time = time.time()
        message = await ctx.send("getting the results hold on")
        end_time = time.time()

        await message.edit(content=f"{round(self.bot.latency * 1000)}ms\nAPI:{round((end_time - start_time) * 1000)}ms")

def setup(bot: commands.Bot):
    bot.add_cog(coggy_commands(bot))

