# Diary App: Daily Reflections with Python  

## Video Demo  
**https://youtu.be/YSD42gqDRk8?si=FytKIz7fNwGDCeqH**  

## Description  
For Hult's BOS2 section last assignment, **Niccolò Arcangioli** and **Aaditya Baradiya** created the **Reflection Diary App**, a web application developed in Python. Using Flask and Python, this project, dated **March 4, 2025**, with the GitHub handles **Niccolo-Arcangioli** and **Aaditya2812**, provides users with an effective way to write daily reflections.  

Users can write, save, view, and delete entries that include **AI-generated quotes** retrieved from an external API for prompts through a basic web interface. This intricate application, far exceeding standard course problem sets, demonstrates our skills in **API integration, file handling, testing, and web design**.  

The purpose of the Reflection Diary App is to allow users to **monitor their emotional well-being**, attain **mental insight**, and reflect on their daily lives. By answering reflective prompts each day, users can develop a habit of self-reflection, fostering **self-awareness and personal growth**. The app provides an open space to reflect, allowing users to **write their thoughts, revisit previous reflections, and track their progress over time**.  

## Features  
- **Web-based interface** for user interaction.  
- **Daily reflection prompts** sourced from an AI-generated **Advice Slip API**.  
- **Ability to save and delete entries** for organized journaling.  
- **Local storage** of diary entries in a structured text file.  
- **Automated testing** to ensure reliability and stability.  

Upon running `project.py`, a local Flask server launches and can be accessed via a web browser at:  
📍 **http://127.0.0.1:5000/**  

This tool provides users with a structured space to nurture self-reflection and observe personal growth over time.  

---

## Project Files  

### `project.py`  
This is the **main Flask web application**, containing three essential functions apart from `main()`:  

1. **`fetch_random_question()`**  
   - Uses the `requests` library to retrieve a **random quote** from the **Advice Slip API** ([https://api.adviceslip.com/advice](https://api.adviceslip.com/advice)).  
   - If the API is unavailable, it defaults to:  
     > *"What did you learn today?"*  
   - This ensures users **always** have a prompt, even when offline.  

2. **`save_entry()`**  
   - Saves user responses (date, question, and reflection) to `diary.txt`.  
   - Uses `---` as a delimiter for readability and structured parsing.  

3. **`get_entries()`**  
   - Reads `diary.txt` and parses entries into a structured list of dictionaries (date, question, response).  
   - Ensures **error handling** in case the file is missing or empty.  

This script provides a **user-friendly web interface** with **Flask**, handling timestamps (`datetime`), API calls (`requests`), and data management.  

---

### `test_project.py`  
This file contains **pytest tests** to validate the core functionality of `project.py`:  

- **`test_fetch_random_question()`**  
  - Ensures the function **always returns a non-empty string**, even if the API fails.  

- **`test_save_entry()`**  
  - Checks that user responses are correctly stored in `diary.txt`.  
  - Ensures each entry includes a date, question, and response.  

- **`test_get_entries()`**  
  - Verifies that diary entries are retrieved correctly.  
  - Handles both populated and blank diary files to maintain stability.  

These tests ensure the **stability and reliability** of the application.  

---

### `requirements.txt`  
This file lists all **required dependencies** for running and testing the application:  
