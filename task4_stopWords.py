from nltk.corpus import stopwords

def get_stopwords(language):
    try:
        # Retrieve stop words for the specified language
        stop_words = stopwords.words(language)
        return stop_words
    except OSError:
        print("Stopwords for '{}' are not available.".format(language))
        return []

# Example usage:
languages = ['english', 'spanish', 'french', 'german']

for lang in languages:
    print('-----------------------------------------------------------------')
    print("Common stop words in", lang.capitalize(), ":", get_stopwords(lang))
    print('-----------------------------------------------------------------')
