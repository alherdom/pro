from __future__ import annotations
from cards import Card, Deck, Hand
from helpers import combinations

class Dealer:
    def __init__(self, deck: Deck, players: list[Player]):
        self.deck = deck
        self.players = players
        
    def draw_random_cards(self):
        for player in self.players:
            player.hole_cards = [self.deck.draw_random_card() for _ in range(2)]
    
    def draw_community_cards(self):
        self.community_cards = [self.deck.draw_random_card() for _ in range(5)]
        for player in self.players:
            player.community_cards = self.community_cards
        
    def __repr__(self) -> str:
        return f'Deck:{self.deck}\nPlayers:{self.players}\n'
    
    def show_community_cards(self):
        return f'{self.community_cards}'

# - Datos:
#   - Mazo ✔
#   - Jugadores ✔ 
# - Responsabilidades:
#   - Dar cartas a los jugadores ✔
#   - Destapar cartas comunes ✔

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hole_cards = []
        self.community_cards = []
        self.hand = Hand
        self.cards_combinations = []
    
    @property
    def get_cards_combinations(self):
        player_cards = self.hole_cards + self.community_cards
        self.cards_combinations =  list(combinations(player_cards, n = 5))
        return self.cards_combinations
        
    def is_royal_flush(self):        
        suits = []
        values = []
        for combination in self.cards_combinations:
            for card in combination:
                values.append(card.cmp_value)
                suits.append(card.suit)
        if len(suits) == 1 and sum[values] >= 60:
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return f'\n 🤺 Player{self.name} \n 🔒 Hole Cards: {self.hole_cards} \n 🃏 Community Cards: {self.community_cards})'

# 1º Escalera Real: 5 cartas seguidas del mismo palo desde el 10 al As.
    # 5 cartas del mismo palo, y consecutivas desde el 10 al AS (14)
    # len(suits) == 1 vale, todas las cartas son del mismo palo porque es igual 1
    # ahora tocaria comporbar, si da 24 la suma de todos los values
    
    
# 2º Escalera color: 5 cartas consecutivas del mismo color.

# 3º Poker: 4 cartas iguales.

# 4º Full: 3 cartas iguales más otras 2 iguales. Es decir, un trio y una pareja.

# En caso de empate, gana el que tiene el trio más alto.

# 5º Color: 5 cartas del mismo palo.

# 6º Escalera: 5 cartas consecutivas que no son del mismo palo.

# 7º Trío: 3 cartas iguales.

# 8º Doble pareja: Dos parejas de cartas iguales.

# 9º Pareja: Una pareja de cartas iguales.

# 10º Carta más alta: Si en el transcurso de la partida ningún jugador consigue formar 
# alguna de las combinaciones presentadas más arriba, el ganador de la partida será el
# que tenga la carta más fuerte, siendo el As la mejor en estos casos. Es también la carta
# más fuerte la que desempata dos combinaciones idénticas.

# - Datos:
#   - Nombre ✔ 
#   - 2 cartas propias ✔
#   - 5 cartas comunes ✔
# - Responsabilidades:
#   - Encontrar su mejor combinación de cartas