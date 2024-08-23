class Conta:
    def __init__(self, titularConta, saldo):
        self.titularConta = titularConta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para o saque.")
        else:
            self.saldo -= valor
    
    def extrato(self):
        return self.saldo

# Criação da conta com saldo inicial
conta = Conta('Luiz Felipe', 500)

while True:
    print("\n1 - Depósito\n2 - Saque\n3 - Extrato\n0 - Sair")
    try:
        opcao = int(input("Selecione sua opção: "))
        
        if opcao == 1:
            try:
                deposito = float(input("Digite o valor do depósito: R$ "))
                conta.depositar(deposito)
                print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
            except ValueError:
                print("Valor inválido para depósito. Tente novamente.")
                
        elif opcao == 2:
            try:
                saque = float(input("Digite o valor do saque: R$ "))
                conta.sacar(saque)
                if saque <= conta.saldo:
                    print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
            except ValueError:
                print("Valor inválido para saque. Tente novamente.")
                
        elif opcao == 3:
            print(f"O saldo total da conta é: R$ {conta.extrato():.2f}")
        
        elif opcao == 0:
            print("Obrigado por usar nossos serviços!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")
            
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
