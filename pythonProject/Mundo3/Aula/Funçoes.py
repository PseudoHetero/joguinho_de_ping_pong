def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1

valores = [1, 2, 8, 3, 5, 8]
dobra(valores)
print(valores)
