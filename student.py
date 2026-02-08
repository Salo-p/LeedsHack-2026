from accessdb import *

def check_in(lecture_id, lecturer_id, student_id, word, seat_num):
    """Check in a student with unlimited attempts"""
    correct_word = get_start_word(lecture_id, lecturer_id)
    if word.strip().upper() != correct_word.strip().upper():
        return {"error": "Incorrect start word"}
    print("Entered word:", word)
    print("Correct word:", correct_word)
    print("Seat:", seat_num)

    if word != correct_word:
        return {"error": "Incorrect start word"}

    if is_seat_taken(lecture_id, seat_num):
        return {"error": "Seat already taken"}

    save_check_in(lecture_id, student_id, seat_num)
    return {"success": True}


def check_out(lecture_id, lecturer_id, student_id, word):
    correct_word = get_end_word(lecture_id, lecturer_id)
    if word.strip().upper() != correct_word.strip().upper():
        return {"error": "Incorrect start word"}
    
    if word != correct_word:
        return {"error": "Incorrect end word"}

    save_check_out(lecture_id, student_id)
    return {"success": True}