from logging_utils import setup_logger
import logging

def main():
    setup_logger()  # Initialiseer de logger
    logging.info("Starting the Frankenstein word count program")
    
    try:
        book_contents = open_book() # run the count_words function, based on the output of open_book
        word_count = count_words(book_contents) # Store the result
        logging.info(f"Frankenstein book contains {word_count} words!")
        print(f"Frankenstein book contains {word_count} words!")
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print("Oops, something went wrong. Check the log file for details.")

def open_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def count_words(f):
    words = len(f.split())
    return words

# Add a new function to your script that takes the text from the book
# as a string, and returns the number of times each character appears
# in the string. Convert any character to lowercase, we don't want duplicates.

# functie nog nader uitwerken.
# def char_count(booktext):


# run main
main()