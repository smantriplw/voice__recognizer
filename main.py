from os import environ
from flask import Flask, jsonify, Response, make_response, request
from recognizer import services, recognizer, get_openai_key, sr
from utility import get_keys

app = Flask(__name__)
serverPort = environ.get('PORT', '3000')

@app.route('/')
def index() -> Response:
    return jsonify({
        'ok': True,
    })

@app.route('/recognizers')
def recognizers():
    return jsonify({'error': None, 'data': get_keys(services)})

@app.route('/recognize/<service>', methods=['POST'])
def recognize(service: str):
    service = service.lower()

    if service not in services:
        return make_response(jsonify({'error': 'Invalid service'}), 400)
    
    file = request.files.get('voice')
    if file is None:
        return make_response(jsonify({'error': 'Missing file to recognize'}), 400)
    try:
        with sr.AudioFile(file) as source:
            audio = recognizer.record(source)
        
        if audio.frame_data is None:
            return make_response(jsonify({'error': 'Couldn\'t process this audio'}), 400)

        open_ai_key = get_openai_key()
        
        fn_service = services[service]
        result = ''

        if service == 'openai':
            result = fn_service(audio, api_key=open_ai_key)
        else:
            result = fn_service(audio)
    except Exception as error:
        return make_response(jsonify({'error': str(error)}), 500)

    return jsonify({'error': None, 'data': result})
    

if __name__ == '__main__':
    app.run('0.0.0.0', int(serverPort))
