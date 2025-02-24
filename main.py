class Carros:
  def __init__(self, marca: str, modelo: str, cor:str):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.ligado = False
    self.velocidade_atual = 0

  def ligar(self):
    self.ligado = True
    print("o veiculo esta ligado")
  
  def desligar(self):
    self.desligado = False
    print("o veiculo esta desligado")

  def acelerar(self):
    if self.ligado:
      self.velocidade_atual += 25
      print(f"acelerando...velocidade: {self.velocidade_atual}km")
    else:
      print("o veiculo esta desligado")
      
  def exibir_dados(self):
    print("dados do veiculo")
    print(f"marca: {self.marca}")
    print(f"modelo: {self.modelo}")
    print(f"cor: {self.cor}")

car1 = Carros("fiat", "uno com escada", "prata")
#print(f"marca:{car1.marca}")
#print(f"cor:{car1.cor}")
car1.exibir_dados()
#car1.cor = input('informe a nova cor: ')
#print(f"nova cor: {car1.cor}")
car1.ligar()
car1.acelerar()
