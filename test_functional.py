#!/usr/bin/env python3
"""
Functional tests that verify the application works with real test data
"""

import unittest
from main import app
from accessdb import init_db, populate_test_data, get_start_word, get_end_word, get_attendance

class FunctionalTestCase(unittest.TestCase):
    """Test cases using actual test data"""
    
    @classmethod
    def setUpClass(cls):
        """Set up database with test data once for all tests"""
        init_db()
        populate_test_data()
    
    def setUp(self):
        """Set up test client for each test"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_01_lecture_words_exist(self):
        """Test that lecture words were seeded correctly"""
        print("\n✓ Test: Lecture Words")
        
        # Lecture 1
        start_word = get_start_word(1)
        end_word = get_end_word(1)
        print(f"  Lecture 1: Start word = '{start_word}', End word = '{end_word}'")
        self.assertEqual(start_word, "PYTHON")
        self.assertEqual(end_word, "JAVASCRIPT")
        
        # Lecture 2
        start_word = get_start_word(2)
        end_word = get_end_word(2)
        print(f"  Lecture 2: Start word = '{start_word}', End word = '{end_word}'")
        self.assertEqual(start_word, "DATABASE")
        self.assertEqual(end_word, "NETWORKING")
    
    def test_02_attendance_recorded(self):
        """Test that attendance records exist"""
        print("\n✓ Test: Attendance Records")
        
        # Lecture 1 should have 3 students
        lecture_1_attendance = get_attendance(1)
        print(f"  Lecture 1: {lecture_1_attendance} students attended")
        self.assertEqual(lecture_1_attendance, 3)
        
        # Lecture 2 should have 2 students
        lecture_2_attendance = get_attendance(2)
        print(f"  Lecture 2: {lecture_2_attendance} students attended")
        self.assertEqual(lecture_2_attendance, 2)
        
        # Lecture 3 should have 2 students
        lecture_3_attendance = get_attendance(3)
        print(f"  Lecture 3: {lecture_3_attendance} students attended")
        self.assertEqual(lecture_3_attendance, 2)
    
    def test_03_start_lecture_flow(self):
        """Test the complete start lecture flow"""
        print("\n✓ Test: Start Lecture Flow")
        
        # Start a lecture (generates new words)
        response = self.client.post('/startLecture')
        print(f"  POST /startLecture → Status: {response.status_code}")
        self.assertEqual(response.status_code, 200)
        # Check that response contains a word (the start word is displayed in page2.html)
        self.assertIn(b'Word:', response.data)
    
    def test_04_end_lecture_flow(self):
        """Test the complete end lecture flow"""
        print("\n✓ Test: End Lecture Flow")
        
        # End the lecture
        response = self.client.post('/endLecture')
        print(f"  POST /endLecture → Status: {response.status_code}")
        self.assertEqual(response.status_code, 200)
    
    def test_05_student_checkin_flow(self):
        """Test student check-in with correct word"""
        print("\n✓ Test: Student Check-in Flow")
        
        # Test check-in with the test data words (Lecture 1)
        response = self.client.post('/checkin', data={
            'sWord': 'PYTHON',  # Correct word for Lecture 1
            'seatNum': '10'
        })
        print(f"  POST /checkin with correct word → Status: {response.status_code}")
        self.assertEqual(response.status_code, 200)
    
    def test_06_student_checkin_wrong_word(self):
        """Test student check-in with wrong word"""
        print("\n✓ Test: Student Check-in with Wrong Word")
        
        # Test check-in with wrong word
        response = self.client.post('/checkin', data={
            'sWord': 'WRONGWORD',
            'seatNum': '11'
        })
        print(f"  POST /checkin with wrong word → Status: {response.status_code}")
        self.assertEqual(response.status_code, 200)
    
    def test_07_student_checkout_flow(self):
        """Test student check-out with correct word"""
        print("\n✓ Test: Student Check-out Flow")
        
        # Test check-out with the test data words (Lecture 1)
        response = self.client.post('/checkout', data={
            'eWord': 'JAVASCRIPT'  # Correct word for Lecture 1
        })
        print(f"  POST /checkout with correct word → Status: {response.status_code}")
        self.assertEqual(response.status_code, 200)
    
    def test_08_student_checkout_wrong_word(self):
        """Test student check-out with wrong word"""
        print("\n✓ Test: Student Check-out with Wrong Word")
        
        # Test check-out with wrong word
        response = self.client.post('/checkout', data={
            'eWord': 'WRONGWORD'
        })
        print(f"  POST /checkout with wrong word → Status: {response.status_code}")
        self.assertEqual(response.status_code, 200)
    
    def test_09_all_routes_accessible(self):
        """Test that all routes are accessible"""
        print("\n✓ Test: All Routes Accessible")
        
        routes = [
            ('GET', '/', 200),
            ('POST', '/startLecture', 200),
            ('POST', '/endLecture', 200),
            ('POST', '/checkin', 200),
            ('POST', '/checkout', 200),
            ('POST', '/endWord', 200),
            ('POST', '/staffData', 200),
            ('POST', '/back', 200),
        ]
        
        for method, route, expected_status in routes:
            if method == 'GET':
                response = self.client.get(route)
            else:
                response = self.client.post(route)
            print(f"  {method:4} {route:15} → Status: {response.status_code}")
            self.assertEqual(response.status_code, expected_status)

if __name__ == '__main__':
    print("=" * 70)
    print("FUNCTIONAL TEST SUITE - Testing with Real Test Data")
    print("=" * 70)
    
    # Run tests
    unittest.main(verbosity=2, exit=True)
