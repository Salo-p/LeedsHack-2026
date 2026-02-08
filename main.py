from flask import Flask, render_template, request, redirect, url_for
from staff import start_lecture, end_lecture
from student import check_in, check_out

app = Flask(__name__)

lecture_id = 1  # Example lecture ID, replace with actual logic to get lecture ID
lecturer_id = 1  # Example lecturer ID, replace with actual logic to get lecturer ID
student_id = 1   # Example student ID, replace with actual logic to get student ID
module_id = 1    # Example module ID, replace with actual logic to get module ID

# STAFF ROUTES

@app.route("/startLecture", methods=["POST"])
def start_lecture_route():
    start_word = start_lecture(
        lecture_id,
        lecturer_id,
        module_id
    )
    return render_template("page2.html", sWord=start_word)

@app.route("/endLecture", methods=["POST"])
def end_lecture_route():
        end_word, attendance = end_lecture(
            lecture_id,
            lecturer_id
        )
        return render_template("page3.html", eWord=end_word, lectureAtten=attendance)


# STUDENT ROUTES

@app.route("/checkin", methods=["POST"])
def check_in_route():
    try:
        check_in(
            request.lecture_id,
            request.user_id,
            request.form["sWord"],
            request.form["seatNum"]
        )
        return render_template("studentMain.html")
    except Exception as e:
        print(f"Error during check-in: {e}")
        return render_template("studentCheckIn.html")
    finally:
        # cleanup only; do not return from here
        pass

@app.route("/checkout", methods=["POST"])    
def check_out_route():
    check_out(
        request.lecture_id,
        request.user_id,
        request.form["eWord"]
    )

    return render_template("studentCheckIn.html") 