# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 02:58:26 2019

@author: marco
"""
import time
from bitarray import bitarray
import numpy as np
import math

#function that computes the number of hash functions
#given a certain value of probability
def number_hash_functions(p):
    return int(round(-np.log(p)/np.log(2)))

#function that computes the number of bits of the bloom filter
#given a certain value of probability and the number of elements
#that have to go in the Bloom Filter
def number_bits(n, p):
    return int(round(-(n*np.log(p)/((np.log(2))**2))))

#function that computes the module of the division between a certain key
#and the length of the bloom filter
def hash_mod_key(key, hash_l):
    return key % len(hash_l)

#function that computes the module of the division between a certain key
#and the floor of the squared root of the length of the bloom filter
def hash_mod_key2(key, hash_l):
    return key % math.floor(math.sqrt(len(hash_l)))

#function that computes 11 hash values four our Bloom filter taking as core 
#a module hash function that takes the sum as strings of the 
#Unicode code points of each Unicode character of the password 
#(using the ord() method) for what we are computing the hash values
#multiplicated for their positions inside the word
def hash_functions(hash_l, string):
    sum_str = str(ord(string[0])*(1))
    for i in range(1, len(string)):
        sum_str += str(ord(string[i])*(i+1))
    sum_hash = int(sum_str)
    #then we recall the two modules function using as parameters different 
    #values each time of the sum_hash value
    hash_key1 = hash_mod_key(sum_hash, hash_l)
    hash_key2 = hash_mod_key(sum_hash//2, hash_l)
    hash_key3 = hash_mod_key2(sum_hash//2, hash_l)
    hash_key4 = hash_mod_key(sum_hash**2, hash_l)
    hash_key5 = hash_mod_key(sum_hash*2, hash_l)
    hash_key6 = hash_mod_key2(sum_hash*(2**16), hash_l)
    hash_key7 = hash_mod_key(math.floor(math.sqrt(sum_hash)), hash_l)
    hash_key8 = hash_mod_key2(sum_hash, hash_l)
    hash_key9 = hash_mod_key2(sum_hash*2, hash_l)
    hash_key10 = hash_mod_key2(math.floor(math.sqrt(sum_hash)), hash_l)
    hash_key11 = hash_mod_key2(sum_hash**2, hash_l)
    return hash_key1, hash_key2, hash_key3, hash_key4, hash_key5, hash_key6, hash_key7, hash_key8, hash_key9,  hash_key10, hash_key11

#Function that performs the Bloom Filter
def Bloom_Filter(passwords1, passwords2):
    start = time.time()
    pool = 100000000
    p = 0.0005
    k = number_hash_functions(p) #computing the number of hash values
    #Creating the bits of our Bloom Filter
    bloom_tables = bitarray(1582028303) 
    bloom_tables.setall(0)
    #Inserting the passwords1 in the Bloom Filter
    for passw in passwords1:
        hash_keys = list(hash_functions(bloom_tables, passw))
        for key in hash_keys:
            #switching to 1 all the bits coming from the hash functions
            if bloom_tables[key] == 0:
                bloom_tables[key] = 1
                
    #Checking how many passwords2 are already entered in the Bloom Filter
    n = 0
    for passw in passwords2:
        hash_keys = list(hash_functions(bloom_tables, passw))
        count = 0
        for key in hash_keys:
    #Checking if the bits are != 0 (or equal to 1)
            if bloom_tables[key] != 0:
                count += 1
    #If all the bits are != 0 (or equal to 1) we probably found a duplicate
        if count == k:  
            n += 1
    end = time.time()
    #Printing the results
    print('Number of hash functions used: ', k)
    print('Number of duplicates detected: ', n)
    print('Probability of false positives: ', p)
    print('Execution time: ', end - start)