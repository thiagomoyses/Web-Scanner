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
lista = input('caminho da lista: \n')
paginas = open(lista, 'r')

for ende in paginas:
	ende = ende.rstrip()
	teste = site+ende
	resultado = requests.get(teste)
	print(teste, "||", resultado.status_code)