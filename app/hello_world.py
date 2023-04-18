from flask import Flask
import json

@app.route('/hello')
def hello_world():
    app.logger.info(json.dumps({'message': 'Hello, World!'}))
    return jsonify({'message': 'Hello World'})
if __name__ == '__main__':
    app.run(debug=False)
