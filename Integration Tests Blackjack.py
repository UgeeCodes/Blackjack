from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

# Test cases for user winning
#1 Both hands are under 21 and user hand is greater than dealer hand
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_greater_dealer(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21. 
        Dealer receives cards with a hand greater than 21.
        The user wins by the dealer busting.
        '''
        output = run_test([5, 7, 8], ['y', 'n'], [8, 8, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 7\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew an 8\n" \
                   "Dealer has 16.\n" \
                   "Drew a 3\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

#2 User hand is less than 21 while dealer busts
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_deal_busts(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21. 
        Dealer receives cards with a hand greater than 21.
        The user wins by the dealer busting.
        '''
        output = run_test([2, 4, 8], ['y', 'n'], [3, 9, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 4\n" \
                   "You have 6. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 14. Hit (y/n)? n\n" \
                   "Final hand: 14.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

#3  User blackjacks and dealer busts
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bj_dealer_busts(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21. 
        Dealer receives cards with a hand greater than 21.
        The user wins by the dealer busting.
        '''
        output = run_test([3, 2, 9, 7], ['y', '0', 'y'], [3, 1, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 2\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 14. Hit (y/n)? 0\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an Ace\n" \
                   "Dealer has 14.\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

#4 User blackjacks and dealer does not blackjack or bust
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bj_dealer(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21. 
        Dealer receives cards with a hand greater than 21.
        The user wins by the dealer busting.
        '''
        output = run_test([3, 2, 9, 7], ['y', '0', 'y'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 2\n" \
                   "You have 5. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 14. Hit (y/n)? 0\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

# Test cases for user Pushing.
#1 When user hand and dealer hand are equal to 21.
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_equal_dealer_21(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand equal to 21.
        The user pushes by having an equal hand as the dealer.

        This does not count as one of your tests.
        '''
        output = run_test([13, 5, 3, 3], ['y', 'hit', 'yes', 'y'], [1, 12], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 18. Hit (y/n)? hit\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 18. Hit (y/n)? yes\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a Queen\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

#2 User hand and dealer hand are equal to 17
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_equal_dealer_17(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand equal to 17.
        The user pushes by having an equal hand as the dealer.

        This does not count as one of your tests.
        '''
        output = run_test([13, 5, 2], ['y', 'n'], [11, 7], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 2\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 7\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

# Dealer winning tests
#1 Dealer blackjacks and user does not blackjack or bust
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_deal_bj(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand greater than 21. 
        Dealer receives cards with a hand equal to 21.
        The dealer wins by the user busting.
        '''
        output = run_test([1, 1], [], [7, 8, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew an Ace\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew an 8\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

#2 Both bust bust dealer hand is less than user hand
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_dealer_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21.
        The dealer wins by the user busting.
        '''
        output = run_test([6, 12, 4, 1], ['y', 'y'], [8, 8, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a Queen\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 20. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 31.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew an 8\n" \
                   "Dealer has 16.\n" \
                   "Drew a 10\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

#3 dealer hand == user hand and they are greater than 21 
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_equal_dealer_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that are equal in hand and greater than 21.
        The dealer wins by the user busting.
        '''
        output = run_test([11, 9, 4], ['y', 'y'], [5, 8, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 9\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew an 8\n" \
                   "Dealer has 13.\n" \
                   "Drew a 10\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

#4 dealer blackjacks, user does not blackjack or bust
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_deal_bj(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand less than 21.
        Dealer receives cards with a hand value equal to 21.
        The dealer wins by getting a blackjack.
        '''
        output = run_test([8, 2, 3, 4], ['y', 'x', 'y', 'n'], [3, 4, 6, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 2\n" \
                   "You have 10. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 13. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 13. Hit (y/n)? y\n" \
                   "Drew a 4\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 4\n" \
                   "Dealer has 7.\n" \
                   "Drew a 6\n" \
                   "Dealer has 13.\n" \
                   "Drew an 8\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

#5 Dealer doesn't blackjack or bust but user busts      
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_deal(self, input_mock, randint_mock):
        '''
        User receive cards that end up with a hand greater than 21.
        Dealer receives cards with a hand value less than 21.
        The dealer wins by getting a blackjack.
        '''
        output = run_test([8, 6, 3, 7], ['y', 'y', 'n'], [3, 4, 3, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew a 6\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 17. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 4\n" \
                   "Dealer has 7.\n" \
                   "Drew a 3\n" \
                   "Dealer has 10.\n" \
                   "Drew a 9\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
