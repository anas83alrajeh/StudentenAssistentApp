from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def find_most_similar_paragraph(question, paragraphs):
    question_emb = model.encode(question, convert_to_tensor=True)
    paragraphs_emb = model.encode(paragraphs, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(question_emb, paragraphs_emb)[0]
    best_idx = similarities.argmax()
    return paragraphs[best_idx]