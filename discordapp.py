from discord.ext import commands
import discord
bot = commands.Bot(command_prefix='^', intents=discord.Intents.all(),description='A simple Discord bot')

token = 'ODQ3MDE5OTQxMjExMTQ0MjEz.YK3-yg.Vt8L1Lu6oCtpmhk_sHBDT9-Nbf8'


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


bot.run(token)
