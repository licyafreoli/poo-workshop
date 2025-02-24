class ContaBancaria:
  def __init__(self,numero:int, cliente:str):
    self.numero = numero
    self.cliente = cliente
    self.saldo = 0
  
  def exibir_dados(self):
    print("dados da conta")
    print(f"numero: {self.numero}")
    print(f"cliente: {self.cliente}")
    print(f"saldo: {self.saldo}")

  def sacar(self, valor:float):
    if self.saldo>= valor:
      self.saldo -= valor
      print(f"saque realizado com sucesso! saldo: R${self.saldo}")
    else:
      print("saldo insuficiente")
    
  def depositar(self,valor:float):
      self.saldo += valor
      print(f"deposito realizado com sucesso! saldo: R${self.saldo}")


conta1 = ContaBancaria("001", "lara")
conta1.exibir_dados()
print("--------------")
conta1.depositar(100)
conta1.sacar(50)