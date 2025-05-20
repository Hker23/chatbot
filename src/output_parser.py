from langchain.schema import BaseOutputParser

class CustomerSupportOutputParser(BaseOutputParser):
    def parse(self, output: dict) -> str:
        answer = output.get("result", "").strip()
        sources = output.get("source_documents", [])

        formatted_sources = ""
        for i, doc in enumerate(sources):
            metadata = doc.metadata.get("source", "unknown")
            content = doc.page_content[:200].strip().replace("\n", " ")
            formatted_sources += f"\n{i+1}. {metadata}: \"{content}...\""

        return f"**Answer:**\n{answer}\n"
