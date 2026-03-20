import streamlit as st
import pandas as pd
from datetime import date

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Teacher Planner", page_icon="🍎", layout="wide")

# --- INITIALIZE SESSION STATE ---
# Changed keys to 'week1_planner_data' so it forces a refresh with the new "Topic" lines

if 'week1_planner_data' not in st.session_state:
    st.session_state.week1_planner_data = pd.DataFrame({
        "Period / Time": [
            "Form (8.30-8.50)", "Period 1 (8.50-9.50)", "Break/Period 2 (9.50-11.05)", 
            "Period 3 (11.05-12.05)", "Period 4/Lunch (12.05-13.50)", "Lesson 5 (13.50-14.50)", "Form (14.50-15.10)"
        ],
        "Monday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "", 
            "9.50-10.05 Break\n10.05-11.05 10Y1 Mrs Price\nTopic: ", 
            "9Y2 Mr Mupfumbati\nTopic: ", 
            "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", 
            "", 
            "11SIN2 Miss Murphy"
        ],
        "Tuesday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "8X2 Miss Murphy\nTopic: ", 
            "9.50-10.50 9Y2 Mr Mupfumbati\nTopic: \n10.50-11.05 Break", 
            "9X1 Mr Darby\nTopic: ", 
            "13.05-13.50 Lunch", 
            "10Y1 Mrs Price\nTopic: ", 
            "11SIN2 Miss Murphy"
        ],
        "Wednesday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "10Y1 Mrs Price\nTopic: ", 
            "9.50-10.50 7Y3 Mrs Bouf-Tah\nTopic: \n10.50-11.05 Break", 
            "9Y2 Mr Mupfumbati\nTopic: ", 
            "13.05-13.50 Lunch", 
            "8X2 Miss Murphy\nTopic: ", 
            "11SIN2 Miss Murphy"
        ],
        "Thursday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "", 
            "9.50-10.05 Break\nMentor Meeting", 
            "", 
            "12.05-12.50 Lunch\n12.50-13.50 10Y1 Mrs Price\nTopic: ", 
            "", 
            "11SIN2 Miss Murphy"
        ],
        "Friday": ["University", "University", "University", "University", "University", "University", "University"]
    })

if 'week2_planner_data' not in st.session_state:
    st.session_state.week2_planner_data = pd.DataFrame({
        "Period / Time": [
            "Form (8.30-8.50)", "Period 1 (8.50-9.50)", "Break/Period 2 (9.50-11.05)", 
            "Period 3 (11.05-12.05)", "Period 4/Lunch (12.05-13.50)", "Lesson 5 (13.50-14.50)", "Form (14.50-15.10)"
        ],
        "Monday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "", 
            "9.50-10.05 Break", 
            "9Y2 Mr Mupfumbati\nTopic: ", 
            "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", 
            "10Y1 Mrs Price\nTopic: ", 
            "11SIN2 Miss Murphy"
        ],
        "Tuesday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "7Y3 Mrs Bouf-Tah\nTopic: ", 
            "9.50-10.50 9Y2 Mr Mupfumbati\nTopic: \n10.50-11.05 Break", 
            "", 
            "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", 
            "10Y1 Mrs Price\nTopic: ", 
            "11SIN2 Miss Murphy"
        ],
        "Wednesday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "10Y1 Mrs Price\nTopic: ", 
            "9.50-10.05 Break", 
            "", 
            "13.05-13.50 Lunch", 
            "9X1 Mr Darby\nTopic: ", 
            "11SIN2 Miss Murphy"
        ],
        "Thursday": [
            "11SIN2 Miss Murphy\nTopic: ", 
            "9Y2 Mr Mupfumbati\nTopic: ", 
            "9.50-10.05 Break", 
            "Mentor Meeting", 
            "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", 
            "7Y3 Mrs Bouf-Tah\nTopic: ", 
            "11SIN2 Miss Murphy"
        ],
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
        st.write("Head over to the Schedule tab to plan your lessons for the upcoming weeks.")

    # --- SCHEDULE PAGE ---
    elif choice == "Schedule":
        st.title("📅 Editable Two-Week Timetable")
        st.info("💡 **Tip:** Double-click any cell to type your lesson topics. You can press `Enter` while typing to add multiple lines.")
        
        # Toggle between Week 1 and Week 2
        week_view = st.radio("Select Week:", ["Week 1", "Week 2"], horizontal=True)
        
        # Define uniform column sizing
        col_config = {
            "Period / Time": st.column_config.TextColumn(width="medium"),
            "Monday": st.column_config.TextColumn(width="medium"),
            "Tuesday": st.column_config.TextColumn(width="medium"),
            "Wednesday": st.column_config.TextColumn(width="medium"),
            "Thursday": st.column_config.TextColumn(width="medium"),
            "Friday": st.column_config.TextColumn(width="medium"),
        }

        # Show the editor and save edits back to session state
        if week_view == "Week 1":
            st.session_state.week1_planner_data = st.data_editor(
                st.session_state.week1_planner_data, 
                hide_index=True, 
                use_container_width=True, 
                column_config=col_config,
                key="week1_editor" 
            )
        else:
            st.session_state.week2_planner_data = st.data_editor(
                st.session_state.week2_planner_data, 
                hide_index=True, 
                use_container_width=True, 
                column_config=col_config,
                key="week2_editor"
            )

if __name__ == '__main__':
    main()
