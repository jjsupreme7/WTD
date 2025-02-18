from src import memory

import pdf_loader
import vector_store
import utils

class TaxChatbot:
    """Main chatbot for handling tax-related queries using WA tax determination PDFs."""

    def __init__(self):
        self.memory = memory.MemoryManager()
        self.vector_store = vector_store.VectorSearch()
        self.pdf_loader = pdf_loader.PDFLoader()

    def process_query(self, query):
        """Processes the user query and provides a structured response."""
        self.memory.save_query(query)  # Save query for context tracking

        # Search for the most relevant tax determinations
        results = self.vector_store.search(query, top_k=50)

        if not results:
            return "No relevant tax determinations found."

        structured_results = []
        
        for doc in results:
            summary = utils.generate_detailed_summary(doc.text)
            legal_refs = utils.extract_legal_references(doc.text)
            relevance_score = utils.rank_relevance(doc.text, query)
            legal_explanations = utils.explain_legal_references(legal_refs, doc.text)
            
            structured_results.append({
                "title": doc.metadata.get("filename", "Unknown"),
                "summary": summary,
                "references": legal_refs,
                "explanations": legal_explanations,
                "relevance": relevance_score
            })

        # Sort results by highest relevance
        structured_results.sort(key=lambda x: x["relevance"], reverse=True)

        response = "**Most relevant tax determinations:**\n\n"
        for i, doc in enumerate(structured_results[:10]):  # Show top 10
            response += f"{i+1}️⃣ **{doc['title']}**\n"
            response += f"- **Summary**: {doc['summary']}\n"
            response += f"- **Legal References**: {', '.join(doc['references'])}\n"
            response += f"- **Legal Explanations**: {doc['explanations']}\n\n"

        return response

# Example usage
if __name__ == "__main__":
    chatbot = TaxChatbot()
    while True:
        user_query = input("Ask a tax-related question: ")
        if user_query.lower() in ["exit", "quit"]:
            break
        print(chatbot.process_query(user_query))
