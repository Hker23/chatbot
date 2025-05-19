from langchain.chains import RetrievalQA
from .prompt import get_prompt
from .vectorstore import build_vectorstore
from langchain_google_genai import ChatGoogleGenerativeAI

def get_qa_chain(split_docs, db_path: str):
    retriever = build_vectorstore(split_docs, db_path)
    prompt = get_prompt()
    return RetrievalQA.from_chain_type(
        llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, max_tokens=256),
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
