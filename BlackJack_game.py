import random

def calculate_score(ls):
	sum=0
	for i in ls:
		sum+=i
	if sum==21 and len(cards)==2:
		return 0

	if 11 in cards and sum>21:
			cards.remove(11)
			card.append(1)
			return sum(ls)	

def compare(user_score, computer_score):
		if user_score>21 and computer_score>21:
			return "You want over, you lose"
		if user_score==computer_score:
				return "Draw"
		elif computer_score==0:
			return "lose, opponenet has blackjack"
		elif user_score==0:
			return "Win with a blackjack"
		elif user_score>21:
			return "You want over. you lose"
		elif computer_score>21:
			return "Opponent went over. you win"
		elif user_score>computer_score:
			return "you win"
		else:
			return "You lose"					


cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]

user_cards=[]
computer_cards=[]
is_game_over = False

for i in range(1,3):
	user_cards.append(random.choice(cards))
	computer_cards.append(random.choice(cards))
	
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print("Your's cards {user_cards}, current score {user_score}")
print("Computer's cards {computer_cards}, computer's score {computer_score}")

if user_score==0 or computer_score ==0 or user_score > 21:
	is_game_over=True
else:
	 user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
	 if user_should_deal == "y":
			user_cards.append(deal_card())
	 else:
			is_game_over = True
		
while computer_score!=0 and computer_score < 17:
		computer_cards.append(cards)  
		computer_score=calculate_score(computer_cards)

print("Your's cards {user_cards}, current score {user_score}")
print("Computer's cards {computer_cards}, computer's score {computer_score}")

print(compare(user_score, computer_score)) 