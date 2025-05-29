import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_docling import DoclingLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

PDF_FILES = [
    "data/BidIFB#03A3974.pdf",
    "data/PriceQuoteIFPQ#01A6494.pdf"
]

EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_PATH = "faiss_index"

# Load and return documents
def load_docs(file_paths):
    documents = []
    for path in file_paths:
        loader = DoclingLoader(path)
        documents = loader.load()
    return documents

#chunks the documents
def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

# Create and save the vectorstore
def create_and_save_vectorstore():
    documents = load_docs(PDF_FILES)
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    chunks = chunk_documents(documents)
    vectordb = FAISS.from_documents(chunks, embeddings)
    vectordb.save_local(VECTORSTORE_PATH)
    print("✅ Vectorstore saved at:", VECTORSTORE_PATH)

# Load the existing vectorstore
def get_vectorstore():
    print("FETCHING FROM VECTOR STORE")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectordb = FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)
    return vectordb