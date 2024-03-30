from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

#set env variable
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

#loading-embedding-storing file

    # loader = TextLoader('/content/drive/MyDrive/Ancient India.txt')
    # documents = loader.load()
    # text_splitter = CharacterTextSplitter (chunk_size=5,
    # chunk_overlap=0)
    # texts= text_splitter.split_documents(documents)
    # embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    # db = Chroma.from_documents(texts, embeddings)
    # db._collection.get(include=['embeddings'])
    # print("--")
    # retriever = db.as_retriever(search_kwargs={"k": 1})

#Get relevent docs based on question
# docs = retriever.get_relevant_documents(question)
# context=[i.page_content for i in docs]

#setting templates
template = """
Following is the context, based on the context answer given question:
Context={context}


{question}"""
prompt = PromptTemplate.from_template(template)
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id, max_length=128, temperature=0.5, token="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"
)
prompt_final=PromptTemplate(template=template, input_variables=['question', 'Context'])
llm_chain = LLMChain(prompt=prompt_final, llm=llm)

def mistral(question):
#   docs = retriever.get_relevant_documents(question)
#   context=[i.page_content for i in docs]
  context=['Accompanied by his devoted wife Sita and loyal brother Lakshmana, Rama embarks on a journey through the wilderness, encountering numerous challenges and adversities along the way. His unwavering commitment to dharma and his exemplary conduct inspire awe and reverence in all who witness his deeds.',
    "However, the tranquility of Rama's life is shattered when his stepmother, Queen Kaikeyi, influenced by the machinations of her maid Manthara, demands that Rama be exiled to the forest for fourteen years and that her own son, Bharata, be crowned king instead. Despite the injustice he faces, Rama accepts his exile with grace and humility, embodying the principle of duty above personal desires.",
    'The Ramayana begins with the birth of Lord Rama to King Dasharatha and Queen Kaushalya of Ayodhya. Rama, the epitome of virtue and nobility, is beloved by all who encounter him. His life unfolds with divine purpose, leading him to marry Sita, the daughter of King Janaka, in a grand ceremony that unites two noble souls destined to play pivotal roles in the cosmic drama.']

  print("Question: ", question)
  print("Context: ", context)
  return llm_chain.run(context=context, question=question)

