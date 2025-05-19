from langchain.vectorstores import Chroma
from .embeddings import get_embeddings

def build_vectorstore(docs, persist_dir: str):
    embedding = get_embeddings()
    vectordb = Chroma.from_documents(
        docs, embedding, persist_directory=persist_dir
    )
    vectordb.persist()
    return vectordb.as_retriever(search_kwargs={"k": 1})
