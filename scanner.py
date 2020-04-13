import requests

print("#################################################")
print("#---------- by Thiago da Silva Moyses ----------#")
print("#              Plagia Não Comedia!              #")
print("# codigos Comuns:                               #")
print("#                                               #")
print("# codigo: 200 || Conexao Feita                  #")
print("# Codigo: 404 || Pagina Não Encontrada          #")
print("# Codigo: 503 || Serviço indisponível           #")
print("#                                               #")
print("# Outros Codigo: http://encurtador.com.br/kvRXY #")
print("#################################################")

site = input('\nURL do site: \n')

while True:
	try:
		lista = input('caminho da lista: \n')
		paginas = open(lista, 'r')
		break
	except:
		print("Caminho incorreto!")

for ende in paginas:
	try:
		ende = ende.rstrip()
		teste = site+ende
		resultado = requests.get(teste)
		print(teste, "||", resultado.status_code)
	except:
		print("Site nao encontrado!")
		break