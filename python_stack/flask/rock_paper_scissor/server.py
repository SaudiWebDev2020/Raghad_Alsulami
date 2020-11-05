from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes  

@app.route('/')
def display():
    session['user_wins'] = 0
    session['user_losses'] = 0
    session['user_ties'] = 0 
    return render_template('index.html')	

@app.route('/process', methods=["POST"])
def process():
    session['user_choice'] = request.form['choice'].lower().capitalize()
    options = ["rock", "paper", "scissors"]
    session['computer_choice'] = options[random.randint(0,2)].capitalize()

    if session['user_choice'] == session['computer_choice']: 
        session['user_result'] = 'Tie'
    elif session['user_choice']=='Rock':
        if session['computer_choice'] == 'Paper':
            session['user_result']='Lose'
        else:
            session['user_result']='Win'
    elif session['user_choice']=='Paper':
        if session['computer_choice'] == 'Scissors':
            session['user_result']='Lose'
        else:
            session['user_result']='Win'
    elif session['user_choice']=='Scissors':
        if session['computer_choice'] == 'Rock':
            session['user_result']='Lose'
        else:
            session['user_result']='Win'
    return redirect('/show_result')	

@app.route('/show_result')
def show_result():
    if session['user_result'] == 'Win':
            session['user_wins'] += 1
    elif session['user_result'] == 'Lose':
            session['user_losses'] += 1
    else: 
        session['user_ties'] += 1
    return render_template('index.html', pharse="show")	

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   
    app.run(debug=True) 
