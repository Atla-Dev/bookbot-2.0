from stats import count_words, get_char_count # type: ignore

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_count = get_char_count(text)
    print(f"{num_words} words found in the book")
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read() 
    
     
main()

