import unittest

class Card:
    """Represents a single playing card in a Solitaire game."""
    
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    @property
    def color(self) -> str:
        """Determines the color of the card based on its suit."""
        if self.suit in ["Hearts", "Diamonds"]:
            return "Red"
        return "Black"

class TestCard(unittest.TestCase):
    """xUnit tests for the Solitaire Card class."""

    def test_card_initialization(self):
        """Test that a card is created with the correct rank and suit."""
        card = Card("Ace", "Spades")
        self.assertEqual(card.rank, "Ace")
        self.assertEqual(card.suit, "Spades")

    def test_card_color_logic(self):
        """Test that the color property correctly identifies Red and Black suits."""
        card1 = Card("10", "Hearts")
        card2 = Card("King", "Clubs")
        
        self.assertEqual(card1.color, "Red")
        self.assertEqual(card2.color, "Black")

if __name__ == '__main__':
    unittest.main()
