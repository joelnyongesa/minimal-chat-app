from flask import Flask, make_response, jsonify, request
from flask_restful import Api, Resource
from openai import OpenAI
from flask_cors import CORS

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
api = Api(app=app)
CORS(app=app)

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

class Index(Resource):
    def get(self):
        response = make_response(jsonify({'message': 'welcome to our chat app!'}), 200)
        return response
    
class CreateMessage(Resource):
    def post(self):
        question = request.get_json().get('question')
        response = client.chat.completions.create(
            model= "gpt-3.5-turbo",
            messages= [{
                "role": "user",
                "content": question,
            }]
        )

        if response:
            return make_response(
                jsonify({
                    'message': response.choices[0].message.content,
                }), 200
            )
        
        return make_response(jsonify({'error'}), 404)
    

api.add_resource(Index, '/')
api.add_resource(CreateMessage, '/chat')

if __name__ == '__main__':
    app.run(port=5000, debug=True)