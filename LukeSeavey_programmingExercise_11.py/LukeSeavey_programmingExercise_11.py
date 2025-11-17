import random

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
        
         "J", "Q", "K", "A"]

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]


def create_deck():
    
    deck = []
    
    for suit in SUITS:
        
        for rank in RANKS:
            
            deck.append(f"{rank} of {suit}")
    
    return deck


def deal_hand(deck, num_cards=5):
    
    hand = []
    
    for _ in range(num_cards):
        
        card = deck.pop()  # remove from the deck so no duplicates
        
        hand.append(card)
    
    return hand


def print_hand(hand, label="Hand"):
    
    print(f"\n{label}:")
    
    for i, card in enumerate(hand, start=1):
        
        print(f"  {i}: {card}")
    
    print()


def get_indices_to_replace():
    
    while True:
        
        user_input = input(
            
            "Enter the card numbers to replace (e.g. 1 3 5 or 2,4), "
            
            "or press Enter to keep all cards: "
        
        ).strip()

        # Empty input no change
        
        if user_input == "":
            
            return []

        user_input = user_input.replace(",", " ")
        
        parts = user_input.split()

        indices = []
        
        valid = True

        for part in parts:
            
            if not part.isdigit():
                
                print("Please enter only numbers separated by spaces or commas.")
                
                valid = False
                
                break

            num = int(part)
            
            if num < 1 or num > 5:
                
                print("Card numbers must be between 1 and 5.")
                
                valid = False
                
                break

            idx = num - 1
            
            if idx not in indices:
                
                indices.append(idx)

        if valid:
            
            return indices

def main():
    
    # Create and shuffle deck
    
    deck = create_deck()
    
    random.shuffle(deck)

    # Deal initial hand
    
    hand = deal_hand(deck, num_cards=5)
    
    print_hand(hand, label="Initial Hand")

    # Ask user which cards to replace
    
    indices_to_replace = get_indices_to_replace()

    # Replace selected cards
    
    for idx in indices_to_replace:
        
        if deck:  
            
            hand[idx] = deck.pop()

    # Show final hand after draw
    
    print_hand(hand, label="Final Hand After Draw")

if __name__ == "__main__":
    
    main()