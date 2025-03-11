import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)"""
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 1)
    except ZeroDivisionError:
        return None

def get_bmi_category(bmi):
    """Determine BMI category"""
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Set page configuration
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon="🏥",
        layout="centered"
    )

    # Title and description
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) by entering your weight and height.")

    # Create two columns for input
    col1, col2 = st.columns(2)

    with col1:
        # Weight input
        weight = st.number_input(
            "Enter your weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.1
        )

    with col2:
        # Height input
        height = st.number_input(
            "Enter your height (m)",
            min_value=0.5,
            max_value=2.5,
            value=1.7,
            step=0.01
        )

    # Calculate button
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        if bmi is not None:
            st.success(f"Your BMI is: {bmi}")
            st.info(f"Category: {category}")
            
            # Display BMI scale
            st.write("BMI Categories:")
            st.write("- Underweight: < 18.5")
            st.write("- Normal weight: 18.5 - 24.9")
            st.write("- Overweight: 25 - 29.9")
            st.write("- Obese: ≥ 30")
        else:
            st.error("Please enter valid height (cannot be zero)")

    # Add some styling
    st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()