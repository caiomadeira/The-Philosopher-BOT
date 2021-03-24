import sqlite3

img_db = sqlite3.connect('../images/img.db')
cursor = img_db.cursor()


print("IMAGE DATABASE - PHILOBOT DISCORD")
try:
        name = input('Digite o nome da imagem junto com a extensão: ')

        with open(f'{name}', 'rb') as f:
            data = f.read()

        cursor.execute(''' 
        INSERT INTO philo_1 (name, data) VALUES (?,?)''', (name, data))

        '''
        # criando tabelas
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS philo_1 (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
         name TEXT, data BLOP) """)
        
        '''
        print('well done!')
except Exception as e:
    print(f"Não foi possível achar a imagem: {e}")



img_db.commit()
cursor.close()
img_db.close()