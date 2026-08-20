# ==========================================================
from pathlib import Path


VECTOR_DB_ROOT = Path(__file__).resolve().parents[2] / "vector_db"


def get_available_roles() -> list[str]:
	"""Return roles whose vector database has been created."""
	if not VECTOR_DB_ROOT.exists():
		return []

	return sorted(
		directory.name
		for directory in VECTOR_DB_ROOT.iterdir()
		if directory.is_dir() and (directory / "index.faiss").is_file()
	)


def is_available_role(role: str) -> bool:
	return role in get_available_roles()


# Number of questions generated for each interview

TOTAL_QUESTIONS = 10