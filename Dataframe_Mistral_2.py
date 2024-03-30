from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_community.llms import HuggingFaceEndpoint
import pandas as pd
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

# data_path = "Data.csv" 
# df = pd.read_csv(data_path)

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5
)


def df_ask_mistral(df, question):
    df_agent = create_pandas_dataframe_agent(llm, df)

    def handle_parsing_error(error):
        print(f"Error parsing LLM output: {error}")

    response = df_agent.invoke(question, handle_parsing_errors=handle_parsing_error)
    return response['output']


question="How many rows do we have?"
df=pd.read_csv("Data.csv")
print(df_ask_mistral(question=question, df=df))