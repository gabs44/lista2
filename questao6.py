class Veiculo:
  def __init__(self, nome, capacidade, distanciaPercorrida):
    self.nome = nome
    self.capacidade = capacidade
    self.distanciaPercorrida = distanciaPercorrida

  def tarifa(self):
    return self.capacidade * 100

class Onibus(Veiculo):
  def __init__(self, nome, distanciaPercorrida, capacidade=50):
    super().__init__(nome, capacidade, distanciaPercorrida)
    
  def tarifa(self):
    r = super().tarifa()
    return r + (0.1 * r)


b1 = Onibus("volvo", 12, 50)
print('a tarifa total do ônibus é:', b1.tarifa())


# Como não ficou claro no enunciado, defini o valor de capacidade para o ônibus como 50.