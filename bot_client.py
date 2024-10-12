import discord
from gen_emodji import gen_emodji
from flip_coin import flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$Hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$Bye'):
        await message.channel.send("Bye")
    elif message.content.startswith('$Emoji'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$Coin'):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

client.run("Token")
