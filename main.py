from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/<name>")
def print_name(first_name):
    return f"Welcome {first_name}"

if __name__=="__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)

