import discord
from discord.ext import commands
from model import get_class
import matplotlib.pyplot as plt
import os
from PIL import Image
import random 


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos uniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola! Soy un robot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            file_path = f'./{attachment.filename}'
            await attachment.save(f'./{attachment.filename}')
            Fruta, score= (get_class(model_path='./keras_model.h5', labels_path='./labels.txt', image_path= file_path))
            fruta = Fruta.strip().capitalize()
            image = Image.open(file_path).convert('RGB')
            plt.imshow(image)
            plt.axis('off')
            plt.title(f'Fruta: {fruta}\nConfianza: {score:.2f}%')
            result_path = 'result.png'
            plt.savefig(result_path)
            plt.close()
            file = discord.File(result_path, filename='result.png')
            if score >= 50:
                await ctx.send(file=file)
            else:
                await ctx.send('No pude detectarlo, seguro que es una fruta?')

            os.remove(file_path)
            os.remove(result_path)
    else:
        await ctx.send('Se te olvidó subir la imagen :/')

bot.run("MTM4MjA0MjM2Njk4NjI4OTM2Mw.GbK9Zz.RkPQLIvH8iFfX9It9av3Ys2xUMQGLLR8Zh8R_o")