import sys
import automatos

def main():
	"""
	
	Para a criação de um autômato será requisitado o alfabeto, 
	os estados e o estado inicial. Seguindo o formato abaixo:

	alfabeto=a,b,c,d   		Lista de símbolos do alfabeto aceito pelo automato
	estados=q0,q1,q2   		Lista de estados no automato
	inicial=q0 			    Indica qual é o estado inicial
	finais=q1,q2 			Especifica os estados finais do automato
	transicoes
	q0,q1,a  				Representa uma transição de q0 para q1 com o símbolo "a"
	q1,q2,epsilon  			Transição de cadeia vazia de q1 para q2
	
	"""
	try:
		automatos.le_arquivo('afn.txt')

	except FileNotFoundError:
		print('Arquivo não encontrado')

if __name__ == '__main__':
    main()
