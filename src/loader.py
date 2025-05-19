import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split(data_dir: str, chunk_size=300, chunk_overlap=100):
    docs = []
    for fname in os.listdir(data_dir):
        if not fname.endswith(".txt"):
            continue
        loader = TextLoader(os.path.join(data_dir, fname), encoding="utf-8")
        docs.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)
