class Veiculo:
  def __init__(self, cor, tipo, ano_de_fabricacao, modelo, placa, valor_do_veiculo, valor_do_ipva = False):
    self._cor = cor
    self._tipo = tipo
    self._ano_de_fabricacao = ano_de_fabricacao
    self._modelo = modelo
    self._placa = placa
    self._valor_do_veiculo = valor_do_veiculo
    self._valor_do_ipva = valor_do_ipva

  #get
  @property
  def cor(self):
    return self._cor

  @property
  def tipo(self):
    return self._tipo

  @property
  def ano_de_fabricacao(self):
    return self._ano_de_fabricacao

  @property
  def modelo(self):
    return self._modelo

  @property
  def placa(self):
    return self._placa

  @property
  def valor_do_veiculo(self):
    return self._valor_do_veiculo
  
  @property
  def valor_do_ipva(self):
    return self._valor_do_ipva

  #set
  @cor.setter
  def cor(self, cor):
    self._cor = cor
  
  @valor_do_veiculo.setter
  def valor_do_veiculo(self, valor):
    self._valor_do_veiculo = valor


  def caucularIPVA(self, classificacao):
    ano = int(2021 - self._ano_de_fabricacao)
    if ano < 15:
        if classificacao == 1:
          ipva = int((self._valor_do_veiculo / 100) * 2)
          self._valor_do_ipva = self._valor_do_veiculo + ipva
        elif classificacao == 2:
          ipva = int((self._valor_do_veiculo / 100) * 1)
          self._valor_do_ipva = self._valor_do_veiculo + ipva
        else:
          print(f"informe apenas 1 para automovel ou 2 pra utilitario na classificção") 
    else:
      self._valor_do_ipva = self._valor_do_veiculo 
 
    return self._valor_do_ipva

  def imprimir(self):
    print(f"IPVA: {self._valor_do_ipva}")