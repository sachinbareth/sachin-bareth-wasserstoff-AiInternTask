import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK data: 'punkt' for sentence tokenization and 'stopwords' for keyword filtering
nltk.download('punkt')
nltk.download('stopwords')

# Function to generate a summary of the input text
def summarize_text(text):
    # Split the text into sentences
    sentences = sent_tokenize(text)
    
    # If the text contains fewer than 10 sentences, return the entire text as the summary
    if len(sentences) < 10:
        return " ".join(sentences)
    
    # Otherwise, return the first 5 sentences as the summary
    return " ".join(sentences[:5])

# Function to extract keywords from the input text
def extract_keywords(text):
    # Load the set of English stopwords
    stop_words = set(stopwords.words("english"))
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Filter out stopwords and non-alphanumeric words
    keywords = [word for word in words if word.isalnum() and word.lower() not in stop_words]
    
    # Return the top 10 keywords (or fewer, if less than 10 are found)
    return keywords[:10]
