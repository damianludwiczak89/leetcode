class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 25:
            return False
            
        letters = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "q": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,      }

        for i in range(len(sentence)):
            letters[sentence[i]] += 1
        
        if 0 in letters.values():
            return False
        else:
            return True


"""
1832. Check if the Sentence Is Pangram


https://leetcode.com/problems/check-if-the-sentence-is-pangram/


A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: sentence = "leetcode"
Output: false

 

Constraints:

    1 <= sentence.length <= 1000
    sentence consists of lowercase English letters.


"""
