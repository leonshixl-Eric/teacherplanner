import streamlit as st
import pandas as pd
from datetime import date, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Digital Teacher Planner", page_icon="🍎", layout="wide")

# --- INITIALIZE SESSION STATE ---
# We use \n to vertically stack Class, Teacher, and Topic to keep columns narrow
if 'week1_stacked_data' not in st.session_state:
    st.session_state.week1_stacked_data = pd.DataFrame({
        "Period / Time": [
            "Form\n(8.30-8.50)", "Period 1\n(8.50-9.50)", "Break / P2\n(9.50-11.05)", 
            "Period 3\n(11.05-12.05)", "P4 / Lunch\n(12.05-13.50)", "Lesson 5\n(13.50-14.50)", "Form\n(14.50-15.10)"
        ],
        "Monday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "", 
            "[Break]\n10Y1\nMrs Price\nTopic: ", 
            "9Y2\nMr Mupfumbati\nTopic: ", 
            "8X2\nMiss Murphy\nTopic: \n[Lunch]", 
            "", 
            "11SIN2\nMiss Murphy"
        ],
        "Tuesday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "8X2\nMiss Murphy\nTopic: ", 
            "9Y2\nMr Mupfumbati\nTopic: \n[Break]", 
            "9X1\nMr Darby\nTopic: ", 
            "[Lunch]", 
            "10Y1\nMrs Price\nTopic: ", 
            "11SIN2\nMiss Murphy"
        ],
        "Wednesday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "10Y1\nMrs Price\nTopic: ", 
            "7Y3\nMrs Bouf-Tah\nTopic: \n[Break]", 
            "9Y2\nMr Mupfumbati\nTopic: ", 
            "[Lunch]", 
            "8X2\nMiss Murphy\nTopic: ", 
            "11SIN2\nMiss Murphy"
        ],
        "Thursday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "", 
            "[Break]\nMentor Meeting", 
            "", 
            "[Lunch]\n10Y1\nMrs Price\nTopic: ", 
            "", 
            "11SIN2\nMiss Murphy"
        ],
        "Friday": ["University", "University", "University", "University", "University", "University", "University"]
    })

if 'week2_stacked_data' not in st.session_state:
    st.session_state.week2_stacked_data = pd.DataFrame({
        "Period / Time": [
            "Form\n(8.30-8.50)", "Period 1\n(8.50-9.50)", "Break / P2\n(9.50-11.05)", 
            "Period 3\n(11.05-12.05)", "P4 / Lunch\n(12.05-13.50)", "Lesson 5\n(13.50-14.50)", "Form\n(14.50-15.10)"
        ],
        "Monday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "", 
            "[Break]", 
            "9Y2\nMr Mupfumbati\nTopic: ", 
            "8X2\nMiss Murphy\nTopic: \n[Lunch]", 
            "10Y1\nMrs Price\nTopic: ", 
            "11SIN2\nMiss Murphy"
        ],
        "Tuesday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "7Y3\nMrs Bouf-Tah\nTopic: ", 
            "9Y2\nMr Mupfumbati\nTopic: \n[Break]", 
            "", 
            "8X2\nMiss Murphy\nTopic: \n[Lunch]", 
            "10Y1\nMrs Price\nTopic: ", 
            "11SIN2\nMiss Murphy"
        ],
        "Wednesday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "10Y1\nMrs Price\nTopic: ", 
            "[Break]", 
            "", 
            "[Lunch]", 
            "9X1\nMr Darby\nTopic: ", 
            "11SIN2\nMiss Murphy"
        ],
        "Thursday": [
            "11SIN2\nMiss Murphy\nTopic: ", 
            "9Y2\nMr Mupfumbati\nTopic: ", 
            "[Break]", 
            "Mentor Meeting", 
            "8X2\nMiss Murphy\nTopic: \n[Lunch]", 
            "7Y3\nMrs Bouf-Tah\nTopic: ", 
            "11SIN2\nMiss Murphy"
        ],
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
        st.write("Head over to the Schedule tab to plan your lessons.")

    elif choice == "Schedule":
        st.title("📅 Editable Two-Week Timetable")
        st.info("💡 **Tip:** Double-click any cell to expand it and type your lesson topics. The text is vertically stacked to keep the table narrow.")
        
        # --- DATE SELECTION LOGIC ---
        col1, col2 = st.columns([1, 2])
        with col1:
            today = date.today()
            last_monday = today - timedelta(days=today.weekday())
            start_date = st.date_input("Select the starting Monday for Week 1:", value=last_monday)

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        w1_col_mapping = {day: f"{day} ({(start_date + timedelta(days=i)).strftime('%b %d')})" for i, day in enumerate(days)}
        w2_col_mapping = {day: f"{day} ({(start_date + timedelta(days=i+7)).strftime('%b %d')})" for i, day in enumerate(days)}

        week_view = st.radio("Select Week:", ["Week 1", "Week 2"], horizontal=True)
        
        base_col_config = {
            "Period / Time": st.column_config.TextColumn(width="medium"),
        }

        if week_view == "Week 1":
            display_df = st.session_state.week1_stacked_data.rename(columns=w1_col_mapping)
            
            for new_col_name in w1_col_mapping.values():
                base_col_config[new_col_name] = st.column_config.TextColumn()

            edited_df = st.data_editor(
                display_df, 
                hide_index=True, 
                use_container_width=True, 
                column_config=base_col_config,
                key="week1_editor" 
            )
            
            reverse_mapping = {v: k for k, v in w1_col_mapping.items()}
            st.session_state.week1_stacked_data = edited_df.rename(columns=reverse_mapping)

        else:
            display_df = st.session_state.week2_stacked_data.rename(columns=w2_col_mapping)
            
            for new_col_name in w2_col_mapping.values():
                base_col_config[new_col_name] = st.column_config.TextColumn()

            edited_df = st.data_editor(
                display_df, 
                hide_index=True, 
                use_container_width=True, 
                column_config=base_col_config,
                key="week2_editor"
            )
            
            reverse_mapping = {v: k for k, v in w2_col_mapping.items()}
            st.session_state.week2_stacked_data = edited_df.rename(columns=reverse_mapping)

if __name__ == '__main__':
    main()
