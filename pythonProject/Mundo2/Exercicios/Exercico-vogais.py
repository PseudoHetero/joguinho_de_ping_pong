palavra = ('banheiro', 'bagagem', 'arara', 'aranha', 'fantasma',
            'odio', 'choro', 'menina')
for letra in palavra:
    print(f'A palavra {letra} possui {letra.count("a")} A, {letra.count("e")} E,'
          f'{letra.count("i")} I, {letra.count("o")} O, {letra.count("U")} U.')