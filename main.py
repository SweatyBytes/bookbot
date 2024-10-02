def main():
    book_contents = open_book() # run the count_words function, based on the output of open_book
    word_count = count_words(book_contents)  # Store the result
    print(f"Frankenstein book contains {word_count} words!")

def open_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def count_words(f):
    words = len(f.split())
    return words

# run main
main()