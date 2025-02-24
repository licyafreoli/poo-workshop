class Elevador:
    def __init__(self, qnt_andares: int, capacidade: int):
        self.qnt_andares = qnt_andares
        self.capacidade = capacidade
        self.qnt_pessoas = 0
        self.andar_atual = 0

      
    def exibir_dados(self):
        print("dados do elevador")
        print(f"Quantidade de andares: {self.qnt_andares}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Quantidade de pessoas: {self.qnt_pessoas}")
        print(f"Andar atual: {self.andar_atual}")

    def subir(self):
        if self.andar_atual == self.qnt_andares:
            print("voce ja esta no ultimo andar")
        else:
            self.andar_atual +=1
            print(f"Subindo...Andar atual: {self.andar_atual}")

    def descer(self):
        if self.andar_atual == 0:
            print("voce ja esta no terreo")
        else:
            self.andar_atual -= 1
            print(f"descendo...andar atual:{self.andar_atual}")
    
    def entrar(self, numero_pessoas):
        if self.qnt_pessoas + numero_pessoas > self.capacidade:
            print("o elevador nao suporta essa quantidade.")
        else:
            self.qnt_pessoas += numero_pessoas
            print(f"entrando pessoas...quantidade atual: {self.qnt_pessoas}")

elevador = Elevador(15,10)
elevador.entrar(10)
    
