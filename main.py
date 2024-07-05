def main():
    frank_path = "./books/frankenstein.txt"
    print(fetch_book(frank_path))
    print(word_count(fetch_book(frank_path)))
    print(letter_totals(fetch_book(frank_path)))

def fetch_book(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def letter_totals(text):
    counts = dict()
    for letter in text:
        letter = letter.lower()  
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts
    
   
  

main()
