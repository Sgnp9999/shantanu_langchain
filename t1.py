import streamlit as st
import os

def save_uploaded_file(uploaded_file, save_directory="."):
  """Saves the uploaded file to the specified directory with a renamed filename (1.txt).

  Args:
      uploaded_file (streamlit.UploadedFile): The uploaded file object from Streamlit.
      save_directory (str, optional): The directory to save the file in. Defaults to "." (current directory).

  Returns:
      str: A success message or an error message if saving fails.
  """
  try:
    if not os.path.exists(save_directory):
      os.makedirs(save_directory)  # Create directory if it doesn't exist

    with open(os.path.join(save_directory, "1.txt"), "wb") as f:
      f.write(uploaded_file.getvalue())
    return "File saved successfully!"

  except Exception as e:
    return f"Error saving file: {e}"

def main():
  """Streamlit app layout and functionality."""

  st.title("File Uploader and Renamer")
  uploaded_file = st.file_uploader("Choose a file to upload:")

  if uploaded_file is not None:
    save_message = save_uploaded_file(uploaded_file)
    st.write(save_message)

  st.stop()

if __name__ == "__main__":
  main()
