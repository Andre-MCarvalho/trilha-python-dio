# oconjunto é uma lista de itens unicos, não aceita itens duplicados
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

#pode ser declarado com chaves
linguagens = {'python', 'java', 'python', 'c++','javascript','c++','c#'}
print (linguagens)
