from flask import Flask, render_template, request, redirect, url_for
from staff import start_lecture, end_lecture
from student import check_in, check_out

app = Flask(__name__)


#app route
#function def
    start_word = start_lecture(
        request.lecture_id,
        request.user_id
    )
    return {"start_word": start_word}

#app route
#function def
        end_word, attendance = end_lecture(
            request.lecture_id,
            request.user_id
        )
        return {
            "end_word": end_word,
            "attendance": attendance
        }


@app.route("/checkin", methods=["POST"])
def checkin():
    check_in(
        request.lecture_id,
        request.user_id,
        request.form["sWord"]
        request.form["seatNum"]
    )

    return render_template("studentMain.html")

@app.route("/checkout", methods=["POST"])    
def checkout():
    check_out(
        request.lecture_id,
        request.user_id,
        request.form["eWord"]
    )

    return render_template("studentCheckIn.html") 