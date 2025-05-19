from langchain.prompts import PromptTemplate


def get_prompt() -> PromptTemplate:
    """
    Returns a PromptTemplate for the e-commerce customer support assistant.

    The template uses provided context and customer question to generate a helpful answer.
    """
    template = (
        "You are a helpful customer support assistant for an e-commerce platform.\n"
        "Respond to the user query using ONLY the provided context below.\n\n"
        "Context:\n{context}\n\n"
        "Customer Query:\n{question}\n\n"
        "Helpful Answer:"
    )
    return PromptTemplate.from_template(template)
