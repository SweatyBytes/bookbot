from logging_utils import setup_logger
import logging

def main():
    setup_logger()  # Initialiseer de logger
    logging.info("Starting the Frankenstein word count program")
    
    try:
        # start count word function
        book_contents = open_book() # run the count_words function, based on the output of open_book
        word_count = count_words(book_contents) # Store the result
        logging.info(f"Frankenstein book contains {word_count} words!")
        print(f"Frankenstein book contains {word_count} words!")

        # start count character function
        book_contents = open_book()
        amount_of_characters = char_count(book_contents)
        logging.info(f"Frankenstein book contains this amount of characters: {amount_of_characters}")
        print(f"Frankenstein book contains this amount of characters: {amount_of_characters}")
    
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print("Oops, something went wrong. Check the log file for details.")

# function to create a long string based on the contents of a file
def open_book():
    with open("books/frankenstein.txt") as bookfile:
        file_contents = bookfile.read()
        return file_contents

# function to count the amount of words within the book
def count_words(f):
    words = len(f.split())
    return words

# function to count all the different characters within the book, e.g. a = 3934, b = 8325, etc.
def char_count(booktext):
    char_dict = {}  # Create an empty character-count dictionary
    for character in booktext:  # Iterate over each character in the supplied string
        lower_character = character.lower()  # Lowercase each character
        if 'a' <= lower_character <= 'z':  # Character is a lowercase letter
            if lower_character in char_dict:
                char_dict[lower_character] += 1  # Increment the count if it exists
            else:
                char_dict[lower_character] = 1  # Initialize the count
    return char_dict

# run main
main()