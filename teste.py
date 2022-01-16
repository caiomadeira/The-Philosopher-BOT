emoji_folder = r'C:\Users\rodri\Documents\The-Philosopher-BOT-2.5.3\TWITTER\v2.5.2\Emojis'
import os

files = os.listdir(emoji_folder)

# print(u'\U0001f603')
for e in files:
    new_e = e.replace('.png', '')
    print("\" + ffU000{new_e})
