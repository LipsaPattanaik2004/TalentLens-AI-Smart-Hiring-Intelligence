from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def similarity(text1, text2):
    return util.cos_sim(model.encode(text1), model.encode(text2)).item()
