from enum import Enum
import random

#Ace = 1, Jack = 11, Queen = 12, King = 13, 10 -> T

hearts = []
spades = []
diamonds = []
clubs = []
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
full_deck = []
remaining_deck = []
hidden_cards = []

deck_loc = 0

class card():
	def __init__(self, value, suit, color):
		self.value = value
		self.suit = suit
		self.color = color

def make_full_deck():
	full_deck.append(card(1, 'H', 'R'))
	full_deck.append(card(2, 'H', 'R'))
	full_deck.append(card(3, 'H', 'R'))
	full_deck.append(card(4, 'H', 'R'))
	full_deck.append(card(5, 'H', 'R'))
	full_deck.append(card(6, 'H', 'R'))
	full_deck.append(card(7, 'H', 'R'))
	full_deck.append(card(8, 'H', 'R'))
	full_deck.append(card(9, 'H', 'R'))
	full_deck.append(card(10, 'H', 'R'))
	full_deck.append(card(11, 'H', 'R'))
	full_deck.append(card(12, 'H', 'R'))
	full_deck.append(card(13, 'H', 'R'))

	full_deck.append(card(1, 'D', 'R'))
	full_deck.append(card(2, 'D', 'R'))
	full_deck.append(card(3, 'D', 'R'))
	full_deck.append(card(4, 'D', 'R'))
	full_deck.append(card(5, 'D', 'R'))
	full_deck.append(card(6, 'D', 'R'))
	full_deck.append(card(7, 'D', 'R'))
	full_deck.append(card(8, 'D', 'R'))
	full_deck.append(card(9, 'D', 'R'))
	full_deck.append(card(10, 'D', 'R'))
	full_deck.append(card(11, 'D', 'R'))
	full_deck.append(card(12, 'D', 'R'))
	full_deck.append(card(13, 'D', 'R'))

	full_deck.append(card(1, 'C', 'B'))
	full_deck.append(card(2, 'C', 'B'))
	full_deck.append(card(3, 'C', 'B'))
	full_deck.append(card(4, 'C', 'B'))
	full_deck.append(card(5, 'C', 'B'))
	full_deck.append(card(6, 'C', 'B'))
	full_deck.append(card(7, 'C', 'B'))
	full_deck.append(card(8, 'C', 'B'))
	full_deck.append(card(9, 'C', 'B'))
	full_deck.append(card(10, 'C', 'B'))
	full_deck.append(card(11, 'C', 'B'))
	full_deck.append(card(12, 'C', 'B'))
	full_deck.append(card(13, 'C', 'B'))

	full_deck.append(card(1, 'S', 'B'))
	full_deck.append(card(2, 'S', 'B'))
	full_deck.append(card(3, 'S', 'B'))
	full_deck.append(card(4, 'S', 'B'))
	full_deck.append(card(5, 'S', 'B'))
	full_deck.append(card(6, 'S', 'B'))
	full_deck.append(card(7, 'S', 'B'))
	full_deck.append(card(8, 'S', 'B'))
	full_deck.append(card(9, 'S', 'B'))
	full_deck.append(card(10, 'S', 'B'))
	full_deck.append(card(11, 'S', 'B'))
	full_deck.append(card(12, 'S', 'B'))
	full_deck.append(card(13, 'S', 'B'))

	random.shuffle(full_deck)

def make_board():
	c1.append(full_deck[0])

	c2.append(full_deck[1])
	c2.append(full_deck[2])

	c3.append(full_deck[3])
	c3.append(full_deck[4])
	c3.append(full_deck[5])

	c4.append(full_deck[6])
	c4.append(full_deck[7])
	c4.append(full_deck[8])
	c4.append(full_deck[9])

	c5.append(full_deck[10])
	c5.append(full_deck[11])
	c5.append(full_deck[12])
	c5.append(full_deck[13])
	c5.append(full_deck[14])

	c6.append(full_deck[15])
	c6.append(full_deck[16])
	c6.append(full_deck[17])
	c6.append(full_deck[18])
	c6.append(full_deck[19])
	c6.append(full_deck[20])

	c7.append(full_deck[21])
	c7.append(full_deck[22])
	c7.append(full_deck[23])
	c7.append(full_deck[24])
	c7.append(full_deck[25])
	c7.append(full_deck[26])
	c7.append(full_deck[27])

	hidden_cards.append(full_deck[1])
	hidden_cards.append(full_deck[3])
	hidden_cards.append(full_deck[4])
	hidden_cards.append(full_deck[6])
	hidden_cards.append(full_deck[7])
	hidden_cards.append(full_deck[8])
	hidden_cards.append(full_deck[10])
	hidden_cards.append(full_deck[11])
	hidden_cards.append(full_deck[12])
	hidden_cards.append(full_deck[13])
	hidden_cards.append(full_deck[15])
	hidden_cards.append(full_deck[16])
	hidden_cards.append(full_deck[17])
	hidden_cards.append(full_deck[18])
	hidden_cards.append(full_deck[19])
	hidden_cards.append(full_deck[21])
	hidden_cards.append(full_deck[22])
	hidden_cards.append(full_deck[23])
	hidden_cards.append(full_deck[24])
	hidden_cards.append(full_deck[25])
	hidden_cards.append(full_deck[26])
	

	for x in range(28, 52, 1):
		remaining_deck.append(full_deck[x])
	
def print_card(card):
	if card.value == 1:
		print('A', end='')
	elif card.value == 10:
		print('T', end='')
	elif card.value == 11:
		print('J', end='')
	elif card.value == 12:
		print('Q', end='')
	elif card.value == 13:
		print('K', end='')
	else:
		print(card.value, end='')

	print(card.suit, end='  ')

def print_ace_piles():
	if len(hearts) == 0:
		print("HH", end='  ')
	else:
		print_card(hearts[len(hearts) - 1])

	if len(spades) == 0:
		print("SS", end='  ')
	else:
		print_card(spades[len(spades) - 1])

	if len(diamonds) == 0:
		print("DD", end='  ')
	else:
		print_card(diamonds[len(diamonds) - 1])

	if len(clubs) == 0:
		print("CC", end='  ')
	else:
		print_card(clubs[len(clubs) - 1])

def print_board():
	global deck_loc
	print("**", end=' ')
	if(len(remaining_deck) == 0):
		print("pile empty", end='')
	else:
		if(deck_loc >= len(remaining_deck)):
			print("end of pile, starting from beginning...")
			deck_loc = 0
		print_card(remaining_deck[deck_loc])
	print("     ", end='')
	print_ace_piles()
	print("\n")
	print("1   2   3   4   5   6   7")

	done = 0
	counter = 0
	while done != 7:
		done = 0
		if len(c1) >= counter+1:
			if c1[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c1[counter])
		else:
			print("  ", end='  ')
			done += 1

		if len(c2) >= counter+1:
			if c2[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c2[counter])
		else:
			print("  ", end='  ')
			done += 1
		
		if len(c3) >= counter+1:
			if c3[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c3[counter])
		else:
			print("  ", end='  ')
			done += 1
		
		if len(c4) >= counter+1:
			if c4[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c4[counter])
		else:
			print("  ", end='  ')
			done += 1
		
		if len(c5) >= counter+1:
			if c5[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c5[counter])
		else:
			print("  ", end='  ')
			done += 1
		
		if len(c6) >= counter+1:
			if c6[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c6[counter])
		else:
			print("  ", end='  ')
			done += 1
		
		if len(c7) >= counter+1:
			if c7[counter] in hidden_cards:
				print("**", end='  ')
			else:
				print_card(c7[counter])
		else:
			print("  ", end='  ')
			done += 1
		
		print()
		counter+=1

def flip_pile():
	global deck_loc
	deck_loc+=1
	if deck_loc >= len(remaining_deck):
		print("end of pile, starting from beginning...")
		deck_loc = 0

def check_valid(move_from, move_to):
	if ((move_from.value + 1) == move_to.value) and move_from.color != move_to.color:
		return True
	return False

def column_to_column_multiple(move):
	arr = {}

	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7

	m0 = 'a' + move[0]
	m1 = 'a' + move[1]

	pile_from = arr[m0]
	pile_to = arr[m1]

	if len(move) == 3:
		num_cards = int(move[2])
	else:
		num_cards = 10 + int(move[3])

	print(num_cards)

	if(len(pile_from) < num_cards):
		print("not enough cards in that pile, try again")
		return

	card_from = pile_from[len(arr[m0])-num_cards]

	#moving king to empty pile
	if(len(pile_to) == 0):
		if(card_from.value != 13):
			print("cannot move card here, try again")
			return
		else:
			for i in range(0, num_cards, 1):
				if pile_from[len(arr[m0])-1-i] in hidden_cards:
					print("can't move those cards, try again")
					return

			count = len(arr[m0]) - num_cards
			while num_cards > 0:
				pile_to.append(pile_from[count])
				pile_from.remove(pile_from[count])
				num_cards -= 1

			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])
			return

	else:
		card_to = pile_to[len(arr[m1])-1]
		if(check_valid(card_from, card_to)):
		#if(True):
			for i in range(0, num_cards, 1):
				if pile_from[len(arr[m0])-1-i] in hidden_cards:
					print("can't move those cards, try again")
					return

			count = len(arr[m0]) - num_cards
			while num_cards > 0:
				pile_to.append(pile_from[count])
				pile_from.remove(pile_from[count])
				num_cards -= 1

			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])
			return
		else:
			print("move not valid, try again")
			return

	return

def column_to_column(move):
	arr = {}

	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7

	m0 = 'a' + move[0]
	m1 = 'a' + move[1]

	pile_from = arr[m0]
	pile_to = arr[m1]

	if(len(pile_from) == 0):
		print("no cards in that pile, try again")
		return

	card_from = pile_from[len(arr[m0])-1]

	#moving king to empty pile
	if(len(pile_to) == 0):
		if(card_from.value != 13):
			print("cannot move card here, try again")
			return
		else:
			pile_to.append(card_from)
			pile_from.remove(card_from)
			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])
			return

	card_to = pile_to[len(arr[m1])-1]

	if(check_valid(card_from, card_to)):
	#if(True):
		pile_to.append(card_from)
		pile_from.remove(card_from)
		if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
			hidden_cards.remove(pile_from[len(pile_from) - 1])
		return
	else:
		print("move not valid, try again")
		return

	return

def column_to_ace(move):
	arr = {}

	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7

	m0 = 'a' + move[0]

	pile_from = arr[m0]

	if(len(pile_from) == 0):
		print("no cards in that pile, try again")
		return

	card_from = pile_from[len(arr[m0])-1]

	aces = {}

	aces['H'] = hearts
	aces['S'] = spades
	aces['D'] = diamonds
	aces['C'] = clubs

	a0 = move[1].upper()

	pile_to = aces[a0]

	if a0 != card_from.suit:
		print("wrong suit, try again")
		return
	else:
		if len(pile_to) == 0:
			if card_from.value == 1:
				pile_to.append(card_from)
				pile_from.remove(card_from)
				if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
					hidden_cards.remove(pile_from[len(pile_from) - 1])
				return

			else:
				print("need ace first, try again")
				return

		elif pile_to[len(pile_to) - 1].value == card_from.value - 1:
			pile_to.append(card_from)
			pile_from.remove(card_from)
			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])
			return

		else:
			print("1: cannot move to ace, try again")
			return

	return

def pile_to_column(move):
	global deck_loc
	arr = {}

	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7

	pile_from = remaining_deck
	if len(remaining_deck) == 0:
		print("no cards left in pile, try again")
		return

	card_from = remaining_deck[deck_loc]
	a0 = 'a' + move[1]
	pile_to = arr[a0]

	if len(pile_to) == 0:
		if(card_from.value != 13):
			print("cannot move card here, try again")
			return
		else:
			pile_to.append(card_from)
			pile_from.remove(card_from)
			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])
	else:
		card_to = pile_to[len(pile_to) - 1]
		if(check_valid(card_from, card_to)):
		#if(True):
			pile_to.append(card_from)
			pile_from.remove(card_from)
			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])
		else:
			print("move not valid, try again")
			return

	if deck_loc - 1 >= 0:
		deck_loc -= 1
	return

def pile_to_ace(move):
	global deck_loc
	pile_from = remaining_deck

	if len(remaining_deck) == 0:
		print("no cards left in pile, try again")
		return

	card_from = remaining_deck[deck_loc]

	aces = {}

	aces['H'] = hearts
	aces['S'] = spades
	aces['D'] = diamonds
	aces['C'] = clubs

	a0 = move[1].upper()

	pile_to = aces[a0]

	if a0 != card_from.suit:
		print("wrong suit, try again")
		return

	else:
		if len(pile_to) == 0:
			if card_from.value == 1:
				pile_to.append(card_from)
				pile_from.remove(card_from)
				if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
					hidden_cards.remove(pile_from[len(pile_from) - 1])

			else:
				print("need ace first, try again")
				return

		elif pile_to[len(pile_to) - 1].value == card_from.value - 1:
			pile_to.append(card_from)
			pile_from.remove(card_from)
			if(len(pile_from) != 0 and pile_from[len(pile_from) - 1] in hidden_cards):
				hidden_cards.remove(pile_from[len(pile_from) - 1])

		else:
			print("cannot move to ace, try again")
			return
	if deck_loc - 1 >= 0:
		deck_loc -= 1
	return

def test_column_to_column_multiple(move):
	arr = {}
	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7
	m0 = 'a' + move[0]
	m1 = 'a' + move[1]
	pile_from = arr[m0]
	pile_to = arr[m1]
	if len(move) == 3:
		num_cards = int(move[2])
	else:
		num_cards = 10 + int(move[3])
	
	if(len(pile_from) < num_cards):
		return False
	card_from = pile_from[len(arr[m0])-num_cards]
	if(len(pile_to) == 0):
		if(card_from.value != 13):
			return False
		else:
			for i in range(0, num_cards, 1):
				if pile_from[len(arr[m0])-1-i] in hidden_cards:
					return False
			return True
	else:
		card_to = pile_to[len(arr[m1])-1]
		if(check_valid(card_from, card_to)):
			for i in range(0, num_cards, 1):
				if pile_from[len(arr[m0])-1-i] in hidden_cards:
					return False
			return True
		else:
			return False
	return False

def test_column_to_column(move):
	arr = {}
	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7
	m0 = 'a' + move[0]
	m1 = 'a' + move[1]
	pile_from = arr[m0]
	pile_to = arr[m1]
	if(len(pile_from) == 0):
		return False
	card_from = pile_from[len(arr[m0])-1]
	if(len(pile_to) == 0):
		if(card_from.value != 13):
			return False
		else:
			return True
	card_to = pile_to[len(arr[m1])-1]
	if(check_valid(card_from, card_to)):
		return True
	else:
		return False

	return False

def test_column_to_ace(move):
	arr = {}
	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7
	m0 = 'a' + move[0]
	pile_from = arr[m0]
	if(len(pile_from) == 0):
		return False
	card_from = pile_from[len(arr[m0])-1]
	aces = {}
	aces['H'] = hearts
	aces['S'] = spades
	aces['D'] = diamonds
	aces['C'] = clubs
	a0 = move[1].upper()
	pile_to = aces[a0]
	if a0 != card_from.suit:
		return False
	else:
		if len(pile_to) == 0:
			if card_from.value == 1:
				return True
			else:
				return False
		if pile_to[len(pile_to) - 1].value == card_from.value - 1:
			return True
		else:
			return False
	return False

def test_pile_to_column(move):
	global deck_loc
	arr = {}

	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7

	pile_from = remaining_deck
	if len(remaining_deck) == 0:
		return False

	card_from = remaining_deck[deck_loc]
	a0 = 'a' + move[1]
	pile_to = arr[a0]

	if len(pile_to) == 0:
		if(card_from.value != 13):
			return False
		else:
			return True
	else:
		card_to = pile_to[len(pile_to) - 1]
		if(check_valid(card_from, card_to)):
			return True
		else:
			return False

	return False

def test_pile_to_ace(move):
	global deck_loc
	pile_from = remaining_deck
	if len(remaining_deck) == 0:
		return False
	card_from = remaining_deck[deck_loc]
	aces = {}
	aces['H'] = hearts
	aces['S'] = spades
	aces['D'] = diamonds
	aces['C'] = clubs
	a0 = move[1].upper()
	pile_to = aces[a0]
	if a0 != card_from.suit:
		return False
	else:
		if len(pile_to) == 0:
			if card_from.value == 1:
				return True
			else:
				return False
		if pile_to[len(pile_to) - 1].value == card_from.value - 1:
			return True
		else:
			return False
	return False


def find_all_moves():
	possible_moves = {}

	#test 'flip'
	if len(remaining_deck) > 1:
		possible_moves["F"] = 1

	#test 'pile_to_ace'
	if len(remaining_deck) > 0:
		if test_pile_to_ace("PH"):
			possible_moves.append("PH")
			possible_moves["PH"] = 2
		if test_pile_to_ace("PS"):
			possible_moves.append("PS")
			possible_moves["PS"] = 2
		if test_pile_to_ace("PD"):
			possible_moves.append("PD")
			possible_moves["PD"] = 2
		if test_pile_to_ace("PC"):
			possible_moves.append("PC")
			possible_moves["PC"] = 2

	#test 'pile_to_column'
	for i in range(1, 8):
		move = "P" + str(i)
		if test_pile_to_column(move):
			possible_moves[move] = 3

	#test 'column_to_ace'
	for i in range(1, 8):
		move = str(i) + "H"
		if test_column_to_ace(move):
			possible_moves[move] = 4
		move = str(i) + "S"
		if test_column_to_ace(move):
			possible_moves[move] = 4
		move = str(i) + "D"
		if test_column_to_ace(move):
			possible_moves[move] = 4
		move = str(i) + "C"
		if test_column_to_ace(move):
			possible_moves[move] = 4

	#test 'column_to_column'
	for i in range(1, 8):
		for j in range(1, 8):
			move = str(i) + str(j)
			if i != j and test_column_to_column(move):
				possible_moves.append(move)

	arr = {}
	arr['a1'] = c1
	arr['a2'] = c2
	arr['a3'] = c3
	arr['a4'] = c4
	arr['a5'] = c5
	arr['a6'] = c6
	arr['a7'] = c7
	#test 'column_to_column_multiple'
	for i in range(1, 8): #column from 1-7
		for j in range(1, 8): #column to 1-7
			if i != j:
				m0 = 'a' + str(i)
				pile_from = arr[m0]
				for k in range(2, len(pile_from) + 1):
					if pile_from[len(pile_from)-k] in hidden_cards:
						k = len(pile_from)
					else:
						move = str(i) + str(j) + str(k)
						if test_column_to_column_multiple(move):
							possible_moves.append(move)


	print(possible_moves)



def play():
	move = ""
	while(move != "quit"):
		if len(hearts) == 13 and len(spades) == 13 and len(diamonds) == 13 and len(clubs) == 13:
			print("congrats!! you won!\n")
			break
		find_all_moves()
		print_board()
		move = input("Move? ")
		if move == "quit":
			print()

		elif move == "help":
			print("type 'f' to flip card in pile")
			print("type 'quit' to quit")
			print("to move a card from the flip pile to a numbered pile, type P(number) {i.e. P2 to move to second pile}")
			print("to move a card from one numbered pile to another, type (num1, num2) {i.e. 35}")
			print("to move multiple cards from one numbered pile to another, type (num1, num2, number of cards) {i.e. 132}")
			print("to move a card from the flip pile to an ace pile, type P(suit initial) {i.e. PH for hearts}")
			print("to move a card from a numbered pile to an ace pile, type (num)(suit initial) {i.e. 3S}")
			print()

		elif move == "f" or move == "F":
			flip_pile()

		elif len(move) == 4:
			if not move.isnumeric() or int(move[2]) != 1:
				print("19:move not valid, try again")
			else:
				column_to_column_multiple(move)

		elif len(move) == 3:
			if not move.isnumeric():
				print("7: move not valid, try again")
			else:
				column_to_column_multiple(move)


		elif len(move) == 2:
			if move[0].isnumeric():
				if int(move[0]) < 1 or int(move[0]) > 7:
					print("1: move not valid, try again")
				else:
					if move[1].isnumeric():
						if int(move[1]) < 1 or int(move[1]) > 7 or int(move[1]) == int(move[0]):
							print("2: move not valid, try again")
						else:
							column_to_column(move)
					else:
						if move[1].upper() != 'H' and move[1].upper() != 'S' and move[1].upper() != 'D' and move[1].upper() != 'C':
							print("8: move not valid, try again")
						else:
							column_to_ace(move)

			else:
				if move[0].upper() == 'P':
					if move[1].isnumeric():
						if int(move[1]) < 1 or int(move[1]) > 7:
							print("3: move not valid, try again")
						else:
							pile_to_column(move)
					else:
						if move[1].upper() != 'H' and move[1].upper() != 'S' and move[1].upper() != 'D' and move[1].upper() != 'C':
							print("8: move not valid, try again")
						else:
							pile_to_ace(move)

				else:
					print("4: move not valid, try again")



		else:
			print("5: move not valid, try again")
		

		if move != "quit":
			move = ""

		
def main():
	deck_loc = 0
	make_full_deck()
	make_board()
	print("Welcome! For help, type 'help'\n")
	play()

if __name__ == "__main__":
	main()


