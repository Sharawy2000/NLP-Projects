import spacy
# from spacy import a

def pos_tagging(text, model_name='en_core_web_sm', tagset='universal'):
    nlp = spacy.load(model_name)
    doc = nlp(text)
    if tagset == 'universal':
        return [(token.text, token.pos_) for token in doc]
    elif tagset == 'penn_treebank':
        return [(token.text, token.tag_) for token in doc]
    else:
        raise ValueError("Invalid tagset. Supported tagsets are 'universal' and 'penn_treebank'.")

# Example text
text = "This is a sample sentence."

# Part-of-speech tagging with different tagsets
universal_tags = pos_tagging(text, tagset='universal')
penn_tags = pos_tagging(text, tagset='penn_treebank')

# Print the results
print("Universal Tagset:")
for word, tag in universal_tags:
    print(f"{word}: {tag}")

print("\nPenn Treebank Tagset:")
for word, tag in penn_tags:
    print(f"{word}: {tag}")

