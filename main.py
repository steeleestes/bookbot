def main():
    frank_path = "./books/frankenstein.txt"
    #print(fetch_book(frank_path))
    #print(word_count(fetch_book(frank_path)))
    #print(letter_totals(fetch_book(frank_path)))
    book_report(fetch_book(frank_path))


def fetch_book(path):
    with open(path) as f:
        return f.read()

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
    
def book_report(text):
    ltr_cnt = letter_totals(text)
    #print("debug - ltr_cnt: ", ltr_cnt)
    wrd_cnt = word_count(text)
    #print("debug - wrd_cnt: ", wrd_cnt)
    out_L = list()
    for i in ltr_cnt:
        out_L.append({'char': i, 'num': ltr_cnt[i]})
    out_L = sorted(out_L, reverse=True, key=lambda x: x['num'])
    print("--- Begin Report ---")
    print(f"There are {word_count(text)} words in the book")
    for e in out_L:
        print(f"Char: {e} was found {e['num']} times.")
    print("--- End of report ---")



main()
