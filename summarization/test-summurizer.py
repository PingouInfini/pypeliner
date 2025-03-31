from transformers import pipeline

# Charger un modèle de résumé en français (T5, BART)
summarizer = pipeline("summarization", model="facebook/mbart-large-50-many-to-many-mmt", tokenizer="facebook/mbart-large-50-one-to-many-mmt")

# Fonction pour lire un fichier texte
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Diviser le texte en segments pour le traitement
def split_text(text, max_length=1024):
    sentences = text.split('. ')
    current_chunk = []
    current_length = 0
    chunks = []

    for sentence in sentences:
        sentence_length = len(sentence.split())
        if current_length + sentence_length <= max_length:
            current_chunk.append(sentence)
            current_length += sentence_length
        else:
            chunks.append(". ".join(current_chunk) + ".")
            current_chunk = [sentence]
            current_length = sentence_length

    if current_chunk:
        chunks.append(". ".join(current_chunk) + ".")

    return chunks

# Charger et traiter le fichier texte
file_path = "doc.txt"  # Nom du fichier texte contenant les données à résumer
texte = read_text_file(file_path)

# Diviser le texte en segments si trop long
chunks = split_text(texte)

# Résumer chaque segment
summaries = [summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]

# Combiner les résumés
summary = " ".join(summaries)
print(summary)
