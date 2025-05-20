import streamlit as st
from dotenv import load_dotenv
from .loader import load_and_split_dir
from .chain import multi_step_qa_chain, get_qa_chain
from utils.env_utils import validate_env
from .prompt import get_prompt
from .output_parser import CustomerSupportOutputParser

def main():
    load_dotenv()
    validate_env()  
    docs = load_and_split_dir("./data")
    qa_chain = get_qa_chain(docs, "./db")
    parser = CustomerSupportOutputParser()
    prompt = get_prompt()
    st.title("🛍️ E-commerce Customer Support Chatbot")
    user_q = st.text_input("How can I help you today?")
    if user_q:
        # with st.spinner("Fetching response..."):
        #     res = multi_step_qa_chain(question=user_q, prompt=prompt)
        # st.markdown("### ✅ Response:")
        # st.write(res["result"])
        # with st.expander("📄 Source Documents"):
        #     for doc in res["source_documents"]:
        #         st.markdown(doc.page_content[:1000])
        
        with st.spinner("🔍 Fetching response..."):
            try:
                res = qa_chain.invoke({"query": user_q})
                final_output = parser.parse(res)
                st.markdown("### ✅ Response:")
                st.markdown(final_output)
                with st.expander("📄 Source Documents"):
                    for i, doc in enumerate(res["source_documents"]):
                        st.markdown(doc.page_content[:1000].strip())
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
if __name__ == "__main__":
    main()
