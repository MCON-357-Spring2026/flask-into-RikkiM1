import code

from flask import Flask,request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome_endpoint():
    return "<h1>Welcome to My Flask API!</h1>"

@app.route("/about", methods=["GET"])
def about_endpoint():
    return jsonify({"name": "Rikki Mann", "course": "MCON-357 - Backend Development", "semester": "Spring 2026"});

@app.route("/greet/<name>", methods=["GET"])
def greet_endpoint(name):
    return f"<p>Hello, {name}! Welcome to Flask.</p>"

@app.route("/calculate", methods=["GET"])
def calc_endpoint():
    num1 = float(request.args.get("num1"))
    num2 = float(request.args.get("num2"))
    operation = request.args.get("operation")

    if operation == "add":
       result=  num1 + num2
    elif operation == "subtract":
        result=  num1 - num2
    elif operation == "multiply":
       result=  num1 * num2
    elif operation == "divide":
       result=  num1 / num2
    return jsonify({"result": result, "operation": operation})


@app.route("/echo", methods=["POST"])
def echo():
    print (request.get_json())
    return {"message": request.get_json(), "echoed": True}

@app.route("/status/<int:code>", methods=["GET"])
def status_endpoint(code):
    return ((f'This is a {code} error'), code)

@app.before_request
def log_request_info():
    print(f"[BEFORE] Method: {request.method}, Path: {request.path}")

@app.teardown_request
def log_exception(error):
    if error:
        print(f"[TEARDOWN] Exception occurred: {error}")
    else:
        print("[TEARDOWN] Request completed successfully.")

@app.after_request
def add_custom_header(response):
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response

@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)

if __name__ == '__main__':
        app.run(debug=True)
