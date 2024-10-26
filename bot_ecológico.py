import discord
from discord.ext import commands
import random

manualidades_list = ["Crea una maceta usando botella de plástico.", 
                     "Elabora un organizador usando tubos de PVC."]

def obtener_manualidad():
    return random.choice(manualidades_list)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="{", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} se ha conectado a Discord.")

@bot.command(name="manualidad")
async def enviar_manualidad(ctx):
    idea = obtener_manualidad()
    await ctx.send(f"Idea de manualidad: {idea}")

bot.run("Token")
