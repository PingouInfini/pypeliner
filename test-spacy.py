import spacy

# Charger le modèle français pré-entraîné
nlp = spacy.load("fr_core_news_md")

# Texte en français
texte = "Emmanuel Macron est le président de la France, et il a rencontré Angela Merkel à Berlin."

# Traiter le texte avec le modèle
doc = nlp(texte)

# Extraire et afficher les entités nommées
for ent in doc.ents:
    print(ent.text, ent.label_)
