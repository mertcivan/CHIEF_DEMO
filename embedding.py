import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma

# 📁 PDF klasör yolu
pdf_dir = "data/"
vectordb_path = "vectordb/"

# 🔢 Embed modeli
embedding = OllamaEmbeddings(model="mistral")

# 📚 Tüm dokümanları yükle
all_docs = []
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        path = os.path.join(pdf_dir, filename)
        print(f"📄 Yükleniyor: {filename}")
        loader = PyPDFLoader(path)
        docs = loader.load()
        all_docs.extend(docs)

# ✂️ Chunk'lara böl
print("🔪 Chunk işlemi başladı...")
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(all_docs)

# 💾 Chroma DB’ye yaz
print("💾 Embed işlemi başlatıldı...")
if not os.path.exists(vectordb_path):
    os.makedirs(vectordb_path)

db = Chroma.from_documents(chunks, embedding=embedding, persist_directory=vectordb_path)
db.persist()

print("✅ Tüm PDF'ler embed edildi ve veritabanına kaydedildi!")
