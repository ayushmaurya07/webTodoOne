import streamlit as st
import functions as todo_utils


def add_todo():
    new_todo = st.session_state["ti_add_todo"]

    local_todos = todo_utils.get_todos()
    local_todos.append(new_todo + '\n')
    todo_utils.save_todos(local_todos)


st.title("My Todo App")
st.subheader("Add / Edit / Complete a TODO")
st.write("This app will increase your productivity")

todos = todo_utils.get_todos()

for todo in todos:
    st.checkbox(
        todo,
        key=todo
    )

for index, todo in enumerate(todos):
    checkbox = st.session_state[todo]
    if checkbox:
        todos.pop(index)
        todo_utils.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(
    label="Enter a todo",
    placeholder="Type your todo here",
    on_change=add_todo,
    key="ti_add_todo"
)
