from veiculo import Veiculo as V

class VeiculoDeCarga(V):
  def __init__(self, cor, tipo, ano_de_fabricacao, modelo, placa, valor_do_veiculo, numero_de_eixos, capacidade_de_carga):
    V.__init__(self, cor, tipo, ano_de_fabricacao, modelo, placa, valor_do_veiculo, valor_do_ipva = False)
    self._numero_de_eixos = numero_de_eixos
    self._capacidade_de_carga = capacidade_de_carga

  #get
  @property
  def numero_de_eixos(self):
    return self._numero_de_eixos

  @property
  def capacidade_de_carga(self):
    return self._capacidade_de_carga

  #set
  @numero_de_eixos.setter
  def numero_de_eixos(self, numero):
    self._numero_de_eixos

  @capacidade_de_carga.setter
  def capacidade_de_carga(self, capacidade):
    self._capacidade_de_carga

  def caucularIPVA(self, classificacao):
    V.caucularIPVA(self, classificacao)

  def cor(self, cor):
    V.cor(self, cor)

  def valor_do_veiculo(self, valor):
    V.valor_do_veiculo(self, valor)