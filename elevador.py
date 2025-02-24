class Elevador:
  def __init__(self,qnt_andares: int, capacidade: int):
    self.qnt_andares = qnt_andares
    self.capacidade = capacidade
    self.qnt_pessoas = 0
    self.andar_atual = 0
    