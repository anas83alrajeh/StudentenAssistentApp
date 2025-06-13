from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def filter_paragraphs(paragraphs, min_length=50):
    return [p for p in paragraphs if len(p) >= min_length]

def find_most_similar_paragraphs(question, paragraphs, top_k=3):
    question_emb = model.encode(question, convert_to_tensor=True)
    paragraphs_emb = model.encode(paragraphs, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(question_emb, paragraphs_emb)[0]
    top_results = similarities.topk(k=top_k)
    best_paragraphs = [paragraphs[idx] for idx in top_results.indices]
    return "\n\n".join(best_paragraphs)
