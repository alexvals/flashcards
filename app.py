from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": 12},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "Which servant has the best personality in FGO like Ryuuuj?", "answer": "牛若丸"},
    {"question": "Which servant is the most meta in FGO?", "answer": "Castoria"},
    {"question": "By how many years is Cuba's life expectancy higher than the US'?", "answer": 0},
    {"question": "What was the in practice religion of the USSR?", "answer": "Atheism"},
    {"question": "By how many years did life expectancy in the USSR increase from the years 1925 to 1955?", "answer": "28 years"},
    {"question": "By how many years did life expectancy in China increase from the years 1940 to 1975?", "answer": "27 years"},
    {"question": "What country has the highest literacy rate in the world?", "answer": "Russia"},
    {"question": "Name a country in which women have a higher literacy rate than men.", "answer": "Lesotho, Palestine, Jamaica, Papua New Guinea, Zimbabwe, and Bangladesh"},
    {"question": "What country that has been surveyed has the lowest literacy rate for women?", "answer": "Afghanistan"},
    {"question": "What country was Ty founded in?", "answer": "The USA"},
    {"question": "How old is Maxine?", "answer": "12 years old"},
    {"question": "How tall is Roxy?", "answer": "6 inches"},
    {"question": "How many FGO servants are called Arthur?", "answer": "17"},
    {"question": "Who is Magi*Mari in FGO?", "answer": "Merlin"},
    {"question": "What knight of the round table killed King Arthur?", "answer": "Mordred, his son"},
    {"question": "How many costumes does Mash Kyrielight have in FGO?", "answer": "3"},
    {"question": "Who is considered the least powerful FGO servant?", "answer": "Anra Mainiiu"}
]

@app.route("/")
def index():
    return render_template("index.html", total=len(flashcards))

@app.route("/flashcard/<int:index>")
def flashcard(index):
    if index < len(flashcards):
        card = flashcards[index]
        return render_template("flashcard.html", card=card, index=index, total=len(flashcards))
    else:
        return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug=True)