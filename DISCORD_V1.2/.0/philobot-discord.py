#Code writed by sudomadeira
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import textwrap

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client = commands.Bot(command_prefix='#')

@client.event
async def on_ready():
    print('Se estou online, logo existo!')
    print(client.user.name)
    print("-----------------------------")

@client.command()
async def status(ctx):
    await ctx.send("Pensando sabe...")

@client.command()
async def versao(ctx):
    await ctx.send("Versão 1.1 - 01/06/20")
    await ctx.send("Versão 1.2 - 05/07/20")

@client.command()
async def credits(ctx):
    await ctx.send("By @sudomadeira")

@client.command()
async def comandos(ctx):
    await ctx.send("------ COMANDOS ------\n-> Prefixo: #\n-> Comando principal: Prefixo + PhiloBot + mensagem do "
                   "usuário\n Siga no Twitter: twitter.con/bot_philosopher \n-> Bot por @sudomadeira")


@client.command()
async def commands(ctx):
    await ctx.send("------ COMMANDS ------\n-> Prefix: #\n-> Main Command: Prefix + PhiloBot + user message \n-> Bot "
                   "by @sudomadeira")

@client.command(aliases=["limpar50", "limpar100"])
async def limpar(ctx):

    if "limpar50":
        await ctx.channel.purge(limit=50)
        print("50 mensagens limpas")

    if "limpar100":
        await ctx.channel.purge(limit=100)
        print("100 mensagens limpas")




@client.command(aliases=["PhiloBot", "philobot", "PHILOBOT"])
async def citacao(ctx, *, mensagem):
    #await ctx.send(f'"{mensagem}"\n-Aristóteles')

    filosofo = [
        Image.open('images/adamsmith.png'),
        Image.open('images/alanturing.png'),
        Image.open('images/aristoteles.png'),
        Image.open('images/bakunin.png'),
        Image.open('images/castro.png'),
        Image.open('images/chaplin.png'),
        Image.open('images/che.png'),
        Image.open('images/curie.png'),
        Image.open('images/dalailama.png'),
        Image.open('images/descartes.png'),
        Image.open('images/FUKO.png'),
        Image.open('images/jesus.png'),
        Image.open('images/karnal.png'),
        Image.open('images/lenin.png'),
        Image.open('images/MANDELA.png'),
        Image.open('images/maquiavel.png'),
        Image.open('images/martin.png'),
        Image.open('images/marx.png'),
        Image.open('images/mussolini.png'),
        Image.open("images/neto.png"),
        Image.open("images/neymar.png"),
        Image.open("images/niet.png"),
        Image.open("images/pascal.png"),
        Image.open("images/platao.png"),
        Image.open("images/rousseau.png"),
        Image.open("images/stalin.png"),
        Image.open("images/winston.png"),
        Image.open("images/albert.png"),
        Image.open("images/anyrand.png"),
        Image.open("images/bauman.png"),
        Image.open("images/camus.png"),
        Image.open("images/clarice.png"),
        Image.open("images/dilma.png"),
        Image.open("images/fiodor.png"),
        Image.open("images/freud.png"),
        Image.open("images/hannah.png"),
        Image.open("images/hawk.png"),
        Image.open("images/jobs.png"),
        Image.open("images/kimjonun.png"),
        Image.open("images/mao.png"),
        Image.open("images/newton.png"),
        Image.open("images/olavo.png"),
        Image.open("images/schop.png"),
        Image.open("images/simone.png"),
        Image.open("images/socrates.png"),
        Image.open("images/voltaire.png"),
        Image.open("images/disney.png"),
        Image.open("images/galileu.png"),
        Image.open("images/getulio.png"),
        Image.open("images/kant.png"),
        Image.open("images/lula.png"),
        Image.open("images/nikola.png"),
        Image.open("images/pitagoras.png"),
        Image.open("images/papa.png"),
        Image.open("images/troskt.png"),
        Image.open("images/beethoven.png"),
        Image.open("images/carlsagan.png"),
        Image.open("images/darwin.png"),
        Image.open("images/davinci.png"),
        Image.open("images/dompedro2.png"),
        Image.open("images/durkheim.png"),
        Image.open("images/euclides.png"),
        Image.open("images/evomorales.png"),
        Image.open("images/henriqueviii.png"),
        Image.open("images/hobbes.png"),
        Image.open("images/johnlocke.png"),
        Image.open("images/lutero.png"),
        Image.open("images/maome.png"),
        Image.open("images/marighella.png"),
        Image.open("images/michelangelo.png"),
        Image.open("images/nicolasmaduro.png"),
        Image.open("images/pasteur.png"),
        Image.open("images/robespierre.png"),
        Image.open("images/sankara.png"),
        Image.open("images/santoagostinho.png"),
        Image.open("images/sartre.png"),
        Image.open("images/shakespper.png"),
        Image.open("images/trump.png"),
        Image.open("images/vangogh.png"),
        Image.open("images/zaratruta.png"),
    ]


    img = Image.open('templates/templateNovo2.png')
    fonte = ImageFont.truetype("font/myriad.otf", 37)

    escrever = ImageDraw.Draw(img)
    escrever.text(xy=(75, 128), text=textwrap.fill(mensagem, 30), fill=(255, 255, 255), font=fonte)
    randomfilo = random.choice(filosofo)
    img.paste(randomfilo, (29, 0), randomfilo)
    img.save('citdisc.png')

    await ctx.send(file=discord.File('citdisc.png'))


client.run(TOKEN)