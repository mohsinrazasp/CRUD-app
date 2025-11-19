from flask import Flask, redirect ,render_template, request
app = Flask(__name__)

tasks=[]
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add')
def show_add_form():
    return render_template('add.html')


@app.route ('/add',methods=['POST'])
def add_task():

    task_name = request.form['task_name']
    tasks.append(task_name)
    return redirect('/')



@app.route('/delete/<int:task_id>')
def delete_task(task_id):

    tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)