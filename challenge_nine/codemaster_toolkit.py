import streamlit as st

# Unit Conversion Functions
def convert_units(value, from_unit, to_unit):
    conversions = {
        ("cm", "inches"): value / 2.54,
        ("inches", "cm"): value * 2.54,
        ("kg", "lbs"): value * 2.20462,
        ("lbs", "kg"): value / 2.20462
    }
    return round(conversions.get((from_unit, to_unit), value), 2)

# Main App
def main():
    # Page Config
    st.set_page_config(
        page_title="Daily Helper Toolkit",
        page_icon="🌟",
        layout="wide",
        initial_sidebar_state="auto"
    )

    # Custom CSS for friendliness
    st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        color: #2c3e50;
        font-weight: bold;
        text-align: center;
    }
    .tool-box {
        background-color: #eef2f7;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #27ae60;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px;
    }
    .stTextInput>input {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigation
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3659/3659865.png", width=80)
        st.title("Daily Helper")
        tool = st.selectbox("Pick a Tool", ["Home", "To-Do List", "Unit Converter", "Budget Tracker"])
        st.write("Simple tools for your day!")

    # Home Page
    if tool == "Home":
        st.markdown('<p class="main-title">Daily Helper Toolkit</p>', unsafe_allow_html=True)
        st.write("Hey there! Pick a tool to make your day easier.")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="tool-box"><h3>To-Do List</h3><p>Keep tasks in check</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="tool-box"><h3>Unit Converter</h3><p>Swap units fast</p></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="tool-box"><h3>Budget Tracker</h3><p>Watch your spending</p></div>', unsafe_allow_html=True)

    # To-Do List
    elif tool == "To-Do List":
        st.markdown('<p class="main-title">To-Do List</p>', unsafe_allow_html=True)
        
        if "tasks" not in st.session_state:
            st.session_state.tasks = []

        # Add task
        with st.form("task_form", clear_on_submit=True):
            new_task = st.text_input("Add a task")
            if st.form_submit_button("Add"):
                if new_task:
                    st.session_state.tasks.append({"text": new_task, "done": False})
                    st.success("Task added!")

        # Display and manage tasks
        if st.session_state.tasks:
            for i, task in enumerate(st.session_state.tasks):
                col1, col2 = st.columns([4, 1])
                with col1:
                    if st.checkbox(task["text"], value=task["done"], key=f"task_{i}"):
                        st.session_state.tasks[i]["done"] = True
                    elif task["done"]:
                        st.session_state.tasks[i]["done"] = False
                with col2:
                    if st.button("X", key=f"del_{i}"):
                        st.session_state.tasks.pop(i)
                        st.experimental_rerun()
            
            if st.button("Clear Completed"):
                st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
                st.experimental_rerun()
        else:
            st.write("No tasks yet—add one above!")

    # Unit Converter
    elif tool == "Unit Converter":
        st.markdown('<p class="main-title">Unit Converter</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            value = st.number_input("Value", min_value=0.0, value=1.0, step=0.1)
        with col2:
            from_unit = st.selectbox("From", ["cm", "inches", "kg", "lbs"])
        with col3:
            to_unit = st.selectbox("To", ["cm", "inches", "kg", "lbs"])
        
        if st.button("Convert"):
            if from_unit != to_unit:
                result = convert_units(value, from_unit, to_unit)
                st.success(f"{value} {from_unit} = {result} {to_unit}")
            else:
                st.warning("Pick different units!")

    # Budget Tracker
    elif tool == "Budget Tracker":
        st.markdown('<p class="main-title">Budget Tracker</p>', unsafe_allow_html=True)
        
        if "expenses" not in st.session_state:
            st.session_state.expenses = []

        # Add expense
        with st.form("expense_form", clear_on_submit=True):
            desc = st.text_input("What did you spend on?")
            amount = st.number_input("Amount ($)", min_value=0.0, step=0.01)
            if st.form_submit_button("Add"):
                if desc and amount > 0:
                    st.session_state.expenses.append({"desc": desc, "amount": amount})
                    st.success("Expense added!")

        # Display expenses
        if st.session_state.expenses:
            total = sum(exp["amount"] for exp in st.session_state.expenses)
            st.write(f"**Total Spent:** ${total:.2f}")
            for i, exp in enumerate(st.session_state.expenses):
                st.write(f"- {exp['desc']}: ${exp['amount']:.2f}")
            if st.button("Clear All"):
                st.session_state.expenses = []
                st.experimental_rerun()
        else:
            st.write("No expenses yet—add one above!")

if __name__ == "__main__":
    main()