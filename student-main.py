

def get_start_word(lectureid, userid):
    #sql statement
    pass


def get_end_word(lectureid, userid):

    pass

def is_seat_taken(lectureid, seat_num):

    pass

def check_in(word, seat):

    if word != get_start_word(lectureid, userid):
        print("Incorrect start word")

    elif seat_num == is_seat_taken(lectureid, seat_num):
        print("Seat already taken")

    else:
        print("Sign in successful")


def check_out(word):

    if end_word != get_end_word(lectureid, userid):
        print("Incorrect start word")

def check_request(request):
    if request == "check in":
        check_in(word, seat)

    elif request == "check out":
        check_out(word)


def main():

    #from front end
    request = get_request()

    check_request(request)

while True:
    main()