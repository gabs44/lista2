class Veiculo:
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    self.nome = nome
    self.maxVelocidade = maxVelocidade
    self.distanciaPercorrida = distanciaPercorrida

  def capacidade(self, capacidade):
    return f" a capacidade de um {self.nome} é de {capacidade} passageiros" 


class Onibus(Veiculo):
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    super().__init__(nome, maxVelocidade, distanciaPercorrida)

  def capacidade(self, capacidade=50):
    return f" a capacidade de um {self.nome} é de {capacidade} passageiros"


onibus = Onibus('onibus', 150, 50) 
print(onibus.capacidade())
