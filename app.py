import streamlit as st
import pandas as pd
from datetime import date

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Teacher Planner", page_icon="🍎", layout="wide")

# --- SESSION STATE INITIALIZATION ---
# This keeps our to-do list data saved while clicking around the app
if 'todos' not in st.session_state:
    st.session_state.todos = ["Grade Math quizzes", "Prepare Science lab", "Email parents"]

def main():
    st.sidebar.title("🍎 Navigation")
    menu = ["Dashboard", "Schedule", "To-Do List", "Student Roster"]
    choice = st.sidebar.radio("Go to:", menu)

    # --- DASHBOARD PAGE ---
    if choice == "Dashboard":
        st.title("Welcome back!")
        st.subheader(f"Today is {date.today().strftime('%B %d, %Y')}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Pending Tasks", value=len(st.session_state.todos))
        with col2:
            st.metric(label="Classes Today", value="4")
        with col3:
            st.metric(label="Upcoming Meetings", value="1")
            
        st.divider()
        st.write("### Quick Glance: Next Class")
        st.info("**10:00 AM - 11:30 AM:** Advanced Biology (Room 204)")

    # --- SCHEDULE PAGE ---
    elif choice == "Schedule":
        st.title("📅 Weekly Schedule")
        
        # Sample schedule data
        schedule_data = {
            "Time": ["08:00 AM", "09:30 AM", "11:00 AM", "01:00 PM", "02:30 PM"],
            "Monday": ["Prep Period", "Biology 101", "Lunch", "Chemistry", "Study Hall"],
            "Tuesday": ["Staff Meeting", "Biology 101", "Lunch", "Lab Prep", "Grading"],
            "Wednesday": ["Prep Period", "Biology 101", "Lunch", "Chemistry", "Study Hall"],
            "Thursday": ["Parent Calls", "Biology 101", "Lunch", "Lab Prep", "Grading"],
            "Friday": ["Prep Period", "Biology 101", "Lunch", "Chemistry", "Early Dismissal"]
        }
        df = pd.DataFrame(schedule_data)
        
        # Display the dataframe without the index
        st.dataframe(df, hide_index=True, use_container_width=True)

    # --- TO-DO LIST PAGE ---
    elif choice == "To-Do List":
        st.title("📝 Task Management")
        
        # Input for new tasks
        new_task = st.text_input("Add a new task:", placeholder="E.g., Print history worksheets")
        if st.button("Add Task"):
            if new_task:
                st.session_state.todos.append(new_task)
                st.success(f"Added: '{new_task}'")
                st.rerun() # Refresh to show the new task
        
        st.divider()
        st.write("### Current Tasks")
        
        # Display tasks with a delete button for each
        for i, task in enumerate(st.session_state.todos):
            col1, col2 = st.columns([0.9, 0.1])
            with col1:
                st.checkbox(task, key=f"check_{i}")
            with col2:
                if st.button("❌", key=f"del_{i}"):
                    st.session_state.todos.pop(i)
                    st.rerun()

    # --- STUDENT ROSTER PAGE ---
    elif choice == "Student Roster":
        st.title("👥 Student Roster")
        st.write("Track basic student information and grades here.")
        
        roster_data = {
            "Student Name": ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince"],
            "Grade Level": [10, 10, 10, 10],
            "Current Grade": ["A", "B+", "B-", "A+"],
            "Notes": ["Great participation", "Needs help with homework", "Excellent test scores", "Leader in group work"]
        }
        roster_df = pd.DataFrame(roster_data)
        
        # Using data_editor allows you to edit the table directly in the app!
        st.data_editor(roster_df, num_rows="dynamic", use_container_width=True)

if __name__ == '__main__':
    main()
