import datetime

class Alimento:
    codigo_atual = 1

    def __init__(self, nome, quantidade):
        self.codigo = Alimento.codigo_atual
        self.nome = nome
        self.quantidade = quantidade
        Alimento.codigo_atual += 1

class Pessoa:
    def __init__(self, nome, cpf, rua, numero_casa, qtd_pessoas, qtd_trabalhadores):
        self.nome = nome
        self.cpf = cpf
        self.rua = rua
        self.numero_casa = numero_casa
        self.qtd_pessoas = qtd_pessoas
        self.qtd_trabalhadores = qtd_trabalhadores
        self.historico_doacoes = []

estoque_alimentos = []
pessoas_cadastradas = []

def cadastrar_alimento(nome, quantidade):
    alimento = Alimento(nome, quantidade)
    estoque_alimentos.append(alimento)
    print(f"Alimento '{nome}' cadastrado em estoque. Código: {alimento.codigo}")

def consultar_alimentos_estoque():
    for alimento in estoque_alimentos:
        print(f"Código: {alimento.codigo}, Nome: {alimento.nome}, Quantidade: {alimento.quantidade}")

def cadastrar_pessoa(nome, cpf, rua, numero_casa, qtd_pessoas, qtd_trabalhadores):
    if any(pessoa.cpf == cpf for pessoa in pessoas_cadastradas):
        print("CPF já cadastrado.")
    else:
        pessoa = Pessoa(nome, cpf, rua, numero_casa, qtd_pessoas, qtd_trabalhadores)
        pessoas_cadastradas.append(pessoa)
        print(f"Pessoa '{nome}' cadastrada com sucesso.")

def remover_pessoa(cpf):
    for pessoa in pessoas_cadastradas:
        if pessoa.cpf == cpf:
            pessoas_cadastradas.remove(pessoa)
            print("Pessoa removida com sucesso.")
            return
    print("Pessoa não encontrada.")

def consultar_todos_cadastros():
    for pessoa in pessoas_cadastradas:
        print(f"Nome: {pessoa.nome}, CPF: {pessoa.cpf}, Rua: {pessoa.rua}, Número: {pessoa.numero_casa}")
        print(f"Quantidade de pessoas na família: {pessoa.qtd_pessoas}, Trabalhadores na família: {pessoa.qtd_trabalhadores}")
        print("")

def registrar_doacao(cpf, codigo_alimento, quantidade):
    for pessoa in pessoas_cadastradas:
        if pessoa.cpf == cpf:
            for alimento in estoque_alimentos:
                if alimento.codigo == codigo_alimento:
                    if alimento.quantidade >= quantidade:
                        doacao = {
                            "data": datetime.date.today(),
                            "alimento": alimento.nome,
                            "quantidade": quantidade
                        }
                        pessoa.historico_doacoes.append(doacao)
                        alimento.quantidade -= quantidade
                        print("Doação registrada com sucesso.")
                        return
                    else:
                        print("Quantidade insuficiente em estoque.")
                        return
            print("Alimento não encontrado.")
            return
    print("CPF não cadastrado.")

def consultar_historico_doacoes(cpf):
    for pessoa in pessoas_cadastradas:
        if pessoa.cpf == cpf:
            if pessoa.historico_doacoes:
                print(f"Histórico de doações para {pessoa.nome} (CPF: {pessoa.cpf}):")
                for doacao in pessoa.historico_doacoes:
                    data = doacao["data"].strftime("%Y-%m-d")
                    print(f"Data: {data}, Alimento: {doacao['alimento']}, Quantidade: {doacao['quantidade']}")
            else:
                print(f"Nenhuma doação encontrada para {pessoa.nome} (CPF: {pessoa.cpf}).")
            return
    print("CPF não cadastrado.")

def main():
    while True:
        print("* Painel de Controle *")
        print("* 1. Cadastrar alimento em estoque *")
        print("* 2. Consultar alimentos em estoque *")
        print("* 3. Cadastrar pessoa *")
        print("* 4. Remover pessoa *")
        print("* 5. Registrar doação *")
        print("* 6. Consultar histórico de doações *")
        print("* 7. Consultar todos os cadastros *")
        print("* 8. Sair *")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Nome do alimento: ")
            quantidade = int(input("Quantidade: "))
            cadastrar_alimento(nome, quantidade)
        elif opcao == "2":
            consultar_alimentos_estoque()
        elif opcao == "3":
            nome = input("Nome completo: ")
            cpf = input("CPF: ")
            rua = input("Nome da rua: ")
            numero_casa = input("Número da casa: ")
            qtd_pessoas = int(input("Quantidade de pessoas que moram junto: "))
            qtd_trabalhadores = int(input("Quantas pessoas trabalham na família: "))
            cadastrar_pessoa(nome, cpf, rua, numero_casa, qtd_pessoas, qtd_trabalhadores)
        elif opcao == "4":
            cpf = input("CPF da pessoa a ser removida: ")
            remover_pessoa(cpf)
        elif opcao == "5":
            cpf = input("CPF da pessoa que está doando: ")
            codigo_alimento = int(input("Código do alimento doado: "))
            quantidade = int(input("Quantidade doada: "))
            registrar_doacao(cpf, codigo_alimento, quantidade)
        elif opcao == "6":
            cpf = input("CPF da pessoa para consultar o histórico de doações: ")
            consultar_historico_doacoes(cpf)
        elif opcao == "7":
            consultar_todos_cadastros()
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
