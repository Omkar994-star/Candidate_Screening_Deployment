from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    PyPDFLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ============================================================
# 1. Load knowledge base
# ============================================================

KNOWLEDGE_BASE = "rag/knowledge_base/Python Developer"

md_loader = DirectoryLoader(
    KNOWLEDGE_BASE,
    glob="**/*.md",
    loader_cls=TextLoader,
    loader_kwargs={
        "encoding": "utf-8",
        "autodetect_encoding": True
    }
)

pdf_loader = DirectoryLoader(
    KNOWLEDGE_BASE,
    glob="**/*.pdf",
    loader_cls=PyPDFLoader
)

documents = md_loader.load() + pdf_loader.load()

print("Documents:", len(documents))


# ============================================================
# 2. Split documents
# ============================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print("Chunks:", len(chunks))


# ============================================================
# 3. Hugging Face BGE-small embeddings
# ============================================================

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={
        "device": "cpu"
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)


# ============================================================
# 4. Create FAISS in batches
# ============================================================

BATCH_SIZE = 100

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


# ============================================================
# 5. Save FAISS database
# ============================================================

VECTOR_DB_PATH = "vector_db/Python Developer"

vector_db.save_local(VECTOR_DB_PATH)

print("FAISS vector database created successfully!")
print(f"Saved at: {VECTOR_DB_PATH}")