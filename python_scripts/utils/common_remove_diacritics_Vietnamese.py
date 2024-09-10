import unicodedata
def remove_diacritics(text):
    # Normalize the text to NFD (Normalization Form Decomposed)
    normalized_text = unicodedata.normalize('NFD', text)
    
    # Filter out diacritical marks (accents) using a generator expression
    text_without_diacritics = ''.join(
        char for char in normalized_text if unicodedata.category(char) != 'Mn'
    )
    
    # Normalize the result back to NFC
    return unicodedata.normalize('NFC', text_without_diacritics)