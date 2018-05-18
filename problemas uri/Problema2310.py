quantity = int(input())
total_saque = 0
total_bloqueio = 0
total_ataque = 0
total_certo_saque = 0
total_certo_bloqueio = 0
total_certo_ataque = 0
for i in range (quantity) :
	nome = input()
	entrada1 = input().split()
	entrada2 = input().split()
	saque_feito,bloqueio_feito,ataque_feito = [int(i) for i in entrada1]
	saque_certo,bloqueio_certo,ataque_certo = [int(i) for i in entrada2]
	total_ataque += ataque_feito
	total_bloqueio += bloqueio_feito
	total_saque += saque_feito
	total_certo_ataque += ataque_certo
	total_certo_bloqueio += bloqueio_certo
	total_certo_saque += saque_certo

media_saque = (total_certo_saque/total_saque)*100
media_ataque = (total_certo_ataque/total_ataque)*100
media_bloqueio = (total_certo_bloqueio/total_bloqueio)*100

print("Pontos de Saque: {:.2f} %.".format(media_saque))
print("Pontos de Bloqueio: {:.2f} %.".format(media_bloqueio))
print("Pontos de Ataque: {:.2f} %.".format(media_ataque))