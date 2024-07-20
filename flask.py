from flask import Flask
import random


app = Flask(__name__)
number = random.randint(0, 9)


@app.route("/")
def home():
    return '<h1 style="text-align: center; color: brown"><em>Guess the Number</em></h1>'


@app.route("/<int:guess>")
def guess_num(guess):
    if guess == number:
        return '<h1 style="text-align: center; color: green"><em>You got that Correct</em></h1>'\
               '<img style="margin-left: 600px"; src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExamlsMG1wZWFtZ2d0aHBiMjJkam85YjVrMWw0OWhqbnhlMXllNGI2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.webp" />'
    elif guess > number:
        return '<h1 style="text-align:center; color: red"><em>Too High</em></h1>'\
               '<img style="margin-left: 500px"; src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3l0Z3k1OW1naXZ3MmhvaG5weGRycTkwcWhqaWQ3aG84M212bHUzOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IuWMpDm2PdTL8s/giphy.webp"/>'
    else:
        return '<h1 style="text-align:center; color:blue"><em>Too Low</em></h1>'\
               '<img style="margin-left: 500px"; src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ20yN2hjc3E2cDMyaGJ6YWFwOW0xOXJvOXJ2anhsZHI2cm84cmhqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.webp"/>'


if __name__ == "__main__":
    app.run(debug=True, port=8001)
