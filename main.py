import sys
import automatos

def main():
	"""
	Verifica se o arquivo foi especificado no comando de execução do
	programa. Senão, a opção de criar um autômato será escolhida por
	padrão.
	Caso o arquivo não seja encontrado, uma mensagem de erro será mostrada.

	Para a criação de um autômato será requisitado o alfabeto, a quantidade
	de estados e o estado inicial.
	Então será definido se o autômato é um AFD ou AFN. E, para cada um, seus
	respectivos métodos.
	"""
	try:
		automatos.le_arquivo('afn.txt')

	except FileNotFoundError:
		print('Arquivo não encontrado')

if __name__ == '__main__':
    main()
