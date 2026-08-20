from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


# 1. Load knowledge base

md_loader = DirectoryLoader(
    "rag/knowledge_base/Advanced or Theoretical ML",
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={
        "encoding": "utf-8",
        "autodetect_encoding": True
    }
)


pdf_loader = DirectoryLoader(
    "rag/knowledge_base/Advanced or Theoretical ML",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

documents = md_loader.load() + pdf_loader.load()

print("Documents:", len(documents))


# 2. Split documents

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print("Chunks:", len(chunks))


embeddings = OllamaEmbeddings(
    model="mxbai-embed-large:latest",
    base_url="http://127.0.0.1:11434"
)

BATCH_SIZE = 50

vector_db = None

for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i + BATCH_SIZE]

    print(
        f"Embedding chunks {i + 1} "
        f"to {min(i + BATCH_SIZE, len(chunks))} "
        f"of {len(chunks)}"
    )

    if vector_db is None:
        vector_db = FAISS.from_documents(
            batch,
            embeddings
        )
    else:
        batch_db = FAISS.from_documents(
            batch,
            embeddings
        )

        vector_db.merge_from(batch_db)

vector_db.save_local(
    "vector_db/Advanced or Theoretical ML"
)

print("FAISS vector database created successfully")