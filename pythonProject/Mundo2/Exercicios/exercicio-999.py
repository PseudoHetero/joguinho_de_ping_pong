n = c = s = 0

while True:
    n = int(input("Digite um valor:"))
    if n == 999:
        break
    c += n
    s += 1

print(f'a soma dos valores são {c}, e você digitou um total de {s} números')