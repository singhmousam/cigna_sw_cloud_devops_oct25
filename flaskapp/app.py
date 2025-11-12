from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome"

task_dict = {
    'MS': ['Create TR Module'],
    'CG': ['Suggest Training Curr'],
    'AS': ['DevOps', 'Python'],
    'ASG': ['DA', 'Cloud'],
    'MZ': [ 'ML', 'DS']
}

@app.route('/greet/<name>')
def greet(name):
    try:
        return render_template('welcome.html', 
                            name=name, 
                            title='Greeting', 
                            tasks=task_dict[name.upper()])
    except KeyError:
        return "User not present, onboard user. user /onboard"

@app.route('/onboard/<name>')
def onboard(name):
    task_dict[name] = ['Cutsom Tasks']
    return f"{name} user added"

if __name__ == '__main__':
    app.run(debug=True)
