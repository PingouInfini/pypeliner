from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "A l’issue des discussions en Arabie saoudite, le président ukrainien Zelensky a dit que « l’Ukraine est prête pour la paix » et que Washington doit désormais « convaincre la Russie » d’accepter cette proposition. Les Etats-Unis ont également acté le retour de leur aide « en matière de sécurité » et de renseignements à Kiev."

ner_results = nlp(example)
print(ner_results)

for entity in ner_results:
    print(entity)
