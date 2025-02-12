import discord
import os
import random
import time
from discord.ext import tasks, commands
from bot_logic import gen_emodji
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy Luna!')
@bot.command()
async def bye(ctx):
    await ctx.send(f'\U0001f642')
@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())
@bot.command()
async def animo(ctx):
    img = random.choice(os.listdir('Imagenes'))
    with open(f'Imagenes\{img}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(f'Cada vez que tiras una botella de plastico a la calle un gatito muere!')
bot.run("Token")
