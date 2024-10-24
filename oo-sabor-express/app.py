from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
# restaurante_japones = Restaurante('Japa', 'Japonesa')

# restaurante_mexicano.alternar_estado()

# restaurante_praca.receber_avaliacao('Italo', 5)
# restaurante_praca.receber_avaliacao('Ana', 3)
# restaurante_praca.receber_avaliacao('Stenio', 2)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

def main():
    pass

if __name__ == '__main__':
    main()