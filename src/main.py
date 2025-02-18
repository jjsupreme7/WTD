from fastapi import FastAPI
import chatbot

app = FastAPI()
chat = chatbot.TaxChatbot()

@app.get("/")
def read_root():
    return {"message": "Washington State Tax Chatbot is running"}

@app.get("/query/")
def query_tax_determination(question: str):
    response = chat.process_query(question)
    return {"response": response}
