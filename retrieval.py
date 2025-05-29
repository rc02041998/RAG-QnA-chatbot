from vector_store import get_vectorstore
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

LLM_MODEL = "llama2"

def get_qa_chain():
    vectordb = get_vectorstore()
    print("-----vectordb loaded------")
    retriever = vectordb.as_retriever()
    llm = Ollama(model=LLM_MODEL)
    print("fetching answers")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return qa_chain
