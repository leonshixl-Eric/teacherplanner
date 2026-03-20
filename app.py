import streamlit as st
import pandas as pd
from datetime import date, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Teacher Planner", page_icon="🍎", layout="wide")

# --- INITIALIZE SESSION STATE ---
if 'week1_planner_data' not in st.session_state:
    st.session_state.week1_planner_data = pd.DataFrame({
        "Period / Time": [
            "Form (8.30-8.50)", "Period 1 (8.50-9.50)", "Break/Period 2 (9.50-11.05)", 
            "Period 3 (11.05-12.05)", "Period 4/Lunch (12.05-13.50)", "Lesson 5 (13.50-14.50)", "Form (14.50-15.10)"
        ],
        "Monday": ["11SIN2 Miss Murphy\nTopic: ", "", "9.50-10.05 Break\n10.05-11.05 10Y1 Mrs Price\nTopic: ", "9Y2 Mr Mupfumbati\nTopic: ", "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", "", "11SIN2 Miss Murphy"],
        "Tuesday": ["11SIN2 Miss Murphy\nTopic: ", "8X2 Miss Murphy\nTopic: ", "9.50-10.50 9Y2 Mr Mupfumbati\nTopic: \n10.50-11.05 Break", "9X1 Mr Darby\nTopic: ", "13.05-13.50 Lunch", "10Y1 Mrs Price\nTopic: ", "11SIN2 Miss Murphy"],
        "Wednesday": ["11SIN2 Miss Murphy\nTopic: ", "10Y1 Mrs Price\nTopic: ", "9.50-10.50 7Y3 Mrs Bouf-Tah\nTopic: \n10.50-11.05 Break", "9Y2 Mr Mupfumbati\nTopic: ", "13.05-13.50 Lunch", "8X2 Miss Murphy\nTopic: ", "11SIN2 Miss Murphy"],
        "Thursday": ["11SIN2 Miss Murphy\nTopic: ", "", "9.50-10.05 Break\nMentor Meeting", "", "12.05-12.50 Lunch\n12.50-13.50 10Y1 Mrs Price\nTopic: ", "", "11SIN2 Miss Murphy"],
        "Friday": ["University", "University", "University", "University", "University", "University", "University"]
    })

if 'week2_planner_data' not in st.session_state:
    st.session_state.week2_planner_data = pd.DataFrame({
        "Period / Time": [
            "Form (8.30-8.50)", "Period 1 (8.50-9.50)", "Break/Period 2 (9.50-11.05)", 
            "Period 3 (11.05-12.05)", "Period 4/Lunch (12.05-13.50)", "Lesson 5 (13.50-14.50)", "Form (14.50-15.10)"
        ],
        "Monday": ["11SIN2 Miss Murphy\nTopic: ", "", "9.50-10.05 Break", "9Y2 Mr Mupfumbati\nTopic: ", "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", "10Y1 Mrs Price\nTopic: ", "11SIN2 Miss Murphy"],
        "Tuesday": ["11SIN2 Miss Murphy\nTopic: ", "7Y3 Mrs Bouf-Tah\nTopic: ", "9.50-10.50 9Y2 Mr Mupfumbati\nTopic: \n10.50-11.05 Break", "", "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", "10Y1 Mrs Price\nTopic: ", "11SIN2 Miss Murphy"],
        "Wednesday": ["11SIN2 Miss Murphy\nTopic: ", "10Y1 Mrs Price\nTopic: ", "9.50-10.05 Break", "", "13.05-13.50 Lunch", "9X1 Mr Darby\nTopic: ", "11SIN2 Miss Murphy"],
        "Thursday": ["11SIN2 Miss Murphy\nTopic: ", "9Y2 Mr Mupfumbati\nTopic: ", "9.50-10.05 Break", "Mentor Meeting", "12.05-13.05 8X2 Miss Murphy\nTopic: \n13.05-13.50 Lunch", "7Y3 Mrs Bouf-Tah\nTopic: ", "11SIN2 Miss Murphy"],
        "Friday": ["University", "University", "University", "University", "University", "University", "University"]
    })

def main():
    st.sidebar.title("🍎 Navigation")
    menu = ["Dashboard", "Schedule"]
    choice = st.sidebar.radio("Go to:", menu)

    if choice == "Dashboard":
        st.title("Dashboard")
        st.subheader(f"Today is {date.today().strftime('%A, %B %d, %Y')}")
        st.divider()
        st.write("### Welcome to your new planner!")
        st.write("Head over to the Schedule tab to plan your lessons for the upcoming weeks.")

    elif choice == "Schedule":
        st.title("📅 Editable Two-Week Timetable")
        st.info("💡 **Tip:** Double-click any cell to type your lesson topics. Columns are widened to fit more text.")
        
        # --- DATE SELECTION LOGIC ---
        col1, col2 = st.columns([1, 2])
        with col1:
            # Default to the most recent Monday
            today = date.today()
            last_monday = today - timedelta(days=today.weekday())
            start_date = st.date_input("Select the starting Monday for Week 1:", value=last_monday)

        # Create dictionaries to map "Monday" to "Monday (Oct 16)", etc.
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        w1_col_mapping = {day: f"{day} ({(start_date + timedelta(days=i)).strftime('%b %d')})" for i, day in enumerate(days)}
        w2_col_mapping = {day: f"{day} ({(start_date + timedelta(days=i+7)).strftime('%b %d')})" for i, day in enumerate(days)}

        # Toggle between Week 1 and Week 2
        week_view = st.radio("Select Week:", ["Week 1", "Week 2"], horizontal=True)
        
        # Define uniform column sizing. We apply "large" to force the table to be as wide as possible.
        base_col_config = {
            "Period / Time": st.column_config.TextColumn(width="medium"),
        }

        if week_view == "Week 1":
            # 1. Rename columns for the frontend display
            display_df = st.session_state.week1_planner_data.rename(columns=w1_col_mapping)
            
            # 2. Add dynamic wide configurations for the newly named date columns
            for new_col_name in w1_col_mapping.values():
                base_col_config[new_col_name] = st.column_config.TextColumn(width="large")

            # 3. Show the editor
            edited_df = st.data_editor(
                display_df, 
                hide_index=True, 
                use_container_width=True, 
                column_config=base_col_config,
                key="week1_editor" 
            )
            
            # 4. Save edits back to session state using the original "Monday", "Tuesday" headers so logic doesn't break
            reverse_mapping = {v: k for k, v in w1_col_mapping.items()}
            st.session_state.week1_planner_data = edited_df.rename(columns=reverse_mapping)

        else:
            # Same logic as above, but for Week 2
            display_df = st.session_state.week2_planner_data.rename(columns=w2_col_mapping)
            
            for new_col_name in w2_col_mapping.values():
                base_col_config[new_col_name] = st.column_config.TextColumn(width="large")

            edited_df = st.data_editor(
                display_df, 
                hide_index=True, 
                use_container_width=True, 
                column_config=base_col_config,
                key="week2_editor"
            )
            
            reverse_mapping = {v: k for k, v in w2_col_mapping.items()}
            st.session_state.week2_planner_data = edited_df.rename(columns=reverse_mapping)

if __name__ == '__main__':
    main()
