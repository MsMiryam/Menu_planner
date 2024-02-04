import streamlit as st

# Create a Streamlit app
st.title("Menu Builder based on Available Items")

# Input box for users to list their available items
user_input = st.text_area("Enter the food or grocery items you have available (comma-separated):")

# Convert user input into a list of items
available_items = [item.strip() for item in user_input.split(',') if item.strip()]

if available_items:
    # Create a checklist for users to select items for their menu
    selected_items = st.multiselect("Select Food Items for Your Menu", available_items)

    # Display the selected items as a menu
    st.header("Your Menu:")
    if selected_items:
        for item in selected_items:
            st.write(f"- {item}")
    else:
        st.write("No items selected yet.")
else:
    st.warning("Please enter some available items in the input box above.")
  
