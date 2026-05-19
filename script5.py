dglobal = {}
nid=0
def criar_id(numero):
    numero+=1
    return 'ID'+str(numero)

def cadastra_centro(idcen):
    listares = []
    cred = 0
    nome = input("Digite o nome da unidade ")
    dici = {idcen: {"nome": nome, "lista res": listares, 'créditos': cred}}
    return dici

def gerar_relatorio(dicig):
    for emp,info in dicig.items():
        soma=0
        for chave,valor in info.items():
            print(f"  {chave}: {valor}")
        for muito in range(len(info['lista res'])):
            soma=sum(info['lista res'])
            print(f'total de residuos:{soma}')

while True:
    print("escolha uma função:\n"
          "1- Cadastrar centro de Reciclagem\n"
          "2- Registrar processamento de Resíduos\n"
          "3- Gerar Relatório Ambiental\n"
          "0- Sair do Sistema")
    esc = int(input("Digite o numero da função desejada: "))
    match esc:
        case 1:
            idcen=criar_id(nid)
            nova = cadastra_centro(idcen)
            dglobal.update(nova)
            print(f'a sua id é: {idcen}')

        case 2:
            id_centro = input("digite o ID do centro:").strip().upper()
            if id_centro not in dglobal:
                print("centro não encontrado!")
            else:
                peso = float(input("Digite o peso dos resíduos processados (em kg): "))
                dglobal[id_centro]["lista res"].append(peso)
                creditos_gerados = peso / 100
                dglobal[id_centro]['créditos'] += creditos_gerados
                print("Processamento registrado com sucesso!")

        case 3:
            gerar_relatorio(dglobal)
        case 0:
            print("saindo do Sistema")
            break
        case _:
            print("nenhuma opção valida")