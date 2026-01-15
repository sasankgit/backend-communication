from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/check",methods =["POST"])
def check():
    data = request.get_json()

    if data and data.get("message") == "is it working?":
        return jsonify({"response":"hello this is working 3"})
    else:
        return jsonify({"response": "this is not right message"}),400
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port =5000)
        
