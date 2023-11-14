import random

def read_tips():
    tips = input("Zadajte svoje tipy (6 čísel oddelených medzerami): ")
    return list(map(int, tips.split()))

def draw_numbers():
    return random.sample(range(1, 50), 6)

def compare_tips(tips, drawn_numbers):
    return [num for num in tips if num in drawn_numbers]

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [list(map(int, line.split())) for line in lines]

def compare_all_tips(all_tips, drawn_numbers):
    results = [0]*7
    for tips in all_tips:
        correct = len(compare_tips(tips, drawn_numbers))
        results[correct] += 1
    return results

def main():
    tips = read_tips()
    drawn_numbers = draw_numbers()
    print("Vyžrebované čísla: ", drawn_numbers)
    correct_tips = compare_tips(tips, drawn_numbers)
    print("Uhádnuté čísla: ", correct_tips)
    print("Počet uhádnutých čísel: ", len(correct_tips))

    all_tips = read_file('loteria_1.txt')
    results = compare_all_tips(all_tips, drawn_numbers)
    for i in range(1, 7):
        print(f"Počet účastníkov, ktorí správne tipovali práve {i} číslo(-á): ", results[i])

main()