"""from flask import Flask, request, jsonify
import openai

app = Flask(_name_)

# Set OpenAI API key
openai.api_key = "api key"

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('user_input', '')
    if not user_input:
        return jsonify({'error': 'No input provided!'}), 400
    
    try:
        # Make a request to the OpenAI API
        response = openai.Completion.create(
            model="gpt-4"
            engine="text-davinci-003",
            prompt=f"You are a travel guide chatbot. Answer the question: {user_input}",
            max_tokens=150,
            temperature=0.7,
        )
        reply = response.choices[0].text.strip()
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if _name== 'main_':
    app.run(debug=True)"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize the app
app = Flask(_name_)
CORS(app)  # Enable cross-origin resource sharing

# Set up OpenAI API key
openai.api_key = "api key"


# Define the ChatGPT endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("user_input", "")

    if not user_input:
        return jsonify({"error": "User input is required"}), 400

    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
        model="gpt-4",  # Specify the model
        messages=[
            {"role": "system", "content": "You are a helpful trip guide chatbot."},
            {"role": "user", "content": user_input},]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if _name_ == '_main_':
    app.run(debug=True)
