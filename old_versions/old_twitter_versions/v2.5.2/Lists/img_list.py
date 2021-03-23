"""
posting.py
Philosopher Bot
---------------
Created by Caio Madeira ('@sudomaidera)
Co-worker: Rodrigo Carmo @rodrigoblock

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from PIL import Image
from config import PATH_IMG
import os

path = PATH_IMG
# os.path.join(path, filename)

philosopher = [

    Image.open(os.path.join(path, 'adamsmith.png')),
    Image.open(os.path.join(path, 'alanturing.png')),
    Image.open(os.path.join(path, 'aristoteles.png')),
    Image.open(os.path.join(path, 'bakunin.png')),
    Image.open(os.path.join(path, 'castro.png')),
    Image.open(os.path.join(path, 'chaplin.png')),
    Image.open(os.path.join(path, 'che.png')),
    Image.open(os.path.join(path, 'curie.png')),
    Image.open(os.path.join(path, 'dalailama.png')),
    Image.open(os.path.join(path, 'descartes.png')),
    Image.open(os.path.join(path, 'FUKO.png')),
    Image.open(os.path.join(path, 'jesus.png')),
    Image.open(os.path.join(path, 'karnal.png')),
    Image.open(os.path.join(path, 'lenin.png')),
    Image.open(os.path.join(path, 'MANDELA.png')),
    Image.open(os.path.join(path, 'maquiavel.png')),
    Image.open(os.path.join(path, 'martin.png')),
    Image.open(os.path.join(path, 'marx.png')),
    Image.open(os.path.join(path, 'mussolini.png')),
    Image.open(os.path.join(path, 'neto.png')),
    Image.open(os.path.join(path, 'neymar.png')),
    Image.open(os.path.join(path, 'niet.png')),
    Image.open(os.path.join(path, 'pascal.png')),
    Image.open(os.path.join(path, 'platao.png')),
    Image.open(os.path.join(path, 'rousseau.png')),
    Image.open(os.path.join(path, 'stalin.png')),
    Image.open(os.path.join(path, 'winston.png')),
    Image.open(os.path.join(path, 'albert.png')),
    Image.open(os.path.join(path, 'anyrand.png')),
    Image.open(os.path.join(path, 'bauman.png')),
    Image.open(os.path.join(path, 'camus.png')),
    Image.open(os.path.join(path, 'clarice.png')),
    Image.open(os.path.join(path, 'dilma.png')),
    Image.open(os.path.join(path, 'fiodor.png')),
    Image.open(os.path.join(path, 'freud.png')),
    Image.open(os.path.join(path, 'hannah.png')),
    Image.open(os.path.join(path, 'hawk.png')),
    Image.open(os.path.join(path, 'jobs.png')),
    Image.open(os.path.join(path, 'kimjonun.png')),
    Image.open(os.path.join(path, 'mao.png')),
    Image.open(os.path.join(path, 'newton.png')),
    Image.open(os.path.join(path, 'olavo.png')),
    Image.open(os.path.join(path, 'schop.png')),
    Image.open(os.path.join(path, 'simone.png')),
    Image.open(os.path.join(path, 'socrates.png')),
    # -------------------------------
    Image.open(os.path.join(path, 'putin.png')),
    Image.open(os.path.join(path, 'aristoteles_2.png')),
    Image.open(os.path.join(path, 'ada.png')),
    Image.open(os.path.join(path, 'amoedo.png')),
    Image.open(os.path.join(path, 'bolsonaro.png')),
    Image.open(os.path.join(path, 'deus.png')),
    Image.open(os.path.join(path, 'juliocesar.png')),
    Image.open(os.path.join(path, 'kimjongil.png')),
    Image.open(os.path.join(path, 'malcomx.png')),
    Image.open(os.path.join(path, 'nicolau_czar.png')),
    Image.open(os.path.join(path, 'pele.png')),
    Image.open(os.path.join(path, 'platao_2.png')),
    Image.open(os.path.join(path, 'rosa.png')),
    # ------------------------------
    Image.open(os.path.join(path, 'alexandre.png')),
    Image.open(os.path.join(path, 'assange.png')),
    Image.open(os.path.join(path, 'clovis.png')),
    Image.open(os.path.join(path, 'copernico.png')),
    Image.open(os.path.join(path, 'dumont.png')),
    Image.open(os.path.join(path, 'durkheim.png')),
    Image.open(os.path.join(path, 'goulart.png')),
    Image.open(os.path.join(path, 'lacerda.png')),
    Image.open(os.path.join(path, 'machado.png')),
    Image.open(os.path.join(path, 'oscar.png')),
    Image.open(os.path.join(path, 'sinatra.png')),
    Image.open(os.path.join(path, 'suntzu.png')),
    Image.open(os.path.join(path, 'tiradentes.png')),
    Image.open(os.path.join(path, 'washington.png')),
    # ======= SECOND VERSION ============
    Image.open(os.path.join(path, 'washington.png')),
    Image.open(os.path.join(path, 'amoedo2.png')),
    Image.open(os.path.join(path, 'bolsonaro2.png')),
    Image.open(os.path.join(path, 'castro2.png')),
    Image.open(os.path.join(path, 'che2.png')),
    Image.open(os.path.join(path, 'curie2.png')),
    Image.open(os.path.join(path, 'jesus2.png')),
    Image.open(os.path.join(path, 'marx2.png')),
    Image.open(os.path.join(path, 'stalin2.png')),
    # ======= SPECIALS ==================
    Image.open(os.path.join(path, 'monark.png')),
    Image.open(os.path.join(path, 'shelby.png')),
    Image.open(os.path.join(path, 'veiohavan.png')),
    Image.open(os.path.join(path, 'renatorusso.png')),
    Image.open(os.path.join(path, 'michael_scott.png')),
    Image.open(os.path.join(path, 'lucifer.png')),
    Image.open(os.path.join(path, 'dwight.png')),
    Image.open(os.path.join(path, 'autordesconhecido.png')),
    Image.open(os.path.join(path, 'atila.png')),
    Image.open(os.path.join(path, 'ednaldo.png')),
    Image.open(os.path.join(path, 'feijoada.png')),
    Image.open(os.path.join(path, 'homelander.png')),
    Image.open(os.path.join(path, 'lenin_negro.png')),
    Image.open(os.path.join(path, 'mcpoze.png'))

]

# print(philosopher)