from flask import Flask, redirect, url_for, render_template, request
import random
import sys

app = Flask(__name__)
message=""

# Open txt ffile
poems = open("poems.txt", "r").read()
poems = ''.join([i for i in poems if not i.isdigit()]).replace("\n\n", " ").split(' ')


# Function to generate poem
def generate_poem (lines=5):
    index = 0
    chain = {}
    words = lines*10

    for word in poems[index:]: 
        key = poems[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < words:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    return message



# Call function


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        lines = request.form['content']
        count = lines*10
        print(lines + "NUMBER OF LINES")
        messageFinal = generate_poem(int(lines))
        print(messageFinal)
    return render_template("index.html", data=messageFinal)

if __name__ == "__main__":
    app.run(debug=True)