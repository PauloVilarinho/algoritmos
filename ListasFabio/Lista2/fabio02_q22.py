"""
	Questão: Lista 2 22
	Descrição: calcula o tempo de uma partida
"""

def main():
	#entrada
	hora_inicial = int(input("digite as horas em que começaram o jogo: "))
	min_inicial = int(input("digite os minutos em que começaram o jogo: "))
	hora_final = int(input("digite as horas em que acabaram o jogo: "))
	min_final = int(input("digite os minutos em que acabaram o jogo: "))
	#processamento
	tempo_inicial = hora_inicial*60 + min_inicial
	tempo_final = hora_final*60 + min_final
	if tempo_inicial < tempo_final :
		tempo = tempo_final - tempo_inicial
	else :
		tempo = 1440 - tempo_inicial + tempo_final

	horas = tempo//60
	minutos = tempo%60
	#saida
	print("o jogo durou %d horas e %d minutos" %(horas,minutos))

if __name__ == '__main__':
	main()
