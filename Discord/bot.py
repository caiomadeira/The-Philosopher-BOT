"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
import dotenv
import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
import os
from Lists.img_list import PHILOSOPHERS_LIST
from Templates.New_Img_Manipulation.reference import TEMPLATES_PATH

# loads .env
dotenv.load_dotenv(dotenv.find_dotenv())

client = commands.Bot(command_prefix="#", case_insensitive=False)
status = ["#help", "#news"]
client.remove_command('help')

mensagens = entrou = 0
message = join = 0


# ==========================================
@client.event
async def on_ready():
    text_channel_list = []
    for server in client.guilds:
        for channel in server.channels:
            if channel.type == 'Tests':
                text_channel_list.append(channel)

    embed_1 = discord.Embed(colour=discord.Colour.dark_green())
    embed_1.set_footer(text=f'PHILOSOPHER BOT ESTÁ ONLINE!🟢 \n \nDigite #news para saber o que há de novo!')

    print("-----------------------------")
    print(f'\n Se o {client.user.name} pensa, logo existe.\n')
    print("-----------------------------")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(status[1])))

    try:
        await channel.send(embed=embed_1)

    except AttributeError:
        print("Não foi possivel mandar mensagem de boas vindas... Pulando!")

    # await channel.send(embed=embed_1)


""""""""""""""""""""""

       COMANDOS

"""""""""""""""""""""""


# =============== INFO ================
@client.command(aliases=['novidades', 'noticias'])
async def news(ctx):
    embed = discord.Embed(color=discord.Colour.dark_green(), timestamp=ctx.message.created_at)

    embed.set_author(name=f'NEWS/NOVIDADES - {os.getenv("version")}', icon_url=ctx.author.avatar_url)
    embed.add_field(name='Otimização do Código!', value="Corrido erros no manipulação das imagens!", inline=False)
    embed.add_field(name='Remoção do site!', value="Site indisponível!", inline=False)
    embed.add_field(name='ENGLISH SUPPORT! 🇺🇸🇺🇸', value="Agora o bot possui comandos em ingles!", inline=False)

    await ctx.send(embed=embed)


@client.command(aliases=['sobre'])
async def about(mensagem):
    global mensagens
    mensagens += 1

    LOGO = 'https://cdn.discordapp.com/attachments/750556593199906956/769867377797890048/logo_new_emoji_newfundo.png'

    embed_1 = discord.Embed(

        title='Sobre Philosopher BOT:',
        description='Criado por Caio Madeira (@sudomadeira)',
        colour=discord.Colour.dark_green()

    )

    embed_1.set_footer(text='Instagram: @sudomadeira \n '
                            'Twitter: @sudomadeira \n '
                            'Github: github.com/CaioMadeira \n '
                            'SITE: www.philosopherbot.com.br \n '
                            'TWITTER: @bot_philosopher')
    embed_1.set_image(url=LOGO)
    embed_1.set_thumbnail(url=LOGO)
    embed_1.add_field(name='SOBRE:', value="Manipulação de texto atribuindo a um filosofo aleatório", inline=True)

    await mensagem.channel.send(embed=embed_1)


# ============== VERSAO ==================================
@client.command(aliases=['versao'])
async def version(mensagem):
    global mensagens
    mensagens += 1

    embed_2 = discord.Embed(
        description=f"Versão:{os.getenv('version')}",
        colour=discord.Colour.dark_green()

    )
    await mensagem.channel.send(embed=embed_2)


# ====================== HELP =============================


@client.command(aliases=['ajuda'])
async def help(ctx):
    embed = discord.Embed(color=discord.Colour.dark_green(), timestamp=ctx.message.created_at)

    embed.set_author(name='Ajuda', icon_url=ctx.author.avatar_url)

    embed.add_field(name='#sobre', value="Fala um pouco sobre o BOT e seus criadores.", inline=False)
    embed.add_field(name='#versao', value="Mostra a versão atual do BOT no Discord.", inline=False)
    embed.add_field(name='#philobot + [mensagem]',
                    value="Gera uma citação com a mensagem enviada com algum filosofo aleatório", inline=False)
    embed.add_field(name='#philomaker + [membro] + [mensagem] + imagem - (BETA) ',
                    value="Gera uma citação com a mensagem enviada com a foto enviada e o "
                          "membro mencionado", inline=False)
    embed.add_field(name='#limpar + [numero]', value="Apaga um determinado número de mensagens.", inline=False)
    embed.add_field(name='#ajuda_philomaker', value="Informa mais sobre o comando philomaker", inline=False)

    await ctx.send(embed=embed)


# ====================== HELP PHILOMAKER =============================


@client.command(aliases=['ajuda_philomaker', 'ajudaphilomaker', 'philomaker_ajuda', 'philomakerajuda',
                         'helpphilomaker', 'philomakerhelp', 'philomaker_help'])
async def help_philomaker(ctx):
    embed = discord.Embed(color=discord.Colour.dark_green(), timestamp=ctx.message.created_at)

    embed.set_author(name='Help - Philomaker', icon_url=ctx.author.avatar_url)
    embed.set_footer(text='Apenas siga a ordem do print')
    embed.add_field(name='#philomaker + [membro] + [mensagem] + [imagem]',
                    value="Gera uma citação com a mensagem enviada com a foto enviada e o "
                          "membro mencionado", inline=False)
    embed.set_image(url='https://media.discordapp.net/attachments/712754644987936858/761974600987967500/exemple.PNG')
    await ctx.send(embed=embed)


# ============== APAGAR MENSAGENS =========================
@client.command(aliases=['limpar'])
async def clear(ctx, numero):
    try:
        numero = int(numero)

        if numero:
            await ctx.channel.purge(limit=numero)
            print(f"{numero} mensagens limpas")

            embed_2 = discord.Embed(
                description=f'{numero} mensagens limpas',
                colour=discord.Colour.dark_green()

            )
            await ctx.channel.send(embed=embed_2)

    except discord.ext.commands.errors.CommandInvokeError as e:
        print(e)


# ==========================================================

@client.command()  # função principal
async def philobot(ctx, *, mensagem):
    try:
        img = Image.open(f'{TEMPLATES_PATH}/layer_1.png')
        font = ImageFont.truetype(os.getenv('myriad_font'), 50)
        drawing = ImageDraw.Draw(img)

        print(f'Canal :{client.activity}\n')
        print(f'Mensagem: {mensagem}')
        print(f'BOT: {client.user}')
        choice_philosopher = random.choice(PHILOSOPHERS_LIST)
        remove_path_of_filename = os.path.basename(choice_philosopher)
        print(f"Imagem do filósofo escolhida: {remove_path_of_filename}")

        remove_extension_of_filename = remove_path_of_filename.replace('.png', '')
        if '(2)' in remove_extension_of_filename:
            print("Removendo lixo no nome da imagem do filosofo...")
            remove_number_in_name = remove_extension_of_filename.replace('(2)', '')
            finish_name_of_philosopher = f'- {remove_number_in_name}'
            print(f'Nome do filósofo tratado: {finish_name_of_philosopher}')
        else:
            finish_name_of_philosopher = f'- {remove_extension_of_filename}'
            print("Nenhum lixo no nome da imagem encontrado. Prosseguindo normalmente...")
            print(f'Nome do filósofo tratado: {finish_name_of_philosopher}')

        philosopher_str_to_obj = Image.open(choice_philosopher)
        img_2 = philosopher_str_to_obj.resize((449, 584))
        img.paste(img_2, (629, 0))
        smooth_template = Image.open(f'{TEMPLATES_PATH}/layer_3.png')
        img.paste(smooth_template, (0, 0), smooth_template)
        TEXTO = drawing.text(xy=(60, 128), text=textwrap.fill(mensagem, 20), fill=(255, 255, 255), font=font)
        font = ImageFont.truetype("Font/times.ttf", 30)
        drawing.text(xy=(43, 512),
                     text=textwrap.fill(str(finish_name_of_philosopher), 25),
                     fill=(255, 255, 255),
                     font=font)
        img.save('philobot_discord.png')

        file = discord.File('philobot_discord.png', filename='philobot_discord.png')
        await ctx.channel.send(TEXTO, file=file)
        print("Comando #philobot enviado com sucesso!")

    except Exception as e:
        print(e)
        await ctx.send(f'Ops, algo deu errado!\nErro: {e}')


# ==========================================================

@client.command()
async def philomaker(ctx, member: discord.Member, *, mensagens):
    # template : 1078 x 584
    # img size : 449 x 584
    # text location : 341, 68

    try:
        template = Image.open(os.getenv('old_template_path'))

        # ======= CITAÇÃO PERSONALIZADA ============
        fonte = ImageFont.truetype(os.getenv('myriad_font'), 50)
        escrever = ImageDraw.Draw(template)
        escrever.text(xy=(50, 100), text=textwrap.fill(mensagens, 30), fill=(255, 255, 255), font=fonte)
        # =====================================
        # ======= NOME DO FILOSOFO ============
        fonte_2 = ImageFont.truetype(os.getenv('myriad_font'), 25)
        escrever_2 = ImageDraw.Draw(template)
        escrever_2.text(xy=(50, 516), text=f'- {member.display_name}', fill=(255, 255, 255), font=fonte_2)

        # =====================================
        # ======= FOTO DO FILOSOFO ============

        for img in ctx.message.attachments:
            await img.save('filo_img.png')
        filo = Image.open("filo_img.png")
        filo2 = filo.resize((449, 584))
        template.paste(filo2, (629, 0))  # try: img.filename or img
        template.save('philomaker_discord.png')
        file = discord.File('philomaker_discord.png', filename="philomaker.png")
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

    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send('Esse comando não existe. Digite #help para ver os que existem!')
        print('Esse comando não existe. Digite #help para ver os que existem!')

    if isinstance(error, commands.BadArgument):
        await ctx.send('O argumento passado não é válido.')
        print('O argumento passado não é válido.')

    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Erro - O comando está errado ou o argumento passado está errado')
        print('Erro - O comando está errado ou o argumento passado está errado')
