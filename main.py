from flask import Flask, render_template, request, redirect, url_for
from staff import start_lecture, end_lecture
from student import check_in, check_out
from accessdb import init_db
from flask import session

app = Flask(__name__, template_folder="templates")
app.secret_key = "dev-secret-key"  # required for sessions

# Initialize database on startup
init_db()

lecture_id = 2  # Example lecture ID, replace with actual logic to get lecture ID
lecturer_id = 101  # Example lecturer ID, replace with actual logic to get lecturer ID
student_id = 4   # Example student ID, replace with actual logic to get student ID
module_id = 1    # Example module ID, replace with actual logic to get module ID

# ROOT ROUTE

@app.route("/", methods=["GET"])
def index():
    return render_template("welcome.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    return render_template("welcome.html")

@app.route("/studentMain", methods=["GET"])
def studentMain():
    return render_template("studentMain.html")

# STAFF ROUTES

@app.route("/Lecturer", methods=["POST"], endpoint="Lecturer")
def lecturer_route():
    lecture_id, start_word = start_lecture(
        lecturer_id,
        module_id
    )

    session["lecture_id"] = lecture_id  # 🔥 shared reference

    return render_template("page2.html", sWord=start_word)

@app.route("/endLecture", methods=["POST"], endpoint="endLecture")
def end_lecture_route():
        end_word, attendance = end_lecture(
            lecture_id,
            lecturer_id
        )
        return render_template("page3.html", eWord=end_word, lectureAtten=attendance)

@app.route("/staffData", methods=["POST"], endpoint="staffData")
def staff_data_route():
    return render_template("index.html")

# STUDENT ROUTES

@app.route("/Student", methods=["POST"], endpoint="Student")
def student_route():
    return render_template("studentCheckIn.html")
           

@app.route("/checkin", methods=["POST"], endpoint="checkIn")
def check_in_route():
    '''lecture_id = session.get("lecture_id")'''
    lecture_id = 2

    if not lecture_id:
        return render_template("studentCheckIn.html", error="Lecture not active")

    s_word = request.form.get("sWord")
    seat_num = request.form.get("seatNum")

    result = check_in(
        lecture_id,
        lecturer_id,
        student_id,
        s_word,
        seat_num
    )

    if "error" in result:
        return render_template("studentCheckIn.html", error=result["error"])

    return redirect(url_for("studentMain"))


@app.route("/checkout", methods=["POST"], endpoint="checkOut")    
def check_out_route():
    try:
        e_word = request.form.get("eWord")
        
        if not e_word:
            return render_template("studentMain.html")
        
        result = check_out(
            lecture_id,
            student_id,
            e_word
        )
        
        if "error" in result:
            return render_template("studentMain.html")
        
        return render_template("studentCheckIn.html")
    except Exception as e:
        print(f"Error during check-out: {e}")
        return render_template("studentMain.html")

@app.route("/endWord", methods=["POST"], endpoint="endWord")    
def end_word_route():
    try:
        e_word = request.form.get("eWord")
        
        if not e_word:
            return render_template("studentMain.html")
        
        result = check_out(
            lecture_id,
            student_id,
            e_word
        )
        
        if "error" in result:
            return render_template("studentMain.html")
        
        return render_template("studentEnd.html")
    except Exception as e:
        print(f"Error during check-out: {e}")
        return render_template("studentMain.html")

@app.route("/help", methods=["POST"], endpoint="help")
def help_route():
    return render_template("\AI summary\templates\index.html")


# BACK BUTTON ROUTES
    
@app.route("/backToWelcome", methods=["GET"])
def backToWelcome():
    return redirect(url_for("welcome"))


@app.route("/backToStudentMain", methods=["GET"])
def backToStudentMain():
    return redirect(url_for("studentMain"))

# RUN THE APP

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 

