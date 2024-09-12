from flask import Flask

app = Flask(__name__) #that name use everywhere

@app.route('/')

def home():
    return "Hello, Welcome to the Flask Application."

if __name__ == '__main__':
    app.run(debug=True)