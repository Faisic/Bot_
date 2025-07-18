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

ff = [
    # 🍌 Banana
    "Las bananas son bayas verdaderas, pero las fresas no.",
    "Las bananas contienen potasio radiactivo (tranqui, no te vas a convertir en Hulk).",
    "Las bananas crecen hacia arriba, ¡no cuelgan!",
    "El 99% de las bananas comerciales vienen de la misma especie: Cavendish.",
    "Las bananas pueden hacerte resbalar... en serio, como en los dibujos animados.",

    # 🍉 Sandía
    "La sandía está compuesta por un 93% de agua.",
    "En Japón cultivan sandías cuadradas para que quepan mejor en la nevera.",
    "Las sandías han sido encontradas en tumbas egipcias.",
    "La sandía más pesada registrada pesó más de 150 kg.",
    "Texas tiene un festival dedicado solo a la sandía.",

    # 🍓 Fresa
    "Las fresas no son bayas verdaderas porque sus semillas están por fuera.",
    "Una sola fresa puede tener más de 200 semillas.",
    "Las fresas crecen en plantas rastreras, no en arbustos.",
    "En la Edad Media, las fresas eran símbolo del amor y la pureza.",
    "La fresa es la primera fruta que madura en primavera en muchos países.",

    # 🍍 Piña
    "La piña es una fusión de muchas frutas pequeñas unidas.",
    "Cristóbal Colón llevó las primeras piñas a Europa.",
    "Las piñas pueden tardar hasta 2 años en crecer completamente.",
    "En el siglo XVII, la gente alquilaba piñas para decorar fiestas.",
    "Las piñas contienen bromelina, una enzima que ablanda la carne.",

    # 🍎 Manzana
    "Las manzanas flotan en el agua porque son 25% aire.",
    "Hay más de 7.500 variedades de manzanas en el mundo.",
    "Las semillas de manzana contienen una pequeña cantidad de cianuro.",
    "Una manzana promedio tiene alrededor de 100 calorías.",
    "Las manzanas son parte de la familia de las rosas 🌹.",

    # 🍊 Naranja
    "El color 'naranja' viene del nombre de la fruta, no al revés.",
    "Las naranjas no siempre son naranjas: en climas tropicales pueden ser verdes.",
    "Una naranja contiene más del 100% de la vitamina C diaria recomendada.",
    "Las naranjas son un híbrido entre el pomelo y la mandarina.",
    "España es uno de los mayores exportadores de naranjas del mundo.",

    # 🥭 Mango
    "El mango es la fruta nacional de India, Pakistán y Filipinas.",
    "Un solo mango puede pesar hasta 5 kilos.",
    "El mango tiene más de 4.000 años de cultivo registrado.",
    "Algunas personas son alérgicas a la piel del mango.",
    "El mango es pariente del anacardo y el pistacho.",

    # 🥝 Kiwi
    "El kiwi es originario de China, no de Nueva Zelanda.",
    "Antes se llamaba 'grosella china'.",
    "Tiene más vitamina C que una naranja.",
    "La piel del kiwi es comestible y muy nutritiva.",
    "Los kiwis crecen en enredaderas como las uvas.",

    # 🍇 Uvas
    "Las uvas pueden explotar si las metes en el microondas (¡no lo hagas!).",
    "Una sola vid bien cuidada puede vivir más de 100 años.",
    "Las uvas se pueden transformar en pasas, jugo o vino.",
    "Existen uvas sin semillas creadas por hibridación.",
    "En España es tradición comer 12 uvas al ritmo de las campanadas de Año Nuevo.",
]

@bot.command()
async def funfact(cxt):
    cxt.send(random.choice(ff))

bot.run("MTM4MjA0MjM2Njk4NjI4OTM2Mw.GbK9Zz.RkPQLIvH8iFfX9It9av3Ys2xUMQGLLR8Zh8R_o")