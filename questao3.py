class Veiculo:
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    self.nome = nome
    self.maxVelocidade = maxVelocidade
    self.distanciaPercorrida = distanciaPercorrida


class Onibus(Veiculo):
  def __init__(self, nome, maxVelocidade, distanciaPercorrida):
    super().__init__(nome, maxVelocidade, distanciaPercorrida)

  
busao = Onibus('Volvo', 180, 12)
print(f'Nome do veículo: {busao.nome} Velocidade: {busao.maxVelocidade} Km: {busao.distanciaPercorrida}')