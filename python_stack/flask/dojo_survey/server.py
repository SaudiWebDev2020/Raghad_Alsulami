from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def display_form():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomment'] = request.form['comment']
    return redirect("/show")

@app.route('/show')
def show_result():
    return render_template('index2.html')

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True) 