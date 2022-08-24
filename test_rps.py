from rps import evaluate_hands, print_result

# Testovací sada gest a jejich vzájemných vztahů
# Pro každého hráče zvlášť vypíše kombinace:
# první pro kámen, pak pro papír a následně pro nůžky
def main():
    print("Testing suite: Kámen, nůžky, papír\n")
    
    print("Hráč 1:")
    # Kámen
    result = evaluate_hands("rock", "rock")
    print(f"Kámen vs. kámen:")
    print_result(result)
    
    result = evaluate_hands("rock", "scissors")
    print(f"Kámen vs. nůžky:")
    print_result(result)

    result = evaluate_hands("rock", "paper")
    print("Kámen vs. papír:")
    print_result(result)
    
    result = evaluate_hands("rock", "spock")
    print("Kámen vs. Spock:")
    print_result(result)

    # Nůžky
    result = evaluate_hands("paper", "rock")
    print(f"Papír vs. kámen:")
    print_result(result)
    
    result = evaluate_hands("paper", "scissors")
    print(f"Papír vs. nůžky:")
    print_result(result)
    
    result = evaluate_hands("paper", "paper")
    print(f"Papír vs. papír:")
    print_result(result)
    
    result = evaluate_hands("paper", "spock")
    print(f"Papír vs. Spock:")
    print_result(result)

    # Papír
    result = evaluate_hands("scissors", "rock")
    print(f"Nůžky vs. kámen:")
    print_result(result)

    result = evaluate_hands("scissors", "scissors")
    print(f"Nůžky vs. nůžky:")
    print_result(result)

    result = evaluate_hands("scissors", "paper")
    print(f"Nůžky vs. papír:")
    print_result(result)

    result = evaluate_hands("scissors", "spock")
    print(f"Nůžky vs. Spock:")
    print_result(result)


    print("Hráč 2:")
    # Kámen
    result = evaluate_hands("rock", "rock")
    print(f"Kámen vs. kámen:")
    print_result(result)

    result = evaluate_hands("scissors", "rock")
    print(f"Nůžky vs. kámen:")
    print_result(result)

    result = evaluate_hands("paper", "rock")
    print(f"Papír vs. kámen:")
    print_result(result)

    result = evaluate_hands("spock", "rock")
    print(f"Spock vs. kámen:")
    print_result(result)

    # Nůžky
    result = evaluate_hands("rock", "paper")
    print(f"Kámen vs. papír:")
    print_result(result)

    result = evaluate_hands("scissors", "paper")
    print(f"Nůžky vs. papír:")
    print_result(result)

    result = evaluate_hands("paper", "paper")
    print(f"Papír vs. papír:")
    print_result(result)

    result = evaluate_hands("spock", "paper")
    print(f"Spock vs. papír:")
    print_result(result)

    # Papír
    result = evaluate_hands("rock", "scissors")
    print(f"Kámen vs. nůžky:")
    print_result(result)

    result = evaluate_hands("scissors", "scissors")
    print(f"Nůžky vs. nůžky:")
    print_result(result)

    result = evaluate_hands("paper", "scissors")
    print(f"Papír vs. nůžky:")
    print_result(result)

    result = evaluate_hands("spock", "scissors")
    print(f"Spock vs. nůžky:")
    print_result(result)
    

if __name__ == "__main__":
    main()