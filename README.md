Diary App: Daily Reflections with Python

youtube demo: https://youtu.be/YSD42gqDRk8?si=FuTsZlNDkupc8C89

Description:
Welcome to the Diary App, an Aaditya Baradiya and Niccolò Arcangioli Python command-line application for our final project. The March 4, 2025, project enables users to view past posts, compose daily insights in answer to AI-generated questions from an API externally, and remove them through a Python program. This is far more complex than the course problem sets as we employ the GitHub handles Aaditya2812 and Niccolò Arcangioli to highlight our skillset in handling files, API integration, and testing.

As an answer to a daily, question-generating question—like "What was I thinking today?" or a user question based on the Advice Slip API—the Diary App, when run in the terminal, allows users to introspect about themselves. The functionalities of deleting individual entries, saving entries in a text file, drawing and printing previous entries, automatically saving dates, and sending entries through a main script are some of the most significant ones. By executing project.py within a terminal and agreeing to prompts for reflection entry, application users start the app. In order to support a strong and pleasant experience, we learned Python file I/O, API interaction with requests, and pytest testing.

We set milestones to be able to look back and verify our progress: a straightforward app with manual questions and file storage was a feasible outcome; an API integration of random questions was a more desirable outcome; and a thoroughly tested, well-designed app with stable functionality was the best outcome. Collaborating, we got the best outcome, a bug-free, tested application that supports entry management and daily reflection through collaboration and knowledge transfer.

Files in the project

The project.py

Pytest for three required functions of project.py is found in this file. It contains: fetch_random_question test: test that fetching a trusted question (or default) by verifying if the function is able to return a non-empty string.

test_save_entry: Tests the save entries as expected by verifying the most recent entry of the diary. The (date, question, and content) input is matched against the text.

test_get_entries: Validates the function works on empty files and returns a list of dictionaries. These tests meet the project's test requirement and verify the app's main feature works as expected.


test_project.py

Pytest for three required functions of project.py is found in this file. It contains: fetch_random_question test: test that fetches a trusted question (or default) by verifying if the function is able to return a non-empty string.

test_save_entry: Tests the save entries as expected by verifying the most recent entry of the diary. The (date, question, and content) input is matched against the text.

test_get_entries: Validates the function works on empty files and returns a list of dictionaries. These tests meet the project's test requirement and verify the app's main feature works as expected.


requirements.txt

This is a list of pip-installable libraries, found in the project root file.:
requests
pytest
The application will not be testable and runnable without these dependencies.

Design Choices and Reflections

For ease of use and focus on Python-only coding, we opted for a command-line interface rather than web frameworks in an attempt to fit the needs of the project. We included a backup ("What did you learn today?") for reliability, a design aspect for fault tolerance, though the advise Slip API was used for its free, random advise (reinterpretation as questions). Although we did consider having a JSON or pickle file for better formalized data, it was more practical to stay within diary.txt for simplicity and persistence. We ended up using text to reduce dependency and focus on the key features.

Parsing was easy using "---" as the delimiter in diary.txt, though additional care in get_entries was required not to create empty splits. In our project timeline, we chose a plain, functional design over introducing more interactive features, like a loop for repeated entry requests in main. In guaranteeing reliability for core use cases, we focused on functional correctness (e.g., saving, reading, and getting questions) rather than edge cases like file corruption under testing.

The command-line version of the program is focused on coding ability and meets the Python-only requirement, but is less practical than a graphical interface. We had considered implementing input checking or a menu system to make it more comprehensive, but lacked time. The work was split among members to reply with efficiency: Aaditya worked on testing and user interface logic, and Niccolò file processing and API integration.




