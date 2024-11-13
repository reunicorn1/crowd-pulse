import contractions
import emoji
import re
import string
import nltk
import spacy
from nltk.corpus import stopwords
import pandas as pd
import argparse

# Download NLTK stopwords
nltk.download('stopwords')

# Download spaCy model
spacy.cli.download("en_core_web_sm")

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def expand_contractions(text):
    """
    Expands contractions in the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The text with expanded contractions.

    Example:
        >>> expand_contractions("I'm learning NLP.")
        'I am learning NLP.'
    """
    try:
        return contractions.fix(text)
    except Exception as e:
        print(f"Error expanding contractions in text: {text}")
        print(f"Exception: {e}")
        return text

def convert_emojis(text):
    """
    Converts emojis in the input text to their text representation.

    Args:
        text (str): The input text.

    Returns:
        str: The text with emojis converted to text.

    Example:
        >>> convert_emojis("I love Python! 😊")
        'I love Python! :smiling_face_with_smiling_eyes:'
    """
    try:
        return emoji.demojize(text)
    except Exception as e:
        print(f"Error converting emojis in text: {text}")
        print(f"Exception: {e}")
        return text

def to_lowercase(text):
    """
    Converts the input text to lowercase.

    Args:
        text (str): The input text.

    Returns:
        str: The text in lowercase.

    Example:
        >>> to_lowercase("Hello World!")
        'hello world!'
    """
    try:
        return text.lower()
    except Exception as e:
        print(f"Error converting text to lowercase: {text}")
        print(f"Exception: {e}")
        return text

def remove_special_characters(text):
    """
    Removes special characters from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The text without special characters.

    Example:
        >>> remove_special_characters("Hello, World!")
        'Hello World'
    """
    try:
        pattern = re.compile(f'[{re.escape(string.punctuation)}]')
        return pattern.sub('', text)
    except Exception as e:
        print(f"Error removing special characters from text: {text}")
        print(f"Exception: {e}")
        return text

def remove_stopwords(text):
    """
    Removes stopwords from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The text without stopwords.

    Example:
        >>> remove_stopwords("This is a sample sentence.")
        'This sample sentence.'
    """
    try:
        stop_words = set(stopwords.words('english'))
        return ' '.join([word for word in text.split() if word.lower() not in stop_words])
    except Exception as e:
        print(f"Error removing stopwords from text: {text}")
        print(f"Exception: {e}")
        return text

def lemmatize_text(text):
    """
    Lemmatizes the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The lemmatized text.

    Example:
        >>> lemmatize_text("The striped bats are hanging on their feet for best.")
        'the stripe bat be hang on their foot for good'
    """
    try:
        doc = nlp(text)
        return ' '.join([token.lemma_ for token in doc])
    except Exception as e:
        print(f"Error lemmatizing text: {text}")
        print(f"Exception: {e}")
        return text

def remove_duplicates(text):
    """
    Removes duplicate words from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The text without duplicate words.

    Example:
        >>> remove_duplicates("This is is a test test.")
        'This is a test'
    """
    try:
        words = text.split()
        seen = set()
        result = []
        for word in words:
            if word not in seen:
                seen.add(word)
                result.append(word)
        return ' '.join(result)
    except Exception as e:
        print(f"Error removing duplicates from text: {text}")
        print(f"Exception: {e}")
        return text

def clean_text(text, steps=None):
    """
    Cleans the input text by applying a series of text preprocessing steps.

    Args:
        text (str): The input text to be cleaned.
        steps (list): A list of steps to apply. If None, applies all steps. Default is None.

    Returns:
        str: The cleaned text.

    Example:
        >>> clean_text("I'm learning NLP! 😊", steps=['contractions', 'emojis', 'lowercase'])
        'i am learning nlp! :smiling_face_with_smiling_eyes:'
    """

    if not text:
        return text

    if steps is None:
        steps = ['contractions', 'emojis', 'lowercase', 'special_characters', 'stopwords', 'lemmatization', 'duplicates']

    try:
        if 'contractions' in steps:
            text = expand_contractions(text)
        if 'emojis' in steps:
            text = convert_emojis(text)
        if 'lowercase' in steps:
            text = to_lowercase(text)
        if 'special_characters' in steps:
            text = remove_special_characters(text)
        if 'stopwords' in steps:
            text = remove_stopwords(text)
        if 'lemmatization' in steps:
            text = lemmatize_text(text)
        # if 'duplicates' in steps:
        #     text = remove_duplicates(text)
    except Exception as e:
        print(f"Error cleaning text: {text}")
        print(f"Exception: {e}")
        return text

    return text

# Function to clean and save a CSV file
def clean_csv_file(input_filepath, output_filepath):
    # Read the CSV file
    df = pd.read_csv(input_filepath, header=None, names=['subreddit', 'post_id', 'post_title', 'post_score', 'post_url', 'post_comms_num', 'post_body', 'post_timestamp'])
    # print the first line of the CSV file
    # print("First line of the CSV file:")
    # print(df.head(1))
    df = df.dropna(subset=['post_body'])
    df = df.dropna(subset=['post_title'])
    # Apply the clean_text function to the 'comment_text' column
    df['post_body'] = df['post_body'].apply(clean_text)
    df['post_title'] = df['post_title'].apply(clean_text)

    # Save the cleaned data to a new CSV file
    df.to_csv(output_filepath, index=False)
    print(f"Processed {input_filepath} and saved to {output_filepath}")

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Clean text data in a CSV file.')
    parser.add_argument('input_file', type=str, help='The input CSV file to be cleaned.')
    parser.add_argument('output_file', type=str, help='The output CSV file to save the cleaned data.')

    args = parser.parse_args()

    clean_csv_file(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
