import streamlit as st
import Mistral
import DF_mistral
import File_Mistral
import pandas as pd
st.title("AI Chatbot")

def chat_function(user_input):
  processed_data = Mistral.ask_mistral(user_input)
  return processed_data

def csv_function(uploaded_file, question):
  try:
    df = pd.read_csv(uploaded_file)
    processed_data =  DF_mistral.df_ask_mistral2(df=df, question=question)
    print(processed_data)
    return processed_data
  except Exception as e:
    return f"Error processing CSV: {e}"

data_type = st.radio("Select Input Type:", ("Chat", "CSV", "Personal"))

if data_type == "Chat":
  user_input = st.text_input("Ask question:", placeholder="What is the currency of India?")

  if st.button("Send"):
    if user_input:
      output = chat_function(user_input)
      st.write("Output:")
      st.success(output)
    else:
      st.error("Please enter some text to process.")

elif data_type == "CSV":
    
  # question = "What is the unique value in the 'Country' column?"
  question=st.text_input("Ask question on CSV:", placeholder="What is the maximum value in the 'Age' column?")
  uploaded_file = st.file_uploader("Upload CSV File:")
  print(uploaded_file)

  if uploaded_file is not None:
    if st.button("Send"):
      output = csv_function(uploaded_file, question)
      st.write("Output:")
      st.success(output)

elif data_type == "Personal":

  question=st.text_input("Ask question on files:", placeholder="What is the phone number of Shantanu")
  uploaded_file = st.file_uploader("Upload File:")



  if uploaded_file is not None:

    with open('1.txt', 'wb') as f:
      f.write(uploaded_file.getvalue())
    st.write("File uploaded successfully.")
    if st.button("Send"):
      output = File_Mistral.mistral_with_context(uploaded_file_path="1.txt", question=question)
      st.write("Output:")
      st.success(output)