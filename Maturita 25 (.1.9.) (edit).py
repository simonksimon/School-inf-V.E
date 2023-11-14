import random
inptips = input("Zadajte svoje tipy (6 čísel oddelených medzerami): ")
tips=list(map(int, inptips.split()))
drawn_numbers = random.sample(range(1, 50), 6)
print("Vyžrebované čísla: ", random.sample(range(1, 50), 6))
correct_tips = [num for num in tips if num in drawn_numbers]
print("Uhádnuté čísla: ", correct_tips)
print("Počet uhádnutých čísel: ", len(correct_tips))
with open('loteria_1.txt', 'r') as file:
    lines = file.readlines()
all_tips = [list(map(int, line.split())) for line in lines]
results = [0]*7
for tips in all_tips:
    correct = len([num for num in tips if num in drawn_numbers])
    results[correct] += 1
for i in range(1, 7):
    print(f"Počet účastníkov, ktorí správne tipovali práve {i} číslo(-á): ", results[i])