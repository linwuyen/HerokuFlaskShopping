from flask import Flask, render_template, request,make_response

app = Flask(__name__,static_folder='static/imges')
IMG_PATH=""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Login.html", methods=['GET'])
def Login(): 
    return render_template("Login.html")

@app.route("/cart.html", methods=['GET'])
def cart(): 
    return render_template("cart.html")

if __name__ == "__main__":
    app.run(debug=True)


