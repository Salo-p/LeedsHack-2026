from db_access import *

def check_in(lecture_id, user_id, word, seat_num):
    """Check in a student with unlimited attempts"""
    correct_word = get_start_word(lecture_id)

    if word != correct_word:
        return {"error": "Incorrect start word"}

    if is_seat_taken(lecture_id, seat_num):
        return {"error": "Seat already taken"}

    save_check_in(lecture_id, user_id, seat_num)
    return {"success": True}


def check_out(lecture_id, user_id, word):
    correct_word = get_end_word(lecture_id)

    if word != correct_word:
        return {"error": "Incorrect end word"}

    save_check_out(lecture_id, user_id)
    return {"success": True}