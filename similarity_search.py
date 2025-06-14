from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_most_similar_paragraphs(question, paragraphs, top_k=3):
    if not paragraphs:
        return "Keine Inhalte gefunden."  # لا توجد فقرات

    if len(paragraphs) < top_k:
        top_k = len(paragraphs)

    question_emb = model.encode(question, convert_to_tensor=True)
    paragraphs_emb = model.encode(paragraphs, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(question_emb, paragraphs_emb)[0]
    top_results = similarities.topk(top_k)
    top_paragraphs = [paragraphs[idx] for idx in top_results.indices]
    return "\n\n".join(top_paragraphs)
