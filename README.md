# pypeliner

### prerequis

```
pip3 install -r requirements.txt
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
# spacy

Sur windows:

- Télécharge et installe Microsoft [Visual Studio Build Tools](https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/)
- Pendant l'installation, sélectionne :
  - Workload de développement desktop avec C++.
  - Assure-toi que C++ build tools et Windows 10 SDK sont cochés.

```
pip install --upgrade pip setuptools wheel
python -m spacy download fr_core_news_md
```

# Training data

https://huggingface.co/dslim/bert-base-NER

Abbreviation	Description
O	Outside of a named entity
B-MISC	Beginning of a miscellaneous entity right after another miscellaneous entity
I-MISC	Miscellaneous entity
B-PER	Beginning of a person’s name right after another person’s name
I-PER	Person’s name
B-ORG	Beginning of an organization right after another organization
I-ORG	organization
B-LOC	Beginning of a location right after another location
I-LOC	Location