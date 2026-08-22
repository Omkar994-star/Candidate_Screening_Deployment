from functools import lru_cache

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.screening_config import VECTOR_DB_ROOT


# Same model used when creating the FAISS vector database
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={
        "device": "cpu"
    },
    encode_kwargs={
        "normalize_embeddings": True
    }
)


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


def retrieve_knowledge(
    search_queries,
    role: str,
    k: int = 5
):

    db = get_vector_db(role)

    unique_docs = {}
    results_per_query = []

    for query in search_queries:

        results = db.similarity_search_with_score(
            query,
            k=k
        )

        results_per_query.extend(results)

    # Remove duplicate chunks
    for document, score in results_per_query:

        content = document.page_content.strip()

        # FAISS similarity_search_with_score:
        # Lower score generally means more similar
        if content not in unique_docs:
            unique_docs[content] = (
                document,
                score
            )

    # Sort by relevance
    sorted_results = sorted(
        unique_docs.values(),
        key=lambda x: x[1]
    )

    return [
        document
        for document, score in sorted_results
    ]