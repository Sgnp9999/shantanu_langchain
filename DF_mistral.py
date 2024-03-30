from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_community.llms import HuggingFaceEndpoint
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# # data_path = "Data.csv" 
# # df = pd.read_csv(data_path)

# llm = HuggingFaceEndpoint(
#     repo_id=repo_id,
#     temperature=0.5
# )


# def df_ask_mistral(df, question):
#     df_agent = create_pandas_dataframe_agent(llm, df)

#     def handle_parsing_error(error):
#         print(f"Error parsing LLM output: {error}")

#     response = df_agent.invoke(question, handle_parsing_errors=handle_parsing_error)
#     return response['output']

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5
)

def df_ask_mistral2(df, question):
    df_agent = create_pandas_dataframe_agent(llm, df)

    def handle_parsing_error(error):
        print(f"Error parsing LLM output: {error}")

    # questions = [
    #     "What is the unique value in the 'Country' column?"
    # ]
    questions=[]
    questions.append(question)

    for question in questions:
        try:
            response = df_agent.invoke(question, handle_parsing_errors=handle_parsing_error)
            print(f"Question: {question}")
            print(f"Answer: {response}")
            print("-" * 20)
        except Exception as e:
            print(f"An error occurred: {e}")
            response = "Error Occured (please restructure question.)"
    
    return response['output']

    
































