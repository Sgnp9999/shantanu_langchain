import streamlit as st
import Mistral
import DF_mistral
import pandas as pd
import personal_mistral

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

def file_mistral(uploaded_file, question):
  try:
    processed_data = personal_mistral.mistral(question=question)
    print(processed_data)
    return processed_data
  except Exception as e:
    return f"Error processing files: {e}"

data_type = st.radio("Select Input Type:", ("Chat Online", "Chat with Personal Files", "Chat with CSV files"))

if data_type == "Chat Online":
  user_input = st.text_input("Ask question:", placeholder="What is the currency of India?")

  if st.button("Process Text"):
    if user_input:
      output = chat_function(user_input)
      st.write("Output:")
      st.success(output)
    else:
      st.error("Please enter some text to process.")

elif data_type == "Chat with CSV files":
    
  # question = "What is the unique value in the 'Country' column?"
  question=st.text_input("Ask question on CSV:", placeholder="What is the maximum value in the 'Age' column?")
  uploaded_file = st.file_uploader("Upload CSV File:")

  if uploaded_file is not None:
    if st.button("Process CSV"):
      output = csv_function(uploaded_file, question)
      st.write("Output:")
      st.code(output)

elif data_type == "Chat with Personal Files":

  question=st.text_input("Ask question on files:", placeholder="What is the phone number of Shantanu")
  uploaded_file = st.file_uploader("Upload personal File:")

  if uploaded_file is not None:
    if st.button("Send"):
      output = file_mistral(uploaded_file, question)
      st.write("Output:")
      st.code(output)
