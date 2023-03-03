from datetime import date
datageracao = date.today()
ano = datageracao.year
mes = datageracao.month

# Criando um arquivo para escrita e leitura
nomearquivo = 'arquivoCNISRPPS'+str(mes)+'/'+str(ano)+'.xml'
output = open(nomearquivo, "w")
