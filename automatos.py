class Estado:
	
	def __init__(self, nome):
		self.nome = nome
		self.transicao = {}
		self.final = False
		self.inicial = False

def le_arquivo(arquivo):
	
	with open(arquivo, 'r') as f:
		tipo = 'afn'
		alfabeto = f.readline().replace('\n','') + ',e'
		alfabeto = alfabeto.replace(',','').split()
		qtd_estados = int(len([x.strip() for x in f.readline().split(',')]))
		lista_estados = criar_estados(alfabeto[0], qtd_estados)

        # definindo estado inicial
		linha = f.readline().split()
		for e in lista_estados:
			if e.nome == linha[0]:
				e.inicial = True

        # definindo estado final
		linha = f.readline().replace('\n','')
		linha = linha.split(',')
		for e in lista_estados:
			for j in range(len(linha)):
				if e.nome == linha[j]:
					e.final = True

        # recebendo todas as transições
        # transicao = f.readline().split()    #[0] = estadoorigem; [1] = estadestino; [2:] = simbolo (Que esta sendo processado)
		for transicao in f:
			lista = []
			t = [x.strip() for x in transicao.split(',')]
			for e in lista_estados:
				if e.nome == t[0]:
					lista.append(t[1])
					if t[2] == 'epsilon':
						e.transicao['e'] = lista.copy()
					else:		
						e.transicao[t[2]] = lista.copy()	
			
			lista.clear()
	f.close()

	sair = True
	while sair:
		palavra = input('Palavra a ser processada: ')
		print('A palavra', palavra, processa_palavra(lista_estados, palavra), 'pelo automato')
		i = input('Sair? (S/N) ')
		sair = (False) if i.upper() == 'S' else (True)

def criar_estados(alfabeto, qtd_estados):
    """
    Criação de um dicionário auxiliar com todos os símbolos do alfabeto.
    Inicialmente, todos os estados levam à um estado "vazio",
    independente de qual símbolo tenha sido processado.
    """
    estados = []
    for i in range(0, qtd_estados):
        nome = 'q' + str(i)
        estados.append(Estado(nome))

    return estados

def processa_palavra(lista_estados, palavra):
	"""
	Procura o estado inicial na lista de estados e o adiciona à lista
	de estados ativos.
	Para cada símbolo da palavra a ser processada, enquanto existirem
	estados ativos, verificar se o símbolo leva à algum estado. Se levar,
	adicioná-lo à fila de processamento, que, posteriormente, será incorporada
	como estados ativos.
	Se algum estado da lista de estados ativos final possuir o atributo ".final"
	igual à "True", então a palavra é aceita pelo autômato.

	"""
	# Procurando o estado inicial
	for e in lista_estados:
		if e.inicial == True:
			e_atual = e

	e_ativos = []
	e_ativos.append(e_atual)
	fila_proc = []
	conjunto = []
	index = ' '

	for simb in palavra:
		while len(e_ativos) > 0:
			e_atual = e_ativos.pop()
			if e_atual.transicao.get(simb) is not None:
				for nome_estado in e_atual.transicao.get(simb):
					for e in lista_estados:
						if e.nome == nome_estado:
							fila_proc.append(e)
							index += e_atual.nome + '--' + simb + '-->' + e.nome + ' \n '

		e_ativos = fila_proc.copy()
		fila_proc.clear()	
	
	for estado in e_ativos:
		if estado.final == True:
			print(index)
			return 'é aceita'
	return 'não é aceita'

