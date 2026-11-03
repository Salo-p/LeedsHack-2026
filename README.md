# LeedsHack 2026


# Attendance Solution

[View our project on Devpost](https://devpost.com/software/attendance-solution)

## Overview

Makes use of seat numbers (in a hypothetical lecture theatre) coupled with a random word given/ displayed by a lectuer at the start and end of each lecture. Attendance can only be logged when a student submits the start word, seat number and end word. This encourages students to stay for the duration of the lecture. The use of seat numbers also reduces risk of sign ins from home. A visualisation of the attendance in the current lecture theatre is availbale for both the student and lecturer.

Additionally students can also get on current slides/ topics by uploading a picture of the slide to the "help" page. API link to genmini AI provides a summary and potential questions to ask the lecturer. On "enter" being pressed, questions are updated to a seperate file. Lecturer will recieve a summary of topics/ questions most asked about on Lecturer Summary Page. Many students struggle to ask questions in the lecture time so this will aide with their learning and give the lecturer a better grasp on everyone's understanding

## Features

### Lecturer Portal

* **Dynamic Check-In/Out:** Generate a random "Start Word" at the beginning of a lecture and an "End Word" at the conclusion to verify students remained present for the entire session.


* **Analytics Dashboard:** Access real-time statistics, view lecture attendance figures, and track student engagement via a leaderboard.


* **AI Topic Feedback:** View AI-queried "Cover Again" topics based on student data to identify areas where the class may need additional review.



### Student Portal

* **Secure Attendance Logging:** Students log into their specific seat number and input the generated start and end words to confirm their attendance.


* **AI Slide Analysis:** Students can upload pictures or screenshots of lecture slides directly into the application.


* **Instant Study Aids:** The AI processes the uploaded slide to provide a concise summary of the visual material and a list of relevant questions to ask or study.



## Repository Structure

The project is built using Python and structured into distinct modules for lecturers and students, utilizing a local SQLite database for record keeping:

* **`main.py`**: The primary entry point for the application, routing users to either the Lecturer or Student portals from the main welcome screen.


* **`staff.py` & `student.py**`: Dedicated backend logic for the respective user portals.


* **`attendance.db`**: The local SQLite database managing user credentials, seat numbers, and logged attendance records.


* **`accessdb.py` & `view_db.py**`: Database management scripts for querying and updating records.


* **`templates/`**: Directory containing the front-end user interface files.


* **`AI summary/`**: Directory handling the machine learning integration for slide analysis and topic generation.


* **`words.txt` & `questions.csv**`: Text and data files used for generating randomized attendance words and handling quiz/study data.


* **Testing Suite**: Includes `test_app.py`, `test_functional.py`, and `seed_testdata.py` for local validation and debugging.
