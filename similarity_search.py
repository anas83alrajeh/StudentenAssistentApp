import torch
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def filter_paragraphs(paragraphs, min_length=50):
    """
    Filtert Absätze heraus, die kürzer als min_length sind.
    """
    return [p for p in paragraphs if len(p) >= min_length]

def find_most_similar_paragraphs(question, paragraphs, top_k=3):
    """
    Gibt die top_k ähnlichsten Absätze zum Frage-Embedding zurück.
    Die Absätze werden mit doppeltem Zeilenumbruch verbunden zurückgegeben.
    """
    question_emb = model.encode(question, convert_to_tensor=True)
    paragraphs_emb = model.encode(paragraphs, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(question_emb, paragraphs_emb)[0]

    # Sicherstellen, dass similarities ein Tensor ist
    if not torch.is_tensor(similarities):
        similarities = torch.tensor(similarities)

    # Top-k ähnlichste Absätze holen
    top_results = torch.topk(similarities, k=min(top_k, len(paragraphs)))

    best_paragraphs = [paragraphs[idx] for idx in top_results.indices]
    return "\n\n".join(best_paragraphs)
