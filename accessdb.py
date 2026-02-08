import sqlite3

DB_NAME = "attendance.db"

def get_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# LECTURE FUNCTIONS

def log_lecture(module_id):
    """Retrieve numLectures for module, increment by 1, and update the record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''SELECT numLectures FROM Module WHERE moduleID = ?'''
    try:
        cursor.execute(query, (module_id,))
        result = cursor.fetchone()
        if result:
            num_lectures = result[0] + 1
            update_query = '''UPDATE Module SET numLectures = ? WHERE moduleID = ?'''
            cursor.execute(update_query, (num_lectures, module_id))
            conn.commit()
    except Exception as e:
        print(f"Error logging lecture: {e}")
    finally:
        conn.close()

def save_words(lecture_id, lecturer_id, start_word, end_word, module_id):
    """Save start and end words for a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''INSERT INTO Lecture (lectureID, moduleID, lecturerID, wordStart, wordEnd)
            VALUES (?, ?, ?, ?, ?)'''
    
    try:
        cursor.execute(query, (lecture_id, module_id, lecturer_id, start_word, end_word))
        conn.commit()
    except Exception as e:
        print(f"Error saving words: {e}")
    finally:
        conn.close()

def get_start_word(lecture_id):
    """Get the start word for a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''SELECT wordStart FROM Lecture WHERE lectureID = ?'''
    try:
        cursor.execute(query, (lecture_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error getting start word: {e}")
    finally:
        conn.close()

def get_end_word(lecture_id):
    """Get the end word for a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''SELECT wordEnd FROM Lecture WHERE lectureID = ?'''
    try:
        cursor.execute(query, (lecture_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error getting end word: {e}")
    finally:
        conn.close()

def get_attendance(lecture_id):
    """Get attendance numbers for a lecture. counts all records in Attends table with the given lectureID"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''SELECT COUNT(*) FROM Attends WHERE lectureID = ?'''
    try:
        cursor.execute(query, (lecture_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print(f"Error getting attendance: {e}")
    finally:
        conn.close()

# STUDENT CHECK-IN/CHECK-OUT FUNCTIONS

def save_check_in(lecture_id, student_id, seat_num):
    """Save a student check-in record. """
    conn = get_connection()
    cursor = conn.cursor()
    query = '''INSERT INTO Attends (lectureID, studentID, seatNum) VALUES (?, ?, ?)'''
    try:
        cursor.execute(query, (lecture_id, student_id, seat_num))
        conn.commit()
    except Exception as e:
        print(f"Error saving check-in: {e}")
    finally:
        conn.close()

def save_check_out(lecture_id, user_id):
    """Save a student check-out record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''DELETE FROM Attends WHERE lectureID = ? AND studentID = ?'''
    try:
        cursor.execute(query, (lecture_id, user_id))
        conn.commit()
    except Exception as e:
        print(f"Error saving check-out: {e}")
    finally:
        conn.close()

def is_seat_taken(lecture_id, seat_num):
    """Check if a seat is already taken in a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''SELECT * FROM Attends WHERE lectureID = ? AND seatNum = ?'''
    try:
        cursor.execute(query, (lecture_id, seat_num))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(f"Error checking seat: {e}")
    finally:
        conn.close()
        