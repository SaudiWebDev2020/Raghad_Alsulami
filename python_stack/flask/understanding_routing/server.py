from flask import Flask  

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!' 
    
@app.route('/dojo')
def dojo(): 
    return 'Dojo!'

@app.route('/say/<name>')
def say_hi(name): 
    return f'Hi {name.capitalize()} !'

@app.route('/repeat/<int:num>/<string>')
def repeat(num, string):
    new_string = ""
    for _ in range (num):
        new_string += string + "\n" 
    return new_string

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":      
    app.run(debug=True)    