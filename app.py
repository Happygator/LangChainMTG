from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    print(os.getcwd())
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    # Add your chatbot logic here to generate a response
    bot_response = "This is the bot's response."

    return {'bot_response': bot_response}

if __name__ == '__main__':
    app.run(debug=True)
