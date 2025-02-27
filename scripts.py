import re
import os
import socket
from collections import Counter

def process_text_files(data_dir, output_file):
    if1_path = os.path.join(data_dir, "IF-1.txt")
    always_path = os.path.join(data_dir, "AlwaysRememberUsThisWay-1.txt")

    if not os.path.exists(if1_path) or not os.path.exists(always_path):
        raise FileNotFoundError("One or both input files not found.")

    def clean_and_count_words(file_path):
        with open(file_path, 'r') as f:
            content = f.read().lower()

        # Replace em-dashes and en-dashes with spaces
        content = re.sub(r"[\u2013\u2014]", " ", content)
        
        # Remove punctuation: ",", "!", ":", ";", "."
        content = re.sub(r'[,\.!;:"]', '', content)

        words = content.split()

        return len(words), words
    
    if1_word_count, if1_words = clean_and_count_words(if1_path)
    if1_word_counts = Counter(if1_words)
    if1_top_3 = if1_word_counts.most_common(3)

    always_word_count, always_words = clean_and_count_words(always_path)

    grand_total_words = if1_word_count + always_word_count

    def expand_contractions(text):
        contractions = {
            "won't": "will not", "can't": "can not", "shan't": "shall not", "n't": " not", "'re": " are",
            "'s": " is", "'m": " am", "'ll": " will", "'ve": " have", "'d": " would", "'t": " not"
        }
        for contraction, expanded in contractions.items():
            text = re.sub(contraction, expanded, text)
        return text

    always_content = " ".join(always_words)
    always_content_expanded = expand_contractions(always_content)
    always_words_expanded = always_content_expanded.split()
    always_word_counts_expanded = Counter(always_words_expanded)
    always_top_3 = always_word_counts_expanded.most_common(3)

    # IP address
    ip_address = socket.gethostbyname(socket.gethostname())

    # Write results to file
    with open(output_file, 'w') as f:
        f.write(f"IF-1.txt word count: {if1_word_count}\n")
        f.write(f"AlwaysRememberUsThisWay-1.txt word count: {always_word_count}\n")
        f.write(f"Grand total word count: {grand_total_words}\n")
        f.write(f"IF-1.txt top 3 words: {if1_top_3}\n")
        f.write(f"AlwaysRememberUsThisWay-1.txt top 3 words (with contractions expanded): {always_top_3}\n")
        f.write(f"Container IP address: {ip_address}\n")
        
    # Print results to console
    with open(output_file, 'r') as f:
        print(f.read())


if __name__ == "__main__":
    data_dir = "/home/data"
    output_file = os.path.join(data_dir, "output", "result.txt")
    process_text_files(data_dir, output_file)