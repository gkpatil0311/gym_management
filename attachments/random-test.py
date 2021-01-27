import random

for i in range(100):
    number_person_pick = random.random()
    number_spend_pick = random.random()
    spend = 150 + 50*number_spend_pick
    if number_person_pick > 0.4: print('gaurav', spend)
    else: print('abhijeet', spend)
