import spacy

def tokenize_text(text, language):
    nlp = spacy.blank(language)
    nlp.add_pipe("sentencizer")
    doc = nlp(text)
    return [sent.text for sent in doc.sents]

# Example text in French
text=str(input("\nEnter your text2 input : "))


# Tokenize the text into sentences using French language model
sentences = tokenize_text(text, language='en')

# Print the tokenized sentences
for sentence in sentences:
    print(sentence)
