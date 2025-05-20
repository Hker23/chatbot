from langchain.chains import RetrievalQA, LLMChain, SimpleSequentialChain
from .prompt import get_prompt
from .vectorstore import build_vectorstore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from .loader import load_and_split_file

product_docs = load_and_split_file("data/products.txt")
order_docs = load_and_split_file("data/ordering.txt")
shipping_docs = load_and_split_file("data/shipping.txt")
returns_docs = load_and_split_file("data/returns.txt")
faq_docs = load_and_split_file("data/faq.txt")
retriever_product = build_vectorstore(product_docs, "./db/product")
retriever_order = build_vectorstore(order_docs, "./db/order")
retriever_shipping = build_vectorstore(shipping_docs, "./db/shipping")
retriever_returns = build_vectorstore(returns_docs, "./db/returns")
retriever_faq = build_vectorstore(faq_docs, "./db/faq")
classify_prompt = PromptTemplate(
    input_variables=["question"],
    template="Classify this customer support question into one of these categories: product, order, shipping, returns, faq.\nQuestion: {question}\nCategory:"
)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
classify_chain = LLMChain(llm=llm, prompt=classify_prompt, output_key="category")

def select_retriever(category):
    if category == "product":
        return retriever_product
    elif category == "order":
        return retriever_order
    elif category == "shipping":
        return retriever_shipping
    elif category == "returns":
        return retriever_returns
    elif category == "faq":
        return retriever_faq
    else:
        return retriever_product

def get_qa_chain_with_prompt(retriever, prompt):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

def multi_step_qa_chain(question, prompt):
    classification_result = classify_chain.run(question)
    category = classification_result.strip().lower()
    retriever = select_retriever(category)
    qa_chain = get_qa_chain_with_prompt(retriever, prompt)
    answer = qa_chain.invoke(question)
    return answer

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