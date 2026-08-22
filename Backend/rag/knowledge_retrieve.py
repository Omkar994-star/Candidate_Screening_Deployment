from functools import lru_cache

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.screening_config import VECTOR_DB_ROOT


# ============================================================
# BGE-small embeddings
# Must be the SAME model used to create the FAISS databases
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
# Load vector database for a role
# ============================================================

@lru_cache(maxsize=None)
def get_vector_db(role: str) -> FAISS:

    vector_db_path = VECTOR_DB_ROOT / role

    if (
        not vector_db_path.is_dir()
        or not (vector_db_path / "index.faiss").is_file()
        or not (vector_db_path / "index.pkl").is_file()
    ):
        raise ValueError(
            f"No vector database is available for role: {role}"
        )

    return FAISS.load_local(
        str(vector_db_path),
        embeddings,
        allow_dangerous_deserialization=True
    )


# ============================================================
# Retrieve knowledge
# ============================================================

def retrieve_knowledge(
    search_queries,
    role: str,
    k: int = 5
):

    db = get_vector_db(role)

    docs = []

    for query in search_queries:

        results = db.similarity_search(
            query,
            k=k
        )

        docs.extend(results)

    return docs