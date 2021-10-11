import itertools

chars = "#PhiloMaker"
results = list(map(''.join, itertools.product(*zip(chars.upper(), chars.lower()))))

for r in results:
    print(r)


with open('words.txt', 'w+') as f:
    for r in results:
        f.write(f"'{r}': '',\n")
