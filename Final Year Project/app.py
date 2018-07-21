from flask import Flask, render_template, request
import sys
from main import main as ret

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/send',methods = ['POST', 'GET'])
def send():
   if request.method == 'POST':
      question = request.form['question']
      answer = ret(question)
      return render_template("result.html",question=question, answer=answer)

if __name__ == "__main__":
    app.run()