import sqlite3

DB_NAME = "attendance.db"

def get_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize the database with required tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create Module table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Module (
            moduleID INTEGER PRIMARY KEY,
            numLectures INTEGER DEFAULT 0
        )
    ''')
    
    # Create Lecture table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecture (
            lectureID INTEGER PRIMARY KEY,
            moduleID INTEGER NOT NULL,
            lecturerID INTEGER NOT NULL,
            wordStart TEXT,
            wordEnd TEXT,
            FOREIGN KEY (moduleID) REFERENCES Module(moduleID)
        )
    ''')
    
    # Create Attends table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Attends (
            lectureID INTEGER NOT NULL,
            studentID INTEGER NOT NULL,
            seatNum INTEGER NOT NULL,
            PRIMARY KEY (lectureID, studentID),
            FOREIGN KEY (lectureID) REFERENCES Lecture(lectureID)
        )
    ''')
    
    conn.commit()
    conn.close()

# for testing
def populate_test_data():
    """Populate the database with test data"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Clear existing data
        cursor.execute('DELETE FROM Attends')
        cursor.execute('DELETE FROM Lecture')
        cursor.execute('DELETE FROM Module')
        
        # Insert test modules
        modules = [
            (1, 0),  # moduleID=1, numLectures=0
            (2, 0),  # moduleID=2, numLectures=0
            (3, 0),  # moduleID=3, numLectures=0
        ]
        cursor.executemany('INSERT INTO Module (moduleID, numLectures) VALUES (?, ?)', modules)
        
        # Insert test lectures with test words
        lectures = [
            (1, 1, 101, 'PYTHON', 'JAVASCRIPT'),    # lectureID=1, moduleID=1, lecturerID=101
            (2, 1, 101, 'DATABASE', 'NETWORKING'),  # lectureID=2, moduleID=1, lecturerID=101
            (3, 2, 102, 'ALGORITHM', 'DATASTRUCTURE'),  # lectureID=3, moduleID=2, lecturerID=102
        ]
        cursor.executemany(
            'INSERT INTO Lecture (lectureID, moduleID, lecturerID, wordStart, wordEnd) VALUES (?, ?, ?, ?, ?)',
            lectures
        )
        
        # Insert test attendance records
        attendance = [
            (1, 201, 1),   # lectureID=1, studentID=201, seatNum=1
            (1, 202, 2),   # lectureID=1, studentID=202, seatNum=2
            (1, 203, 3),   # lectureID=1, studentID=203, seatNum=3
            (2, 201, 1),   # lectureID=2, studentID=201, seatNum=1
            (2, 204, 4),   # lectureID=2, studentID=204, seatNum=4
            (3, 202, 2),   # lectureID=3, studentID=202, seatNum=2
            (3, 205, 5),   # lectureID=3, studentID=205, seatNum=5
        ]
        cursor.executemany(
            'INSERT INTO Attends (lectureID, studentID, seatNum) VALUES (?, ?, ?)',
            attendance
        )
        
        conn.commit()
        print("✓ Test data populated successfully")
        print(f"  - 3 modules created")
        print(f"  - 3 lectures created with words")
        print(f"  - 7 attendance records created")
    except Exception as e:
        print(f"Error populating test data: {e}")
    finally:
        conn.close()

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
        
def get_all_occupied_seats(lecture_id):
    """Returns a list of all seat numbers currently taken in a lecture"""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''SELECT seatNum FROM Attends WHERE lectureID = ?'''
    try:
        cursor.execute(query, (lecture_id,))
        # Fetch all as a list of integers
        return [row['seatNum'] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error getting occupied seats: {e}")
        return []
    finally:
        conn.close()