from pyfiglet import Figlet
from flask import Flask

## text input
user_text = input("Enter your text: ")
user_font = input("Enter font: ")

#user_font = input("Enter your text again: ")

# print(user_text)

f = Figlet(font=user_font)

print(f.renderText(user_text))

#app = Flask(ASCII_gen.py)
#
#@app.route("127.0.0.1:5000")
#def skhello():
#    return "Test"
