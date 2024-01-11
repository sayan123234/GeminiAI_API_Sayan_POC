import google.generativeai as genai
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

@app.route('/sayanGenAI', methods=['POST'])
def your_api_function():
    # Access the payload from the POST request
    payload = request.get_json()

    # Extract the value for the 'prompt' variable
    prompt_value = payload.get('prompt', '')

    api_key =os.environ.get('google_api_key')

    genai.configure(api_key=api_key)


    def get_gemini_response(question):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text

    response = get_gemini_response(prompt_value)
    return jsonify(response)

mode = "prod"

if __name__ == '__main__':
        if mode == "dev":
            app.run(debug=True,host="0.0.0.0",port=8080)
        else:
             serve(app, host="0.0.0.0", port=8080, threads=1)
