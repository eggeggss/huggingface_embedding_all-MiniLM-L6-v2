from sentence_transformers import SentenceTransformer

def get_embedding_from_hugginface(text: str):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return model.encode(text)

if __name__== "__main__":
    query_text = "高頻率晶體振盪器"
    query_embedding = get_embedding_from_hugginface(query_text)
    print(query_embedding)

