import discord
import random
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send("😟")

@bot.command()
async def abc(ctx):
    await ctx.send("abcdefghijklmnopqrstuvwxyz")

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def pas(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def alien(ctx):
    await ctx.send("👽")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def re(ctx, left: int, right: int):
    await ctx.send(left - right)

@bot.command()
async def mult(ctx, left: int, right: int):
    await ctx.send(left * right)

@bot.command()
async def div(ctx, left: int, right: int):
    await ctx.send(left / right)

bot.run("aqui va el token")
