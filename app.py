from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/music")
def music():
    return render_template('sheesh.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)