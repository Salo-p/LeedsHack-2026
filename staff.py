from os import access
from accessdb import *
import random

def generate_words():
    with open("words.txt", "r") as f:
        words = [w.strip().upper() for w in f if w.strip()]

    start = random.choice(words)
    end = random.choice(words)

    while start == end:
        end = random.choice(words)

    return start, end


def start_lecture(lecture_id, lecturer_id, module_id):
    start_word, end_word = generate_words()

    log_lecture(module_id)  # Log the lecture for the module
    save_words(lecture_id, lecturer_id, start_word, end_word, module_id)  # Save the start and end words for the lecture

    return start_word


def end_lecture(lecture_id, lecturer_id):
    end_word = get_end_word(lecture_id)

    attendance = get_attendance(lecture_id)
    return end_word, attendance