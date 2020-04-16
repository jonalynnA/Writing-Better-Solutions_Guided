word_list = open(
    "/Users/toshamasters/Desktop/CS_28/Week2_Algorithms/Guided/WritingBetterSolutions/Writing-Better-Solutions_Guided/words.txt ", "r")
word_list_dict = word_list.readlines()

anagram_list = []
   for word in word_list_dict:
        number = 0
        while number < 5:
            anagram_list.append(str(word)+str(number))
            number = number + 1
    print anagram_list

'''NOTE: Understnd
              given a word, return all anagrams of that word

              anagram = a word, phrase, or name formed by rearranging 
              the letters of another, such as cinema, formed from iceman.
      '''
# NOTE: Plan
# generate all permutations of the input
# check all permutations against the dictionary (words.txt file)
# return all valid items.


def anagrams(word):
    pass
