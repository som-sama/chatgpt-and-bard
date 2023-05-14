import os
from flask import Flask, request, jsonify, render_template
import requests
# from bard_chat import BardChat


my_secret = os.environ['OPENAI_API_KEY']
secure_1psid = os.environ['SECURE_1PSID']
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatgpt', methods=['POST'])
# def chatgpt():
#     message = request.json['message']

#     response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', 
#                          headers={'Authorization': f'Bearer {my_secret}'}, 
#                          json={'prompt': message, 'max_tokens': 150})

#     if response.status_code == 200:
#         return jsonify({"message": response.json()['choices'][0]['text'].strip()}), 200
#     else:
#         return jsonify({"message": "An error occurred"}), 500

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    message = request.json['message']

    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions', 
                     headers={'Authorization': 'Bearer ' + my_secret}, 
                     json={'prompt': message, 'max_tokens': 150})

    if response.status_code == 200:
        return jsonify({"message": response.json()['choices'][0]['text'].strip()}), 200
    else:
        # Log error message and status code
        print(f"Error: {response.status_code}, {response.text}")
        return jsonify({"message": "An error occurred"}), 500


# @app.route('/bard', methods=['POST'])
# def bard():
#   message = request.json['message']
#   chat = BardChat(secure_1psid)
#   bard_response = chat.ask(message)
#   return jsonify({"message": bard_response}), 200

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5000)
