from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "hello flask"

@app.route("/test")
def test():
    return "this is test"

if __name__=="__name__":
    app.run()