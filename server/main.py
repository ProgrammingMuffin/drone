from flask import Flask, jsonify, request
from flask_cors import CORS
import motor

app = Flask(__name__)
CORS(app)

@app.route("/gpio", methods=['POST', 'DELETE'])
def init_or_clear_gpio():
    if request.method == 'POST':
        motor.init_gpio()
    else:
        motor.clear_gpio()
    return jsonify({"message": "success"}) 

@app.route("/duty/:val", methods=['PATCH'])
def change_duty_cycle(val):
    if val == None:
        return jsonify({"message": "duty cycle is NULL"})
    return jsonify(motor.change_duty_cycle(int(val)))
    

if __name__ == "__main__":
    app.run("192.168.0.103", port=5002)
    
