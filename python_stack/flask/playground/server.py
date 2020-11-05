from flask import Flask, render_template 

app = Flask(__name__)    

@app.route('/play/<int:times>/<color>')
def color_play(times, color):
    return render_template('playground.html', times=times, color=color)	

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":      
    app.run(debug=True)    