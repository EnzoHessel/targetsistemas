def contarA(text):
    quantidadeA = text.lower().count('a')
    return quantidadeA

text = input("Digite uma palavra para contagem de letra 'a': ")

quantidade = contarA(text)

print(f"A letra ocorre {quantidade} vezes")

