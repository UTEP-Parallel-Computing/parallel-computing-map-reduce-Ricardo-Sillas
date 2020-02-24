# Parallel computing lab 3
# Ricardo Sillas

import pymp
import re
import time

def count_words(doc, word_list, tot_word):
    f = open(doc, 'r')
    for word in word_list:
        tot_word[word] += len(re.findall(word, f.read().lower()))
        f.seek(0)

def map_reduce(doc_list, word_list):
    tot_word = pymp.shared.dict()
    with pymp.Parallel(8) as p:
        for word in word_list:
            tot_word[word] = 0
        map_lock = p.lock
        for doc in p.iterate(doc_list):
            map_lock.acquire()
            count_words(doc, word_list, tot_word)
            map_lock.release()
    print(tot_word)

def main():
    doc_list = ["shakespeare1.txt", "shakespeare2.txt", "shakespeare3.txt", "shakespeare4.txt", "shakespeare5.txt", "shakespeare6.txt", "shakespeare7.txt", "shakespeare8.txt"]
    doc_list1 = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt"]
    word_list = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    word_list1 = ["one", "six", "seven", "eight", "nine"]
    start_time = time.time()
    map_reduce(doc_list, word_list)
    print(time.time() - start_time)

main()
