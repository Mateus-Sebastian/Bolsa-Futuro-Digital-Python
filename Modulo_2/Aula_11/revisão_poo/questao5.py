class ContaBancaria:
    banco = 'Banco Central'
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def mostrar_informacoes(self):
        print(f"Banco: {self.banco}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}\n")

conta1 = ContaBancaria("Alice", 1500.0)
conta1.mostrar_informacoes()
conta2 = ContaBancaria("Bob", 2500.5)
conta2.mostrar_informacoes()