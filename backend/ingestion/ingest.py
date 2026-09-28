from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent
DOCUMENTS_DIR = BASE_DIR / "data" / "dummy_docs"
CHROMA_DIR = BASE_DIR / "vectorstore" / "chroma_db"


def load_documents(directory):
    documents = []

    for file_path in directory.glob("*.md"):
        content = file_path.read_text(encoding="utf-8")

        documents.append({
            "file_name": file_path.name,
            "content": content
        })

    return documents


def chunk_text(text, chunk_size=500):
    chunks = []

    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size].strip()

        if chunk:
            chunks.append(chunk)

    return chunks


def create_chunks(documents):
    all_chunks = []

    for document in documents:
        chunks = chunk_text(document["content"])

        for chunk in chunks:
            all_chunks.append({
                "file_name": document["file_name"],
                "content": chunk
            })

    return all_chunks


def create_chroma_client():
    client = chromadb.PersistentClient(
        path=str(CHROMA_DIR)
    )

    return client


def get_collection(client):
    collection = client.get_or_create_collection(
        name="deltarag_documents"
    )

    return collection


def prepare_chroma_data(chunks):
    documents = []
    ids = []
    metadatas = []

    for index, chunk in enumerate(chunks):
        documents.append(chunk["content"])
        ids.append(f"chunk_{index}")

        metadatas.append({
            "file_name": chunk["file_name"]
        })

    return documents, ids, metadatas


def main():
    documents = load_documents(DOCUMENTS_DIR)
    print(f"Documents loaded: {len(documents)}")

    all_chunks = create_chunks(documents)
    print(f"Chunks created: {len(all_chunks)}")

    client = create_chroma_client()
    print("ChromaDB client created successfully.")

    collection = get_collection(client)
    print("ChromaDB collection created successfully.")

    documents, ids, metadatas = prepare_chroma_data(all_chunks)

    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    print("Chunks added to ChromaDB successfully.")
    
    result = collection.get()
    print(result)


if __name__ == "__main__":
    main()