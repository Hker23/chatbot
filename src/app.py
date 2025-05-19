import streamlit as st
from dotenv import load_dotenv
from .loader import load_and_split
from .chain import get_qa_chain
from utils.env_utils import validate_env


def main():
    load_dotenv()
    validate_env()  
    docs = load_and_split("./data")
    qa_chain = get_qa_chain(docs, "./db")

    st.title("🛍️ E-commerce Customer Support Chatbot")
    user_q = st.text_input("How can I help you today?")
    if user_q:
        with st.spinner("Fetching response..."):
            res = qa_chain.invoke({"query": user_q})
        st.markdown("### ✅ Response:")
        st.write(res["result"])
        with st.expander("📄 Source Documents"):
            for doc in res["source_documents"]:
                st.markdown(doc.page_content[:1000])

if __name__ == "__main__":
    main()
