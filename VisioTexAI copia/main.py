import keras
import discord
from discord.ext import commands
from model import get_class
intents = discord.Intents.default()
intents.message_content = True
import os, random
import requests
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def ciao(ctx):
    await ctx.send("ciao, sono VisioTexAI; un AI progettata per la descrizione di immagini da postare su social_media")


@bot.command()
async def addio(ctx):
    await ctx.send("Addio, per onore ti canto: cantami o diva del pelide achille l'ira funesta che infiniti addusse lutti agli Achei, molte anzi tempo all'orco, genrose travolse alme d'eroi; l'aspra contesa che disgiunse re Atride di Prodi el divo Achille")
    await bot.close()

def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data ["url"]
@bot.command('papera')
async def papera(ctx):
    '''Il comando restituisce la foto di una papera'''
    await ctx.send("Ciao, ecco la tua papera:")
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_cleaner_turple(result):
    label, confidence = result
    label = label. strip().replace('\n', '').rstrip('s')
    confidence_percent=int(confidence * 100)
    if confidence_percent < 50:
        answer = "Non sono sicuro di cosa sia, ma credo possa essere {label}, Sono sicuro al {confidence_percent}%"
        # Remove newline and plural 's'
    elif confidence_percent < 80:
        answer = f"Questo credo possa essere un {label}, Sono sicuro al {confidence_percent}%"

    else:
       answer = f"Questo è sicuramente {label}, Sono sicuro al {confidence_percent}%"
    return answer

@bot.command("check")
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{file_name}")
            result = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}")
            message = get_cleaner_turple(result)
            await ctx.send(message)
    else:
        await ctx.send("Hai dimenticato di caricare un'immagine")

bot.run("")
