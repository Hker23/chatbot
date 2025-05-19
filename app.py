# from langchain.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.prompts import PromptTemplate
# from langchain.chains import RetrievalQA
# import google.generativeai as genai
# from langchain.schema.runnable import RunnableMap
# from langchain_community.document_loaders import TextLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langsmith import Client
# from langsmith import traceable
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("API_KEY")
# os.environ["API_KEY"] = os.getenv("API_KEY")
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
# os.environ["LANGCHAIN_TRACING_BACKEND"] = os.getenv("LANGCHAIN_TRACING_BACKEND", "langsmith")
# os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
# os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
# client = Client()
# # Load and split docs
# docs = []
# data_dir = "./data"  # path to your folder with knowledge base .txt files

# for file_name in os.listdir(data_dir):
#     if file_name.endswith(".txt"):
#         loader = TextLoader(os.path.join(data_dir, file_name), encoding="utf-8")
#         docs.extend(loader.load())
# splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=100)
# split_docs = splitter.split_documents(docs)

# # Create vector store
# embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
# vectordb = Chroma.from_documents(split_docs, embedding, persist_directory="./db")
# vectordb.persist()

# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.2
# )

# prompt = PromptTemplate.from_template(
#     """You are a helpful customer support assistant for an e-commerce platform.
# Respond to the user query using ONLY the provided context below.

# Context:
# {context}

# Customer Query:
# {question}

# Helpful Answer:"""
# )

# retriever = vectordb.as_retriever(search_kwargs={"k": 5})

# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     retriever=retriever,
#     chain_type="stuff",
#     return_source_documents=True,
#     chain_type_kwargs={"prompt": prompt}
# )
# import streamlit as st

# st.title("🛍️ E-commerce Customer Support Chatbot")
# user_input = st.text_input("How can I help you today?")

# if user_input:
#     try:
#         with st.spinner("Fetching response..."):
#             result = qa_chain.invoke({"query": user_input})
#             st.markdown("### ✅ Response:")
#             st.write(result["result"])

#             with st.expander("📄 Source Documents"):
#                 for doc in result["source_documents"]:
#                     st.markdown(doc.page_content[:1000])
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")

from src.app import main

if __name__ == "__main__":
    main()
