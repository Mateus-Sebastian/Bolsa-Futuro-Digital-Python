class Lampada:
    def __init__(self):
        self.ligada = False
    
    def ligar(self):
        self.ligada = True
        print(f"A lâmpada está ligada. {self.ligada}")

    def desligar(self):
        self.ligada = False
        print(f"A lâmpada está desligada. {self.ligada}")

lampada1 = Lampada()
lampada1.ligar()
lampada1.desligar()