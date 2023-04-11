from veiculo import Veiculo as V


class Automovel(V):
    def __init__(self, cor, tipo, ano_de_fabricacao, modelo, placa, valor_do_veiculo, capacidade_de_passageiros, numero_de_portas):

        V.__init__(self, cor, tipo, ano_de_fabricacao, modelo,
                   placa, valor_do_veiculo, valor_do_ipva=False)
        self._capacidade_de_passageiros = capacidade_de_passageiros
        self._numero_de_portas = numero_de_portas

    # get
    @property
    def capacidade_de_passageiros(self):
        return self._capacidade_de_passageiros

    @property
    def numero_de_portas(self):
        return self._numero_de_portas

    # set
    @capacidade_de_passageiros.setter
    def capacidade_de_passageiros(self, numero):
        self._capacidade_de_passageiros = numero

    @numero_de_portas.setter
    def numero_de_portas(self, numero):
        self._numero_de_portas = numero

    def caucularIPVA(self, classificacao):
        V.caucularIPVA(self, classificacao)

    def cor(self, cor):
        V.cor(self, cor)

    def valor_do_veiculo(self, valor):
        V.valor_do_veiculo(self, valor)
