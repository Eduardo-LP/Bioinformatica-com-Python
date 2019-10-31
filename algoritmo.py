entrada = open("humano.txt").read()
saida = open("nova_humano.html", "w")

cont = {}

for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0

entrada = entrada.replace("\n", "")
entrada = entrada.replace("N", "")

for k in range(len(entrada)-1):
	cont[entrada[k]+entrada[k+1]] += 1

i = 1

for k in cont:
	trans = cont[k]/max(cont.values())
	saida.write("<div style='width:100px; height: 100px; border: 1px solid black; float: left; background-color: rgba(0,0,0,"+ str(trans) +"); color: white;'>"+ k +": " + str(cont[k]) +"</div>")

	if i%4 == 0:
		saida.write("<div style='clear: both;'></div>")

	i += 1

saida.close()