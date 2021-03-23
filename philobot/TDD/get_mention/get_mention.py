from Credentials.Test.main_credentials_test import api_test

api = api_test

usuario = api.get_status('1355235977615319042')
mention = usuario.entities['user_mentions'] # tupla

listar = []
for m in mention:
    listar.append(m['name'])

name = listar[0]
print(name)