from logging_utils import setup_logger
import logging

def main():
    setup_logger()  # Initialiseer de logger
    # logging.info("Starting the Frankenstein word count program")
    
    try:
        # start report
        print("--- Begin report of books/frankenstein.txt ---")

        # start count word function
        book_contents = open_book() # run the count_words function, based on the output of open_book
        word_count = count_words(book_contents) # Store the result
        # logging.info(f"{word_count} words found in the document")
        print(f"{word_count} words found in the document\n")

        # start count character function
        book_contents = open_book()
        char_count_list = char_count(book_contents)
        char_count_list.sort(reverse=True, key=lambda x: x['count'])
        for char_dict in char_count_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
            # logging.info(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
        
        # end report
        print("--- End report ---")

    
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
        if 'a' <= lower_character <= 'z':  # Character is a lowercase letter, can also use isalpha() function?
            if lower_character in char_dict:
                char_dict[lower_character] += 1  # Increment the count if it exists
            else:
                char_dict[lower_character] = 1  # Initialize the count
    
    char_list = [] # new list
    for char, count in char_dict.items(): # bekijk iedere entry in dictionary als twee tuples (key en value)
        char_list.append({"char": char, "count": count}) # voeg de entry toe als apart list object
    
    return char_list # return the list

# run main
main()