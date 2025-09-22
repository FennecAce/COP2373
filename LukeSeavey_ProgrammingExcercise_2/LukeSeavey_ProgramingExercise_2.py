# importing regular expressions library

import re

# import a counter to simplify counting occurrences

from collections import Counter

# Data: 30 common spam words/phrases

# dictionary of spam words

SPAM_WORDS = {
    
    # 20 single words (1 point each)
    
    "free", "winner", "win", "urgent", "prize", "cash", "bonus", "deal",
    
    "discount", "offer", "trial", "guarantee", "crypto", "bitcoin",
    
    "lottery", "bank", "wire", "investment", "password", "unsubscribe"
}

# dictionary of spam phrases

SPAM_PHRASES = {
    
    # 10 multi-word phrases (2 points each)
    
    "limited time",
    
    "act now",
    
    "click here",
    
    "risk free",
    
    "money back",
    
    "no obligation",
    
    "verify your account",
    
    "update your account",
    
    "urgent response",
    
    "claim your prize",
}

# setting weights for scoring

WORD_WEIGHT   = 1

PHRASE_WEIGHT = 2  # phrases should carry higher weight than single words

# Utilities

# normaliz text for ease of processing

def normalize(text: str):
    
    # Lowercase and collapse whitespace; keep letters/numbers/spaces only. ###
    
    text = text.lower()
    
    # replace any non-alphanumeric characters with spaces
    
    text = re.sub(r"[^a-z0-9]+", " ", text)
    
    return re.sub(r"\s+", " ", text).strip()

def tokenize(text: str):
    
    # whitespace tokenizer after normalization.
    
    return normalize(text).split()

# Phrase scanning

# check for phrases in text for flaged phases from spam phrases dictionary

def check_phrase_counts(text: str, phrases: set[str]):
    
    # Count occurrences of each phrase in text using word-boundary regex. 
    
    # Returns a Counter 
    
    counts = Counter()
    
    # Work with a normalized, spaced out version of the text
    
    padded = f" {normalize(text)} "
    
    for ph in phrases:
        
        # Build a word-boundary pattern for the phrase (spaces -> \s+)
        
        words = ph.split()
        
        pattern = r"\b" + r"\s+".join(map(re.escape, words)) + r"\b"
        
        hits = re.findall(pattern, padded)
        
        if hits:
            
            counts[ph] = len(hits)
    
    return counts

# Word scanning 

def scan_text_for_words(text: str, vocab: set[str]):
    
    # Count occurrences of each spam WORD in the message. 
    
    # Returns a Counter mapping word - count. 
    
    counts = Counter()
    
    tokens = tokenize(text)
    
    for tok in tokens:
        
        if tok in vocab:
            
            counts[tok] += 1
    
    return counts

# Score + decision

def compute_spam_score(word_counts: Counter, phrase_counts: Counter):
    
    # Combine weighted counts to produce a total spam score. 
    
    word_points = sum(word_counts.values()) * WORD_WEIGHT
    
    phrase_points = sum(phrase_counts.values()) * PHRASE_WEIGHT
    
    return word_points + phrase_points


def likelihood_label(score: int):
    
    # Maps score 
    
    # These can be tweaked to be stricter/looser. 
    
    if score <= 2:
        
        return "Low likelihood of spam"
    
    elif score <= 5:
        
        return "Moderate likelihood of spam"
    
    elif score <= 9:
        
        return "High likelihood of spam"
    
    else:
        
        return "Very high likelihood of spam"

# Orchestrator

def analyze_email(email_message: str):
    
    # Main handler: scan words, scan phrases, compute score, labels likelihood. 
    
    # Returns a dict with everything needed for display/reporting. 
    
    word_counts   = scan_text_for_words(email_message, SPAM_WORDS)
    
    phrase_counts = check_phrase_counts(email_message, SPAM_PHRASES)
    
    score         = compute_spam_score(word_counts, phrase_counts)
    
    label         = likelihood_label(score)

    # Build a flat list of which items caused points
    
    triggers = []
    
    for w, c in word_counts.items():
        
        triggers.append((w, c, WORD_WEIGHT))
    
    for p, c in phrase_counts.items():
        
        triggers.append((p, c, PHRASE_WEIGHT))

    # Sort by total contribution (count * weight), desc
    
    triggers.sort(key=lambda t: t[1] * t[2], reverse=True)

    return {
        
        "score": score,
        
        "label": label,
        
        "word_counts": word_counts,
        
        "phrase_counts": phrase_counts,
        
        "triggers": triggers,
    }

# CLI entry point

def main():
    
    print("=== Email Spam Scanner ===")
    
    email_message = input("Paste the email text and press Enter:\n> ")

    result = analyze_email(email_message)

    print("\n--- Results ---")
    
    print(f"Spam score: {result['score']}")
    
    print(f"Likelihood: {result['label']}")

    # Display flagged words/phrases if any
    
    if result["triggers"]:
                
        print("\nFlagged words/phrases (item | matches × weight = points):")
        
        for item, count, weight in result["triggers"]:
            
            points = count * weight
            
            kind = "phrase" if " " in item else "word"
            
            print(f"  - [{kind}] {item!r}: {count} × {weight} = {points}")
    else:
        
        print("\nNo spam words or phrases were detected.")

# Calls main function

if __name__ == "__main__":
    
    main()
