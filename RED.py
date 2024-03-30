from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
template = """{question}"""
prompt = PromptTemplate.from_template(template)
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=128, temperature=0.5, token="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"
)
llm_chain = LLMChain(prompt=prompt, llm=llm)
while True:
    question = input("Ask Q: ")
    print("---"*20)
    print(llm_chain.run(question))
    print("---"*20)