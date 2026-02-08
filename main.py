from flask import Flask, render_template, request, redirect, url_for
from staff import start_lecture, end_lecture
from student import check_in, check_out

app = Flask(__name__, template_folder="templates")

lecture_id = 1  # Example lecture ID, replace with actual logic to get lecture ID
lecturer_id = 1  # Example lecturer ID, replace with actual logic to get lecturer ID
student_id = 1   # Example student ID, replace with actual logic to get student ID
module_id = 1    # Example module ID, replace with actual logic to get module ID

# ROOT ROUTE

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

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
        s_word = request.form.get("sWord")
        seat_num = request.form.get("seatNum")
        
        if not s_word or not seat_num:
            return render_template("studentCheckIn.html")
        
        result = check_in(
            lecture_id,
            student_id,
            s_word,
            seat_num
        )
        
        if "error" in result:
            return render_template("studentCheckIn.html")
        
        return render_template("studentMain.html")
    except Exception as e:
        print(f"Error during check-in: {e}")
        return render_template("studentCheckIn.html")

@app.route("/checkout", methods=["POST"])    
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 