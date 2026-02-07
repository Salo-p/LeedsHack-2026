import sqlite3

DB_NAME = "attendence.db"

def get_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# LECTURE FUNCTIONS

def log_lecture(department):
    """Retrieve Elapsed_lec for module, increment by 1, and update the record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
            SELECT ELAPSED_LEC FROM MODULES WHERE DEPARTMENT = ?
            '''
    try:
        cursor.execute(query, (department,))
        result = cursor.fetchone()
        if result:
            elapsed_lec = result[0] + 1
            update_query = '''
                           UPDATE MODULES SET ELAPSED_LEC = ? WHERE DEPARTMENT = ?
                           '''
            cursor.execute(update_query, (elapsed_lec, department))
            conn.commit()
    except Exception as e:
        print(f"Error logging lecture: {e}")
    finally:
        conn.close()

def save_words(lecture_id, lecturer_id, start_word, end_word, module=""):
    """Save start and end words for a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
            INSERT INTO LECTURES (ID, LECTURERID, STARTWORD, ENDWORD, MODULE)
            VALUES (?, ?, ?, ?, ?)
            '''
    
    try:
        cursor.execute(query, (lecture_id, lecturer_id, start_word, end_word, module))
        conn.commit()
    except Exception as e:
        print(f"Error saving words: {e}")
    finally:
        conn.close()

def get_start_word(lecture_id):
    """Get the start word for a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
            SELECT STARTWORD FROM LECTURES WHERE ID = ?
            '''
    try:
        cursor.execute(query, (lecture_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error getting start word: {e}")
    finally:
        conn.close()

def get_end_word(lecture_id, lecturer_id):
    """Get the end word for a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
            SELECT ENDWORD FROM LECTURES WHERE ID = ? AND LECTURERID = ?
            '''
    try:
        cursor.execute(query, (lecture_id, lecturer_id))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error getting end word: {e}")
    finally:
        conn.close()

def get_attendance(lecture_id):
    """Get attendance numbers for a lecture. """
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
            SELECT ATTENDING FROM SEATGRID WHERE SEATGRID.LECTURE = ?
            '''
    try:
        cursor.execute(query, (lecture_id,))
        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting attendance: {e}")
    finally:
        conn.close()

# STUDENT CHECK-IN/CHECK-OUT FUNCTIONS

def save_check_in(lecture_id, user_id, seat_num):
    """Save a student check-in record. """
    conn = get_connection()
    cursor = conn.cursor()
    query = 
    try:
        cursor.execute(query, (lecture_id, user_id, seat_num))
        conn.commit()
    except Exception as e:
        print(f"Error saving check-in: {e}")
    finally:
        conn.close()

def save_check_out(lecture_id, user_id):
    """Save a student check-out record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
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
    query = ""
    try:
        cursor.execute(query, (lecture_id, seat_num))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(f"Error checking seat: {e}")
    finally:
        conn.close()

# GENERAL DATABASE FUNCTIONS

def insert_lecture(lecturer_id, date, start_time, end_time):
    """Insert a new lecture record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (lecturer_id, date, start_time, end_time))
        conn.commit()
        return cursor.lastrowid
    except Exception as e:
        print(f"Error inserting lecture: {e}")
    finally:
        conn.close()

def get_lecture(lecture_id):
    """Get a specific lecture record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (lecture_id,))
        result = cursor.fetchone()
        return dict(result) if result else None
    except Exception as e:
        print(f"Error getting lecture: {e}")
    finally:
        conn.close()

def get_all_lectures():
    """Get all lecture records"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting all lectures: {e}")
    finally:
        conn.close()

def update_lecture(lecture_id, **kwargs):
    """Update a lecture record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, tuple(kwargs.values()) + (lecture_id,))
        conn.commit()
    except Exception as e:
        print(f"Error updating lecture: {e}")
    finally:
        conn.close()

def delete_lecture(lecture_id):
    """Delete a lecture record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (lecture_id,))
        conn.commit()
    except Exception as e:
        print(f"Error deleting lecture: {e}")
    finally:
        conn.close()

# STUDENT FUNCTIONS

def insert_student(student_id, name, email):
    """Insert a new student record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (student_id, name, email))
        conn.commit()
    except Exception as e:
        print(f"Error inserting student: {e}")
    finally:
        conn.close()

def get_student(student_id):
    """Get a specific student record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        return dict(result) if result else None
    except Exception as e:
        print(f"Error getting student: {e}")
    finally:
        conn.close()

def get_all_students():
    """Get all student records"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting all students: {e}")
    finally:
        conn.close()

def update_student(student_id, **kwargs):
    """Update a student record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, tuple(kwargs.values()) + (student_id,))
        conn.commit()
    except Exception as e:
        print(f"Error updating student: {e}")
    finally:
        conn.close()

def delete_student(student_id):
    """Delete a student record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (student_id,))
        conn.commit()
    except Exception as e:
        print(f"Error deleting student: {e}")
    finally:
        conn.close()

# STAFF FUNCTIONS

def insert_staff(staff_id, name, email, department):
    """Insert a new staff record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (staff_id, name, email, department))
        conn.commit()
    except Exception as e:
        print(f"Error inserting staff: {e}")
    finally:
        conn.close()

def get_staff(staff_id):
    """Get a specific staff record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (staff_id,))
        result = cursor.fetchone()
        return dict(result) if result else None
    except Exception as e:
        print(f"Error getting staff: {e}")
    finally:
        conn.close()

def get_all_staff():
    """Get all staff records"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting all staff: {e}")
    finally:
        conn.close()

def update_staff(staff_id, **kwargs):
    """Update a staff record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, tuple(kwargs.values()) + (staff_id,))
        conn.commit()
    except Exception as e:
        print(f"Error updating staff: {e}")
    finally:
        conn.close()

def delete_staff(staff_id):
    """Delete a staff record"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (staff_id,))
        conn.commit()
    except Exception as e:
        print(f"Error deleting staff: {e}")
    finally:
        conn.close()

# ATTENDANCE RECORD FUNCTIONS

def get_attendance_by_student(student_id):
    """Get all attendance records for a specific student"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (student_id,))
        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting student attendance: {e}")
    finally:
        conn.close()

def get_attendance_by_date(date):
    """Get all attendance records for a specific date"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (date,))
        results = cursor.fetchall()
        return [dict(row) for row in results]
    except Exception as e:
        print(f"Error getting attendance by date: {e}")
    finally:
        conn.close()

def get_student_attendance_count(student_id):
    """Get total attendance count for a student"""
    conn = get_connection()
    cursor = conn.cursor()
    query = ""
    try:
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        print(f"Error getting attendance count: {e}")
    finally:
        conn.close()
