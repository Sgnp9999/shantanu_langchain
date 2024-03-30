import streamlit as st
import os

# Function to pass the file name to MrlWithContext function
def pass_to_function(file_name):
    # Assuming MrlWithContext function exists
    result = "RUN"
    return result

# Function to delete the file after processing
def delete_file(file_name):
    os.remove(file_name)
    st.write(f"File '{file_name}' deleted successfully.")

# Main function
def main():
    st.title("File Upload and Processing")

    # File upload section
    uploaded_file = st.file_uploader("Upload a file", type=["txt"])

    if uploaded_file is not None:
        # Save file to local directory
        with open('1.txt', 'wb') as f:
            f.write(uploaded_file.getvalue())
        st.write("File uploaded successfully.")

        # Pass file name to function
        result = pass_to_function('1.txt')
        st.write("Function execution result:", result)

        # Delete file after function execution
        delete_file('1.txt')

if __name__ == "__main__":
    main()