# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 11/11/2018
# Lab 4 purpose: practice the use of Hash Tables

import time
from HashTable import HashTable, HashTableNode


# Function creates a Hash Table using words from a given file
def create_table(file_name):
    try:
        english_words = HashTable(5000)

        # Open file and read first line
        file = open(file_name, "r")
        line = file.readline()

        # Loop will go trough every line in the file
        while line:
            english_words.insert(line.rstrip())
            line = file.readline()

        # Returns Hash Table
        return english_words
    # Catches error when the given file does not exist
    except FileNotFoundError:
        print("File not found. Please try again.")


# Function that generates all possible permutations from a given word
def get_perms(word):
    if len(word) <= 1:
        return word
    else:
        perm_list = []
        for perm in get_perms(word[1:]):
            for i in range(len(word)):
                perm_list.append(perm[:i] + word[0:1] + perm[i:])
        return perm_list


# Function that returns the number of valid anagrams from a given word
def count_anagrams(word, table):
    permutations = get_perms(word)
    count = 0

    for i in range(len(permutations)):
        # Checks if permutation is a valid word
        if table.search(permutations[i]):
            count += 1

    return count


# Function returns the number of words inside a chain
def get_num_col(node):
    count = 0
    temp = node

    while temp is not None:
        count = count + 1
        temp = temp.next

    return count


# Returns the average number of comparisons needed to find a word in the Hash Table
def av_comparisons(table):
    num_of_cols = 0

    # Sums the middle point of every line in the hash table
    # because that is the average number of comparisons needed in that line
    for i in range(len(table.table)):
        num_of_cols = num_of_cols + get_num_col(table.table[i])//2

    # Dividing all the averages by the number of lines, gives the average number
    # of comparisons needed to find a number in the whole table
    return num_of_cols/len(table.table)


# Function returns the load factor of the Hash Table
def get_load_factor(table):

        num_elements = 0
        for i in range(len(table.table)):
            temp = table.table[i]

            # Loop counts number of elements per chain
            while temp is not None:
                num_elements = num_elements + 1
                temp = temp.next

        return num_elements / len(table.table)


# Main function
# It is asked to the user what operation he/she wishes to perform.
def main():
    file_name = input("Please enter the name of the file to generate a Hash Table:")
    keep_going = True
    start_time = time.time()
    hash_table = create_table(file_name)
    print("--- %s seconds ---" % (time.time() - start_time))

    if hash_table is not None:
        while keep_going:
            print("Please type the number of the operation you would like to perform:")
            print("   1. Get the average number of comparisons needed to perform a retrieve.")
            print("   2. Get the number of possible anagrams from a given word.")
            print("   3. Get the Load Factor for the Hash Table.")
            answer = input()

            if answer == '1':
                print("The average number of comparisons is:", av_comparisons(hash_table))
            elif answer == '2':
                word = input("Please type the word to search for anagrams: ")
                print("Number of possible anagrams for " + word + " is:", count_anagrams(word, hash_table))
            elif answer == '3':
                print("The Load Factor is:", get_load_factor(hash_table))
            else:
                print("You typed a non-supported command number.")

            loop = input("\nWould you like to perform a new operation? y/n\n")

            if loop == 'y':
                keep_going = True
            elif loop == 'n':
                keep_going = False
            else:
                print("You typed a non-supported command, please try again.")


main()