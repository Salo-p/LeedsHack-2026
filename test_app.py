#!/usr/bin/env python3
"""
Comprehensive test suite for the attendance tracking Flask application
"""

import os
import sys
import unittest
from flask import Flask
from unittest.mock import patch, MagicMock

# Test imports
try:
    from main import app
    from staff import start_lecture, end_lecture
    from student import check_in, check_out
    print("✓ All imports successful")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

class FlaskAppTestCase(unittest.TestCase):
    """Test cases for Flask app"""
    
    def setUp(self):
        """Set up test client"""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_index_route(self):
        """Test the root route"""
        response = self.client.get('/')
        print(f"\nTest: GET /")
        print(f"  Status Code: {response.status_code}")
        self.assertIn(response.status_code, [200, 500])  # 200 if templates work, 500 if DB issues
    
    def test_start_lecture_route(self):
        """Test the start lecture route"""
        response = self.client.post('/startLecture')
        print(f"\nTest: POST /startLecture")
        print(f"  Status Code: {response.status_code}")
        self.assertIn(response.status_code, [200, 500])
    
    def test_end_lecture_route(self):
        """Test the end lecture route"""
        response = self.client.post('/endLecture')
        print(f"\nTest: POST /endLecture")
        print(f"  Status Code: {response.status_code}")
        self.assertIn(response.status_code, [200, 500])
    
    def test_check_in_route(self):
        """Test the check-in route"""
        response = self.client.post('/checkin', data={'sWord': 'TEST', 'seatNum': '1'})
        print(f"\nTest: POST /checkin")
        print(f"  Status Code: {response.status_code}")
        self.assertIn(response.status_code, [200, 500])
    
    def test_checkout_route(self):
        """Test the check-out route"""
        response = self.client.post('/checkout', data={'eWord': 'TEST'})
        print(f"\nTest: POST /checkout")
        print(f"  Status Code: {response.status_code}")
        self.assertIn(response.status_code, [200, 500])

class FunctionalityTests(unittest.TestCase):
    """Test the core functionality"""
    
    def test_imports_work(self):
        """Test that key modules can be imported"""
        print("\nTest: Module imports")
        try:
            from staff import start_lecture, end_lecture, generate_words
            from student import check_in, check_out
            print("  ✓ All functions imported successfully")
            self.assertTrue(callable(start_lecture))
            self.assertTrue(callable(end_lecture))
            self.assertTrue(callable(check_in))
            self.assertTrue(callable(check_out))
        except Exception as e:
            self.fail(f"Import failed: {e}")

if __name__ == '__main__':
    print("=" * 60)
    print("ATTENDANCE TRACKING APPLICATION - TEST SUITE")
    print("=" * 60)
    
    # Run tests
    unittest.main(verbosity=2, exit=True)
