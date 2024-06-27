import streamlit as st
from app import Database

db = Database()

st.title("To-Do List")

data = db.view_task()

task_input = st.text_input("Enter a new task:")
btn = st.button("Add Task")

if btn:
    if task_input:
        db.add_task(task_input)
        data = db.view_task()
    else:
        st.error("Please enter a task")

for task in data:
    check = st.checkbox(f"{task[1]}", key=task[0])
    if check:
        db.delete_task(task[0])
        data = db.view_task()
        st.rerun()