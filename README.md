# CHIEF_DEMO
 155 / 5.000 CHIEF is a hybrid structure that enables corporate companies to use document-based information systems securely and flexibly with LLM models.

 embedding.py → Belgeleri embed ederek vektör veritabanına aktarıyor.

rag_chat.py → RAG (Retrieval-Augmented Generation) mantığıyla chat arayüzünü çalıştırıyor.

data/ klasörü → Çeşitli PDF dökümanlar (NATO, MIL-STD, NIST, ISO, savunma sistemleri vb.) → bunlar RAG için bilgi tabanı.

.gradio/ klasörü → Flagged dataset dosyaları, demoda kullanılan gradio UI için.

Document Embedding: embedding.py ile PDF dokümanları vektör veritabanına embed eder.

RAG Chat Interface: rag_chat.py üzerinden Gradio tabanlı sohbet arayüzü sunar.

Knowledge Base: data/ klasörü içindeki standartlar (ISO, NIST, MIL-STD vb.) ve teknik dokümanlar anında sorgulanabilir.
