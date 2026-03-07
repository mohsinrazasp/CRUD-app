# To-Do List App

A simple task manager I built to get comfortable connecting a Python web app to a real database. You can add tasks, mark them done, edit them, and delete them. Nothing fancy, but it works.

---

## Why I built this

I wanted to stop relying on local lists or tutorials that fake the database part. This one actually talks to Supabase, so the data sticks around when you close the browser. That was the main goal.

---

## Features

**Add tasks** — Type a name and hit submit. It trims any extra spaces before saving.

**View everything** — All tasks load on the main page in the order they were added, with their current status next to them.

**Mark done or undo** — One click flips a task between Pending and Done. Click again to undo it.

**Edit a task** — Opens a separate page where you can change the title or update the status.

**Delete a task** — Asks you to confirm before it actually removes anything, so you don't delete something by accident.

**Task count** — Shows how many tasks you have at the bottom of the list.
---

## Stack

- Python and Flask for the backend
- Jinja2 for the HTML pages
- Supabase as the database (PostgreSQL under the hood)
- python-dotenv to keep the API keys out of the code

---

## Setup


### Install what you need
```bash
pip install flask supabase python-dotenv
```

### Add your Supabase credentials

Make a `.env` file in the root folder and put this in it:
```
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_anon_key
```

### Create the table in Supabase

Run this in the Supabase SQL editor:
```sql
CREATE TABLE tasks (
  id    BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  title TEXT NOT NULL,
  done  BOOLEAN DEFAULT FALSE
);
```

### Run it
```bash
python app.py
```

Then go to `http://127.0.0.1:5000` in your browser.

---

## Folder structure

```
crud-app/
├── app.py            # routes and database calls
├── templates/
│   ├── index.html    # main task list
│   ├── add.html      # form to add a task
│   └── edit.html     # form to edit a task
└── .env              # your keys, don't commit this
```

---

## What I took away from this

Figuring out how to wire Flask routes to actual database operations without an ORM was the most useful part. It made the whole request-response cycle a lot clearer.
