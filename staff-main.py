import random

LECTURE_IN_PROGRESS = False


def generate_word():
    with open("words.txt", "r") as f:
        lines = f.read().splitlines()

    random_line = random.choice(lines).upper()
    return random_line


def main(LECTURE_IN_PROGRESS):

    if not(LECTURE_IN_PROGRESS):
        #press button
        inp = input("start button ")

        if inp == "y":
            LECTURE_IN_PROGRESS = True
            print("LECTURE STARTED")
            print(generate_word())

    else:
        #press button
        inp = input("end button ")

        if inp == "y":
            LECTURE_IN_PROGRESS = False
            print("LECTURE ENDED")
            print(generate_word())

            #give data on attendance
    
    return LECTURE_IN_PROGRESS
    
while True:
    LECTURE_IN_PROGRESS = main(LECTURE_IN_PROGRESS)
