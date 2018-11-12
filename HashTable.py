# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 11/11/2018
# Lab 4 purpose: practice the use of Hash Tables


# Hash Table Node class
class HashTableNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next


# Hash Table class
class HashTable:

    def __init__(self, table_size):
        self.table = [None] * table_size

    # hashing function
    def hash(self, word):
        lower_case_word = word.lower()
        sum = 0
        # Adds values for each letter in a word to
        # store anagrams in the same chain
        for i in range(len(lower_case_word)):
            sum = sum + ord(lower_case_word[i])

        return sum % len(self.table)

    # Inserts new words in the Hash Table
    def insert(self, word):
        loc = self.hash(word)
        if self.table[loc] is None:
            self.table[loc] = HashTableNode(word.lower(), None)
        else:
            self.table[loc] = HashTableNode(word.lower(), self.table[loc])

    # Searches for words in the Hash Table
    def search(self, k):
        loc = self.hash(k)

        temp = self.table[loc]

        while temp is not None:
            if temp.item == k:
                return True

            temp = temp.next

        return False
