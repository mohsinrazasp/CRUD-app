import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from supabase import create_client, Client

load_dotenv()

app = Flask(__name__)
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route('/')
def show_all_tasks():

    response = supabase.table('tasks').select('*').order('id').execute()
    tasks = response.data
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET'])
def show_add_form():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add_task():

    title_typed_by_user = request.form['title']
    clean_title = title_typed_by_user.strip()

    if clean_title != '':
        new_task = {}
        new_task['title'] = clean_title
        supabase.table('tasks').insert(new_task).execute()
    return redirect('/')


@app.route('/edit/<int:task_id>', methods=['GET'])
def show_edit_form(task_id):

    response = supabase.table('tasks').select('*').eq('id', task_id).single().execute()
    task = response.data
    if task is None:
        return redirect('/')
    return render_template('edit.html', task=task)


@app.route('/edit/<int:task_id>', methods=['POST'])
def update_task(task_id):

    new_title = request.form['title'].strip()
    checkbox_value = request.form.get('done')
    if checkbox_value == 'on':
        is_done = True
    else:
        is_done = False
    if new_title != '':
        updated_fields = {}
        updated_fields['title'] = new_title
        updated_fields['done']  = is_done
        supabase.table('tasks').update(updated_fields).eq('id', task_id).execute()
    return redirect('/')


@app.route('/toggle/<int:task_id>')
def toggle_done(task_id):

    response = supabase.table('tasks').select('done').eq('id', task_id).single().execute()
    task = response.data
    if task is not None:
        if task['done'] == True:
            new_done_value = False
        else:
            new_done_value = True
        supabase.table('tasks').update({'done': new_done_value}).eq('id', task_id).execute()
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):

    supabase.table('tasks').delete().eq('id', task_id).execute()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)