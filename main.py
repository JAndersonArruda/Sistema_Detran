from automovel import Automovel as A
from veiculodecarga import VeiculoDeCarga as VC

a1 = A("vermelha", "automovel", 2000, "D20", "NBH164", 20000, 6, 4)
vc1 = VC("amarelo", "utilitario", 2010, "caminhão", "HVN204", 18000, 8, 30)

print(a1._cor, a1._tipo, a1._ano_de_fabricacao, a1._modelo, a1._placa,
      a1._valor_do_veiculo, a1._capacidade_de_passageiros, a1._numero_de_portas)
a1.caucularIPVA(1)
a1.imprimir()

print(vc1._cor, vc1._tipo, vc1._ano_de_fabricacao, vc1._modelo, vc1._placa,
      vc1._valor_do_veiculo, vc1._numero_de_eixos, vc1._capacidade_de_carga)
vc1.caucularIPVA(2)
vc1.imprimir()
