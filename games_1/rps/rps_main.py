from flask import Flask, request, render_template
import rps   # import your game file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # render the HTML form

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form.get('choice')  # get the user's choice
    result = rps.play(user_choice)  # run the game logic
    return render_template('result.html', result=result)  # render the result

if __name__ == '__main__':
    app.run(debug=True)