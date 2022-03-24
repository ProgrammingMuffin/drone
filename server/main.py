from flask import Flask, jsonify, request
import motor

app = Flask(__name__)

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
    app.run(host="0.0.0.0", port=5000)
    
