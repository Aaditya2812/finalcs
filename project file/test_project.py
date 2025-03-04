# test_project.py

import pytest
from project import fetch_random_question, save_entry, get_entries

# Test fetching a random question (could be from the API or fallback message)
def test_fetch_random_question():
    question = fetch_random_question()
    assert isinstance(question, str)  # Ensure it's a string
    assert len(question) > 0  # Ensure the question is not empty

# Test saving an entry to the diary file
def test_save_entry():
    date = "2025-03-03 12:00:00"
    question = "What did you learn today?"
    content = "I learned about Flask."
    
    save_entry(date, question, content)
    
    entries = get_entries()
    assert len(entries) > 0  # Ensure an entry was saved
    assert entries[-1]["date"] == date  # Check if the date matches the last saved entry
    assert entries[-1]["question"] == question  # Check if the question matches the last saved entry
    assert entries[-1]["content"] == content  # Check if the content matches the last saved entry

# Test getting entries from the diary file
def test_get_entries():
    entries = get_entries()
    assert isinstance(entries, list)  # Ensure the return type is a list
    assert all(isinstance(entry, dict) for entry in entries)  # Ensure each entry is a dictionary
