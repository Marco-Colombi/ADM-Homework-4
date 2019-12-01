# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:15:47 2019

@author: marco
"""
def Counting_Sort(A):
    #finding the maximum value of A and
    #creating the auxiliary list
    Aux = [0]*(max(A)+1)
    for x in A:
        Aux[x] += 1
    #creating the sorted list
    sortedA = [0]*(len(A))
    j = 0
    for x in range(len(Aux)):
        while (Aux[x]) > 0:
            sortedA[j] += x 
            Aux[x] -= 1
            j += 1
    return sortedA

def Letters_Sort(letters):
    #defining the alphabet
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #creating the auxiliary array
    Aux = [0]*26
    for x in letters:
        Aux[alphabet.index(x)] += 1
    #creating the sorted array
    sortedA = [0] * len(letters)
    j = 0
    for x in range(len(Aux)):
        while (Aux[x]) > 0:
            sortedA[j] = (alphabet[x])
            Aux[x] -= 1
            j += 1
    return sortedA

#function that sorts the words in an alphabetical order
def Words_Sort(words):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #list with all the initial letters of our words
    initial_letters = [word[0] for word in words]
    #creating the auxilliary array
    Aux = [0] * 26
    for x in initial_letters:
        Aux[alphabet.index(x[0])] += 1
    j = 0
    #creating the sorted array
    sortedA = [0] * len(words)
    for x in range(len(Aux)):
        #we look for words which begin with the same letter
        if Aux[x] > 1:
            words2 = []
            for word in words: 
                if alphabet.index(word[0]) == x:
            #appending to words2 words which begin with the same letter
                    words2.append(word)
#looking for the next letters of the word in order to know how to sort them
            sortedA2 = Words_Sort2(words2, 1)
            for y in sortedA2:
                sortedA[j] = y
                j += 1
        else:
            #if a word is the only one which begins with a certain letters
            while Aux[x] > 0:
                for word in words:
                    #we append it to the sorting Array
                    if alphabet.index(word[0]) == x:
                        sortedA[j] = word
                        words.remove(word)
                        Aux[x] -= 1
                        j += 1
    return sortedA

#auxiliary functions that sort words by looking at the k-th letter 
def Words_Sort2(words, k):
    alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    j = 0
    #creating the sorted array
    sortedA = [0] * len(words)
    consecutive_letters = []
    for word in words:
        if len(word) != k: 
            consecutive_letters.append(word[k])
        #if the word doesn't have a k-th letter means that it's ended
        #so we can already append it to sorted array
        else:
            sortedA[j] = word
            j += 1
    #creating the auxiliary array
    Aux = [0] * 27 #we are considering also a white space as a letter
    for x in consecutive_letters:
        Aux[alphabet.index(x[0])] += 1
    for x in range(len(Aux)):
        #we look for words which have the same k-th letter
        if Aux[x] > 1:
            words2 = []
            for word in words: 
                if len(word) != k:
                    if alphabet.index(word[k]) == x:
             #appending to words2 words which have the same k-th letter
                        words2.append(word)
#looking for the next letters of the word in a recursive way in order to know how to sort them
            sortedA2 = Words_Sort2(words2, k + 1)
            for y in sortedA2:
                sortedA[j] = y
                j += 1
        else:
   #if a word is the only one which have a certain value of the k-th letter
            while Aux[x] > 0:
                for word in words:
                    if len(word) != k:
                    #we append it to the sorting Array
                        if alphabet.index(word[k]) == x:
                            sortedA[j] = word
                            words.remove(word)
                            Aux[x] -= 1
                            j += 1
    return sortedA
