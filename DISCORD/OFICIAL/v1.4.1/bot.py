""""""""""""""""""""""
PHILOSOPHER BOT DISCORD 1.2
---------------
Criado por Caio Madeira (@sudomaidera)
Disponível no Discord e no Twitter!
2020

"""""""""""""""""""""""

import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
from Lists.img_list import filosofo

client = commands.Bot(command_prefix="#", case_insensitive=True)
status = ["my mind blow", "#help", "my thoughts"]
client.remove_command('help')

mensagens = entrou = 0
message = join = 0


# ==========================================
@client.event
async def on_ready():
    text_channel_list = []
    for server in client.guilds:
        for channel in server.channels:
            if channel.type == 'Text':
                text_channel_list.append(channel)

    embed_1 = discord.Embed(colour=discord.Colour.dark_green())
    embed_1.set_footer(text=f'PHILOSOPHER BOT ESTÁ ONLINE!🟢')

    print("-----------------------------")
    print(f'\n Se o {client.user.name} pensa, logo existe.\n')
    print("-----------------------------")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(status[1])))

    # await channel.send(f'Se penso, logo existo! \n O {client.user.display_name} TA ON!')

    #await channel.send(embed=embed_1)


""""""""""""""""""""""

       COMANDOS

"""""""""""""""""""""""


# =============== INFO ================
@client.command()
async def sobre(mensagem):
    global mensagens
    mensagens += 1

    LOGO = 'https://cdn.discordapp.com/attachments/750556593199906956/761666774520430628/logoNEW.png'

    embed_1 = discord.Embed(

        title='Sobre Philosopher BOT:',
        description='Criado por Caio Madeira (@sudomadeira)',
        colour=discord.Colour.dark_green()

    )

    embed_1.set_footer(text='Instagram: @sudomadeira \n Twitter: @sudomadeira \n Github: github.com/CaioMadeira')
    embed_1.set_image(url=LOGO)
    embed_1.set_thumbnail(url=LOGO)
    embed_1.add_field(name='SOBRE:', value="Manipulação de texto atribuindo a um filosofo aleatório", inline=True)
    embed_1.add_field(name='TWITTER:', value="@bot_philosopher", inline=True)
    embed_1.add_field(name='SITE:', value="philobot-site.vercel.app", inline=True)

    await mensagem.channel.send(embed=embed_1)


# ============== VERSAO ==================================
@client.command()
async def versao(mensagem):
    global mensagens
    mensagens += 1

    embed_2 = discord.Embed(
        description="Versão: 1.4.1",
        colour=discord.Colour.dark_green()

    )
    await mensagem.channel.send(embed=embed_2)


# ====================== HELP =============================


@client.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Colour.dark_green(), timestamp=ctx.message.created_at)

    embed.set_author(name='Help/Ajuda', icon_url=ctx.author.avatar_url)

    embed.add_field(name='sobre', value="Fala um pouco sobre o BOT e seus criadores.", inline=False)
    embed.add_field(name='versao', value="Mostra a versão atual do BOT no Discord.", inline=False)
    embed.add_field(name='philobot [mensagem]',
                    value="Gera uma citação com a mensagem enviada com algum filosofo aleatório", inline=False)
    embed.add_field(name='philomaker [membro][mensagem] + imagem - (BETA) ',
                    value="Gera uma citação com a mensagem enviada com a foto enviada e o "
                          "membro mencionado", inline=False)
    embed.add_field(name='limpar [numero]', value="Apaga um determinado número de mensagens.", inline=False)
    embed.add_field(name='help_philomaker', value="Informa mais sobre o comando philomaker", inline=False)

    await ctx.send(embed=embed)

# ====================== HELP PHILOMAKER =============================


@client.command()
async def help_philomaker(ctx):
    embed = discord.Embed(color=discord.Colour.dark_green(), timestamp=ctx.message.created_at)

    embed.set_author(name='Help - Philomaker', icon_url=ctx.author.avatar_url)
    embed.set_footer(text='Apenas siga a ordem -  em relação a [membro] e [mensagem]')
    embed.add_field(name='philomaker [membro][mensagem] + imagem',
                    value="Gera uma citação com a mensagem enviada com a foto enviada e o "
                          "membro mencionado", inline=False)
    embed.set_image(url='https://media.discordapp.net/attachments/712754644987936858/761974600987967500/exemple.PNG')
    await ctx.send(embed=embed)



# ============== APAGAR MENSAGENS =========================
@client.command()
async def limpar(ctx, numero):
    numero = eval(numero)

    if numero:
        await ctx.channel.purge(limit=numero)
        print(f"{numero} mensagens limpas")

        embed_2 = discord.Embed(
            description=f'{numero} mensagens limpas',
            colour=discord.Colour.dark_green()

        )
        await ctx.channel.send(embed=embed_2)


# ==========================================================

@client.command()  # função principal
async def philobot(ctx, *, mensagem):
    try:
        img = Image.open('templateNovo.png')
        fonte = ImageFont.truetype("font/myriad.otf", 45)
        escrever = ImageDraw.Draw(img)

        TEXTO = escrever.text(xy=(50, 128), text=textwrap.fill(mensagem, 30), fill=(255, 255, 255), font=fonte)
        print(f'Canal :{client.guilds}')
        print(f'Mensagem: {mensagem}')
        randomphilo = random.choice(filosofo)
        img.paste(randomphilo, (0, 0), randomphilo)
        img.save('Philobot/philocit.png')

        file = discord.File('Philobot/philocit.png', filename='philocit.png')
        await ctx.channel.send(TEXTO, file=file)
        print("Comando #philobot enviado com sucesso!")

    except Exception as e:
        print(e)
        await ctx.send(f'Ops, algo deu errado!\nErro: {e}')


# ==========================================================

@client.command()  # feature - 1.4.0
async def philomaker(ctx, member: discord.Member, *, mensagens):
    # template : 1078 x 584
    # img size : 449 x 584
    # text location : 341, 68

    try:
        template = Image.open('templateNovo.png')

        # ======= CITAÇÃO PERSONALIZADA ============
        fonte = ImageFont.truetype("font/myriad.otf", 45)
        escrever = ImageDraw.Draw(template)
        escrever.text(xy=(50, 100), text=textwrap.fill(mensagens, 30), fill=(255, 255, 255), font=fonte)
        # =====================================
        # ======= NOME DO FILOSOFO ============
        fonte_2 = ImageFont.truetype("font/myriad.otf", 25)
        escrever_2 = ImageDraw.Draw(template)
        escrever_2.text(xy=(50, 516), text=f'- {member.display_name}', fill=(255, 255, 255), font=fonte_2)

        # =====================================
        # ======= FOTO DO FILOSOFO ============

        for img in ctx.message.attachments:
            await img.save('Philomaker/stored_img/filo_img.png')
        filo = Image.open("Philomaker/stored_img/filo_img.png")
        filo2 = filo.resize((449, 584))
        template.paste(filo2, (629, 0))  # try: img.filename or img
        template.save('Philomaker/philomaker.png')
        file = discord.File('Philomaker/philomaker.png', filename="philomaker.png")
        await ctx.channel.send(file=file)


    except Exception as e:
        print(e)
        await ctx.send(f'Ops, algo deu errado!\n Erro: {e} \n ===============')
        await ctx.send('Não se esqueça, precisa ser nessa ordem: \n #philomaker + @membro + mensagem')


# ================================================================
@client.event
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Argumento necessário faltando para esse comando.')
        print('Argumento necessário faltando para esse comando.')

    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Esse comando não existe. Digite #help para ver os que existem!')
        print('Esse comando não existe. Digite #help para ver os que existem!')

    if isinstance(error, commands.BadArgument):
        await ctx.send('O argumento passado não é válido.')
        print('O argumento passado não é válido.')


# ==================================================================
