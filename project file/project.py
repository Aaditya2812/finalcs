from flask import Flask, render_template, request, redirect, url_for
import datetime
import random
import requests

app = Flask(__name__)

diary_file = "diary.txt"
questions_api_url = "https://api.adviceslip.com/advice"

def fetch_random_question():
    try:
        response = requests.get(questions_api_url)
        data = response.json()
        # Adjust based on the structure of the API response
        return data.get("slip", {}).get("advice", "What did you learn today?")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching question: {e}")
        return "What did you learn today?"

def save_entry(date, question, content):
    with open(diary_file, "a") as f:
        f.write(f"Date: {date}\nQuestion: {question}\nContent: {content}\n---\n")

def get_entries():
    entries = []
    try:
        with open(diary_file, "r") as f:
            content = f.read().strip().split("---")
            for entry in content:
                if entry.strip():
                    lines = entry.strip().split("\n")
                    date = lines[0].replace("Date: ", "")
                    question = lines[1].replace("Question: ", "")
                    content = "\n".join(lines[2:]).replace("Content: ", "")
                    entries.append({"date": date, "question": question, "content": content})
    except FileNotFoundError:
        pass
    return entries

@app.route("/", methods=["GET", "POST"])
def index():
    question_of_the_day = fetch_random_question()
    
    if request.method == "POST":
        content = request.form.get("content")
        question = request.form.get("question_of_the_day")  # Retrieve the question from the form
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_entry(date, question, content)  # Save the entry with the correct question
        return redirect(url_for("index"))

    entries = get_entries()
    return render_template("index.html", entries=entries, question_of_the_day=question_of_the_day)

@app.route("/delete/<entry_date>", methods=["POST"])
def delete_entry(entry_date):
    entries = get_entries()
    updated_entries = [entry for entry in entries if entry["date"] != entry_date]

    # Rewriting the file without the deleted entry
    with open(diary_file, "w") as f:
        for entry in updated_entries:
            f.write(f"Date: {entry['date']}\nQuestion: {entry['question']}\nContent: {entry['content']}\n---\n")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
