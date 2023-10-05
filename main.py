##manipulando texto
nome = "samuel"

itemString = nome[3]
intervalo = nome[0:2]
pulando = nome[1:5:2]
ignorandoInicio = nome[5]
ateOFinal = nome[3:]
inicioComIntervalo = nome[2::3]

tamanho = len(nome)
quantValorRepete =  nome.count("a")
quantValorRepeteComIntervalo =  nome.count("a", 0,5)

ondeComeca = nome.find('muel')
valorInvalido = nome.find('abobora')
existe = 'sam' in nome

##transformando
nome.replace('sam', 'Sam')
maiusculas = nome.upper()
minusculas = nome.lower()
capitalizado = nome.capitalize()
tituloPadraoYouTube = nome.title()
removendoEspacos = nome.strip() ##mesmo que trim
removerEspacoDireita = nome.rstrip()
removerEspacoEsquerda = nome.lstrip()
dividirString = nome.split()
dividirCaminho = "curso/curso1".split("/")
colocarTraco = "-".join(dividirCaminho)

##exercicio - TAMANHO DO NOME SEM ESPACOS
tamanhoNomeSemEspacos = len("Samuel Santos".replace(" ", ""))
print(tamanhoNomeSemEspacos)

##exercicio - Quantas letras tem o primeiro nome
quantLetrasPrimeiroNome = len("Samuel Santos".split(" ")[0])
print(quantLetrasPrimeiroNome)

##exercicio - cidade comeca com o nome 'santos'
cidade = input("Digite o nome da cidade: ")
ehNomeProcurado = cidade.split(" ")[0] in "santos"
if ehNomeProcurado:
    print("Cidade digitada comeca com o nome: santos")
else:
    print("Cidade digitada não comeca com o nome santos")

##exercicio - verifica se a pessoa tem silva no nome

nomePessoa = input("Digite o nome da pessoa: ")

contemSilva = False

for e in nomePessoa.split():
    print(e)
    if e is 'silva':
        contemSilva = True

if contemSilva:
    print("O nome fornecido contem a palavra silva")
else:
    print('O nome fornecido não contem a palavra silva')