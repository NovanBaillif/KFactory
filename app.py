from flask import Flask, request, render_template, jsonify
import json
import re
import datetime
import openai
import collections
import os

app = Flask(__name__)

conversation_queue = collections.deque(maxlen=10)

if os.path.exists("conversations.txt") and os.path.getsize("conversations.txt") > 0:
    with open("conversations.txt", "r") as f:
        conversation_queue = collections.deque(f.readlines(), maxlen=10)
openai.api_key = os.environ['OPENAI_API_KEY']

conversations = []

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/chatbot', methods=['POST'])
def openai_chatbot():
    user = request.json['user']
    message = request.json['message']
    conversation = request.json['conversation']
    bot = "KF202301V62"
    prompt =  f"tu es {bot}, un bot test de kreol factory dans une conversartion test\n"
    if conversation:
        prompt = f"Last conversations\n:"
        prompt += f"{conversation}"
    prompt += f"\nRepondez à la question à {user} qui dit '{message}'."
    response = generate_response(prompt)
    #response = prompt
    return jsonify({'prompt': prompt, 'response': response})


def generate_response(prompt): 
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response["choices"][0]["text"]


if __name__ == '__main__':
    app.run()


