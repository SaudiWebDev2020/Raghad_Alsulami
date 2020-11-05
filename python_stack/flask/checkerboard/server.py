from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_board():
    return render_template('index.html', x_axis=8, y_axis=8, color1='red', color2='black')

@app.route('/<int:x_axis>')
def board_by_x_axis(x_axis):
    return render_template('index.html', x_axis=x_axis, y_axis=8, color1='red', color2='black')

@app.route('/<int:x_axis>/<int:y_axis>')
def create_board(x_axis, y_axis):
    return render_template('index.html', x_axis=x_axis, y_axis=y_axis, color1='red', color2='black')

@app.route('/<int:x_axis>/<int:y_axis>/<color1>/<color2>')
def board_by_color(x_axis, y_axis, color1, color2):
    return render_template('index.html', x_axis=x_axis, y_axis=y_axis, color1=color1, color2=color2)

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)