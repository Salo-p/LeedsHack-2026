#!/usr/bin/env python3
"""
Script to populate the database with test data for development and testing
"""

from accessdb import init_db, populate_test_data

if __name__ == "__main__":
    print("=" * 60)
    print("TEST DATA SEEDER")
    print("=" * 60)
    print("\nInitializing database...")
    init_db()
    print("✓ Database schema created\n")
    
    print("Populating test data...")
    populate_test_data()
    
    print("\n" + "=" * 60)
    print("Test data setup complete!")
    print("=" * 60)
    print("\nTest Data Summary:")
    print("-" * 60)
    print("MODULES:")
    print("  - Module 1: Python Fundamentals")
    print("  - Module 2: Web Development")
    print("  - Module 3: Data Science")
    print("\nLECTURES:")
    print("  - Lecture 1 (Module 1) - Words: PYTHON / JAVASCRIPT")
    print("  - Lecture 2 (Module 1) - Words: DATABASE / NETWORKING")
    print("  - Lecture 3 (Module 2) - Words: ALGORITHM / DATASTRUCTURE")
    print("\nSTUDENT IDs (for testing):")
    print("  - 201, 202, 203, 204, 205")
    print("\nLECTURER IDs (for testing):")
    print("  - 101, 102")
    print("-" * 60)
