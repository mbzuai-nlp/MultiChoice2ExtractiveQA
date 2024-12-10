import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from primeqa.mitqa.metrics.evaluate import compute_exact, compute_f1
import argparse

# Download NLTK stopwords corpus if you haven't already
nltk.download('stopwords')
nltk.download('punkt')

# Setting up argument parsing
parser = argparse.ArgumentParser(description='Process input and output file paths.')
parser.add_argument('--input_file', type=str, required=True, help='Path to the input TSV file.')
parser.add_argument('--output_file', type=str, required=True, help='Path to save the output TSV file.')
parser.add_argument(
    '--language', 
    type=str, 
    choices=['arabic', 'english'], 
    required=True,
    help='Language used in the input TSV file. Choose between "arabic" or "english".'
)
args = parser.parse_args()

# Reading the input file path and output file path from arguments
input_file = args.input_file
output_file = args.output_file

# Load the input file into a DataFrame
df = pd.read_csv(input_file, sep="\t")

def remove_stopwords(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Get the Arabic stopwords
    stop_words = set(stopwords.words(args.language))
    
    # Filter out the stopwords
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the remaining words back into a string
    filtered_text = ' '.join(filtered_words)
    
    return filtered_text

# Apply the stopword removal function to the 'Reference' and 'Predection' columns
df['reference_no_stop_words'] = df['Reference'].apply(remove_stopwords)
df['prediction_no_stop_words'] = df['Predection'].apply(remove_stopwords)

# Function to compute F1 score
def f1_computation(row):
    return compute_f1(row['reference_no_stop_words'], row['prediction_no_stop_words'])

# Function to compute Exact match score
def exact_computation(row):
    return compute_exact(row['reference_no_stop_words'], row['prediction_no_stop_words'])

# Add F1 and Exact scores to new columns in the DataFrame
df['F1 Score_new'] = df.apply(f1_computation, axis=1)
df['Exact Score_new'] = df.apply(exact_computation, axis=1)

# Save the modified DataFrame to the output file
df.to_csv(output_file, sep='\t', index=False)
