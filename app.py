import streamlit as st
import pandas as pd
from datetime import date

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Teacher Planner", page_icon="🍎", layout="wide")

# --- INITIALIZE SESSION STATE ---
# We load the data into session state ONLY ONCE so that your edits aren't overwritten

if 'week1_data' not in st.session_state:
    st.session_state.week1_data = pd.DataFrame({
        "Period / Time": [
            "Form (8.30-8.50)", "Period 1 (8.50-9.50)", "Break/Period 2 (9.50-11.05)", 
            "Period 3 (11.05-12.05)", "Period 4/Lunch (12.05-13.50)", "Lesson 5 (13.50-14.50)", "Form (14.50-15.10)"
        ],
        "Monday": ["11SIN2 E1.15 Miss Murphy", "", "9.50-10.05 Break\n10.05-11.05 10Y1 E2.14 Mrs Price", "9Y2 E2.9 Mr Mupfumbati", "12.05-13.05 8X2 E2.18 Miss Murphy\n13.05-13.50 Lunch", "", "11SIN2 E1.15 Miss Murphy"],
        "Tuesday": ["11SIN2 E1.15 Miss Murphy", "8X2 E2.18 Miss Murphy", "9.50-10.50 9Y2 E2.9 Mr Mupfumbati\n10.50-11.05 Break", "9X1 E2.4 Mr Darby", "13.05-13.50 Lunch", "10Y1 E2.14 Mrs Price", "11SIN2 E1.15 Miss Murphy"],
        "Wednesday": ["11SIN2 E1.15 Miss Murphy", "10Y1 E2.14 Mrs Price", "9.50-10.50 7Y3 E2.15 Mrs Bouf-Tah\n10.50-11.05 Break", "9Y2 E2.9 Mr Mupfumbati", "13.05-13.50 Lunch", "8X2 E2.18 Miss Murphy", "11SIN2 E1.15 Miss Murphy"],
        "Thursday": ["11SIN2 E1.15 Miss Murphy", "", "9.50-10.05 Break\nMentor Meeting E2.18", "", "12.05-12.50 Lunch\n12.50-13.50 10Y1 E2.14 Mrs Price", "", "11SIN2 E1.15 Miss Murphy"],
        "Friday": ["University", "University", "University", "University", "University", "University", "University"]
    })

if 'week2_data' not in st.session_state:
    st.session_state.week2_data = pd.DataFrame({
        "Period / Time": [
            "Form (8.30-8.50)", "Period 1 (8.50-9.50)", "Break/Period 2 (9.50-11.05)", 
            "Period 3 (11.05-12.05)", "Period 4/Lunch (12.05-13.50)", "Lesson 5 (13.50-14.50)", "Form (14.50-15.10)"
        ],
        "Monday": ["11SIN2 E1.15 Miss Murphy", "", "9.50-10.05 Break", "9Y2 E2.9 Mr Mupfumbati", "12.05-13.05 8X2 E2.18 Miss Murphy\n13.05-13.50 Lunch", "10Y1 E2.14 Mrs Price", "11SIN2 E1.15 Miss Murphy"],
        "Tuesday": ["11SIN2 E1.15 Miss Murphy", "7Y3 E2.15 Mrs Bouf-Tah", "9.50-10.50 9Y2 E2.9 Mr Mupfumbati\n10.50-11.05 Break", "", "12.05-13.05 8X2 E2.18 Miss Murphy\n13.05-13.50 Lunch", "10Y1 E2.14 Mrs Price", "11SIN2 E1.15 Miss Murphy"],
        "Wednesday": ["11SIN2 E1.15 Miss Murphy", "10Y1 E2.14 Mrs Price", "9.50-10.05 Break", "", "13.05-13.50 Lunch", "9X1 E2.4 Mr Darby", "11SIN2 E1.15 Miss Murphy"],
        "Thursday": ["11SIN2 E1.15 Miss Murphy", "9Y2 E2.9 Mr Mupfumbati", "9.50-10.05 Break", "Mentor Meeting E2.18", "12.05-13.05 8X2 E2.18 Miss Murphy\n13.05-13.50 Lunch", "7Y3 E2.15 Mrs Bouf-Tah", "11SIN2 E1.15 Miss Murphy"],
        "Friday": ["University", "University", "University", "University", "University", "University", "University"]
    })

def main():
    st.sidebar.title("🍎 Navigation")
    menu = ["Dashboard", "Schedule"]
    choice = st.sidebar.radio("Go to:", menu)

    # --- DASHBOARD PAGE ---
    if choice == "Dashboard":
        st.title("Dashboard")
        st.subheader(f"Today is {date.today().strftime('%A, %B %d, %Y')}")
        st.divider()
        st.write("### Welcome to your new planner!")
        st.write("Head over to the Schedule tab to view and edit your timetable.")

    # --- SCHEDULE PAGE ---
    elif choice == "Schedule":
        st.title("📅 Editable Two-Week Timetable")
        st.write("Click any cell to edit your classes. Your changes will save automatically while the app is open.")
        
        # Toggle between Week 1 and Week 2
        week_view = st.radio("Select Week:", ["Week 1", "Week 2"], horizontal=True)
        
        # Define uniform column sizing so it fits on one page
        col_config = {
            "Period / Time": st.column_config.TextColumn(width="medium"),
            "Monday": st.column_config.TextColumn(width="medium"),
            "Tuesday": st.column_config.TextColumn(width="medium"),
            "Wednesday": st.column_config.TextColumn(width="medium"),
            "Thursday": st.column_config.TextColumn(width="medium"),
            "Friday": st.column_config.TextColumn(width="medium"),
        }

        # Show the editor for the selected week and save the edits back to session state
        if week_view == "Week 1":
            st.session_state.week1_data = st.data_editor(
                st.session_state.week1_data, 
                hide_index=True, 
                use_container_width=True, # Forces the table to stretch to the edges of the window
                column_config=col_config,
                key="week1_editor" # A unique key is required when using multiple data_editors
            )
        else:
            st.session_state.week2_data = st.data_editor(
                st.session_state.week2_data, 
                hide_index=True, 
                use_container_width=True, 
                column_config=col_config,
                key="week2_editor"
            )

if __name__ == '__main__':
    main()
