class Veiculo:
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    self.nome = nome
    self.maxVelocidade = maxVelocidade
    self.distanciaPercorrida = distanciaPercorrida
    self.cor = 'Branco' 

class Onibus(Veiculo):
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    super().__init__(nome, maxVelocidade, distanciaPercorrida)
    

class Carro(Veiculo):
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    super().__init__(nome, maxVelocidade, distanciaPercorrida)
    

v1 = Veiculo('volvo', 180, 12,)
print(f'cor: {v1.cor}, nome do veículo: {v1.nome}, velocidade: {v1.maxVelocidade}, quilometragem: {v1.distanciaPercorrida} ')
v2 = Carro('audi Q5', 240, 18)
print(f'cor: {v2.cor}, nome do veículo: {v2.nome}, velocidade: {v2.maxVelocidade}, quilometragem: {v2.distanciaPercorrida} ')