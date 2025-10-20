import re

def read_paragraph() -> str:
    
    print("Paste your paragraph. Press ENTER on an empty line to finish:\n")
    
    lines = []
    
    while True:
        
        try:
            
            line = input()
        
        except EOFError:
            
            break
        
        if line.strip() == "":
            
            # blank line ends input
            
            break
        
        lines.append(line)
    
    return "\n".join(lines).strip()

def split_sentences(text: str):

# keeps decimal points and abbreviations intact

# uses regex to split on sentence-ending punctuation
    
    text = text.strip()

    if not text:
        
        return []

    # Splits on sentence ending punctuation 
    
    parts = re.split(r'(?<=[.!?])\s+', text)

    sentences = []
    
    for part in parts:
        
        
        part = part.strip()
        
        if part:
            
            sentences.append(part)

    return sentences

def main():
    
    paragraph = read_paragraph()
    
    sentences = split_sentences(paragraph)

    if not sentences:
        
        print("\nNo sentences found.")
        
        return

    print("\nIndividual sentences:")
    
    for i, s in enumerate(sentences, start=1):
        
        print(f"{i}. {s}")

    print(f"\nTotal sentences: {len(sentences)}")

if __name__ == "__main__":
    
    main()