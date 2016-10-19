# Joker-Bot
import asyncio import discord from discord.ext import commands  token = 'MjM4Mzc1NzAyOTgwNzIyNjg5.CulUhQ.HIGCGtJc9xne2UNsyYHgwDTMrjs '  class Music:     """Example bot"""     def __init__(self, bot):         self.bot = bot      @commands.command(pass_context=True, no_pm=True)     async def ping(self, ctx, *, channel : discord.Channel):         """test."""         await bot.say("Pong!")    bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='A playlist example for discord.py') bot.add_cog(Music(bot))  @bot.event async def on_ready():     print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))  bot.run(token)
import asyncio
import discord
from discord.ext import commands

token = 'MjM4Mzc1NzAyOTgwNzIyNjg5.CulUhQ.HIGCGtJc9xne2UNsyYHgwDTMrjs
'

class Music:
    """Example bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=True)
    async def ping(self, ctx, *, channel : discord.Channel):
        """test."""
        await bot.say("Pong!")



bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='A playlist example for discord.py')
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(token)

