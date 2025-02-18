class MemoryManager:
    """Handles memory for tracking user queries and follow-ups."""

    def __init__(self):
        self.history = []

    def save_query(self, query):
        """Stores user query for context awareness."""
        self.history.append(query)
    
    def get_recent_queries(self, num=3):
        """Retrieves the last few user queries."""
        return self.history[-num:]
