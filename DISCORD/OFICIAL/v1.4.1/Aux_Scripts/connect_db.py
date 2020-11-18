import sqlite3
import random

img_db = sqlite3.connect('img.db')
c = img_db.cursor()
c.execute('SELECT name FROM philo_1')
pegando = c.fetchall()
#for i in pegando:
    #print(i)

print("Feito!")
img_db.commit()
img_db.close()



