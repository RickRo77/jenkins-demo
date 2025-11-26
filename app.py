# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.get("/")
# def home():
#     return jsonify({"message": "Python CI/CD Demo API is running!"})

# @app.get("/hello/<name>")
# def greet(name):
#     return jsonify({"greeting": f"Hello, {name}!"})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"message": "Python Calculator API is running!"})

@app.get("/add")
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"result": a + b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters"}), 400

@app.get("/subtract")
def subtract():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"result": a - b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters"}), 400

@app.get("/multiply")
def multiply():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"result": a * b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters"}), 400

@app.get("/divide")
def divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        return jsonify({"result": a / b})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing parameters"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
