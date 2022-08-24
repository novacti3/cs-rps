# Zadání vývojového požadavku -- Kámen, nůžky, papír
# Česká spořitelna -- Junior Developer v Pythonu
# Jan Šaler
# srpen 2022


# Vyhodnotí výstup zadaných gest
from enum import IntEnum


# Enum možných gest, které se ve hře mohou objevit
class PossibleHands(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    SPOCK = 4


# Enum všech možných výsledků kola
class PossibleResults(IntEnum):
    DRAW = 0
    PLAYER_ONE_WINS = 1
    PLAYER_TWO_WINS = 2


# Vyhodnotí vstupní string a vrátí gesto podle jeho prvního písmena
# Pokud se jedná o nemožné gesto, vrátí -1
def _parse_hand(hand: str) -> PossibleHands:
    match(hand[0]):
        case 'r':
            return PossibleHands.ROCK
        case 'p':
            return PossibleHands.PAPER
        case 's':
            if hand[1] == 'c':
                return PossibleHands.SCISSORS
            else:
                return PossibleHands.SPOCK
    # Ošetření špatného vstupu
    return -1


# Vyhodnotí výsledek momentálního kola podle zadaných vstupních stringů
# Výstup:
# -1 - nemožný vstup
# 0 - remíza 
# 1 - hráč 1 vyhrál
# 2 - hráč 2 vyhrál
def evaluate_hands(player_one: str, player_two: str) -> PossibleResults:
    hand_one: PossibleHands = _parse_hand(player_one)
    hand_two: PossibleHands = _parse_hand(player_two)

    if hand_one <= 0 or hand_two <= 0:
        return -1
    
    # Spock vítězí nad vším :)
    if hand_one == PossibleHands.SPOCK:
        return 1
    elif hand_two == PossibleHands.SPOCK:
        return 2

    # Algoritmus: odečteme od sebe hodnoty gest prvního hráče a druhého hráče
    # Vyhodnotíme výsledek kola podle rozdílu jejich gest
    # 
    # Vysvětlení: Jelikož jsou v enum PossibleHands gesta seřazena tak,
    # že položka s nižším indexem je poražena položkou nad ní,
    # kterou zase porazí gesto další, můžeme od hodnoty gesta 
    # prvního hráče odečíst hodnotu gesta hráče dva.
    # Jelikož se bude vždy odečítat od potenciálně nejnižší hodnoty
    # ze hry, výsledek bude vždy buď záporné číslo, nula nebo kladné číslo.
    # <0 => hráč dva vyhrál
    # 0 => remíza
    # >0 => hráč jedna vyhrál
 
    # Edge case: Jelikož považujeme záporná čísla za výhru druhého hráče,
    # odečtení kamene (hodnota 1 = nejmenší) a nůžek (hodnota 3 = nejvyšší) 
    # má vždy za výsledek záporné číslo, tedy dle algoritmu má vyhrát hráč dva, 
    # což je ale špatně
    # To samé platí pro případ, kdy je gesto prvního hráče nůžky a druhého kámen,
    # byť tentokrát je výsledek kladný, byť by měl být záporný (=> výhra druhého hráče)
    result = hand_one - hand_two
    if (hand_one == PossibleHands.ROCK and hand_two == PossibleHands.SCISSORS) or \
        hand_one == PossibleHands.SCISSORS and hand_two == PossibleHands.ROCK:
        result *= -1
    
    if result > 0:
        return PossibleResults.PLAYER_ONE_WINS
    elif result < 0:
        return PossibleResults.PLAYER_TWO_WINS
    else:
        return PossibleResults.DRAW


# Pomocná funkce pro výpis výsledku kola
def print_result(result: PossibleResults) -> None:
    match(result):
        case PossibleResults.DRAW:
            print("Remíza\n")
        case PossibleResults.PLAYER_ONE_WINS:
            print("Hráč 1 vyhrál\n")
        case PossibleResults.PLAYER_TWO_WINS:
            print("Hráč 2 vyhrál\n")


def main():
    print("Kámen, nůžky, papír")
    print("------------------------------")
    
    play_game = 1
    while play_game == 1:
        print("Zadejte vstup")
        print("Formát: (hráč 1) (hráč 2)")
        print("Možné příkazy: rock, paper, scissors, quit")

        hands = input("Příkaz: ")
        tokens = hands.split(' ')

        # Můžeme počítat s přesně 2 příkazy od uživatele, 
        # jelikož případný nedostatek je ošetřen hned po tomto kousku kódu
        if tokens[0] == "quit" or (len(tokens) == 2 and tokens[1] == "quit"): 
            play_game = 0
            continue

        # Příkazy musí být jen a pouze 2
        if len(tokens) < 2:
            print("Musíte zadat dva příkazy ve formátu: (hráč 1) (hráč 2)\n")
            continue
        if len(tokens) > 2:
            print("Musíte zadat pouze dva příkazy, ve formátu: (hráč 1) (hráč 2)\n")
            continue

        # Ošetření proti tomu, že by byl jeden z příkazů mezera či jakkoliv prázdný
        if not tokens[0] or not tokens[1]:
            print("Byl zadán špatný příkaz\n")
            continue

        # Vyhodnoť kolo
        result = evaluate_hands(tokens[0], tokens[1])
        
        # Vypiš výsledek
        if result == -1:
            print("Byl zadán špatný příkaz\n")
            continue
        else:
            print_result(result)


if __name__ == "__main__":
    main()