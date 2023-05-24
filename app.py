from flask import Flask, render_template, request
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import api_key
import os


app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = api_key.api_key
vectordb = Chroma(persist_directory="./data", embedding_function=OpenAIEmbeddings())
retriever = vectordb.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)
@app.route('/')
def home():
    print(os.getcwd())
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    # Add your chatbot logic here to generate a response
    result = qa_chain({'query': user_message})
    bot_response = result['result']
    return {'bot_response': bot_response}

if __name__ == '__main__':
    app.run(debug=True)
