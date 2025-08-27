from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
import gradio as gr

# Embed edilmiş veriyi yüklüyoruz
vectordb = Chroma(persist_directory="vectordb", embedding_function=OllamaEmbeddings(model="mistral"))

# Retriever ayarı
retriever = vectordb.as_retriever()

# LLM + RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm=Ollama(model="mistral"),
    retriever=retriever,
    return_source_documents=True
)

# Gradio UI fonksiyonu
def chat_with_docs(question):
    result = qa_chain({"query": question})
    return result["result"]

# Arayüz
demo = gr.Interface(fn=chat_with_docs, inputs="text", outputs="text", title="PDF Chatbot (MVP)")

# Başlat
demo.launch()
