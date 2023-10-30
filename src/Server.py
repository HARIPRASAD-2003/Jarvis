from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/commands', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get('command')
    # Process the command using your Jarvis logic
    # Return a response
    response = {'message': 'Command received and processed'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
