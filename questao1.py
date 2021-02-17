class Veiculo:
  def __init__(self, maxVelocidade, distanciaPercorrida ):
    self.maxVelocidade = maxVelocidade
    self.distanciaPercorrida = distanciaPercorrida

c1 = Veiculo(150, 5)
print(c1.maxVelocidade)
print(c1.distanciaPercorrida)