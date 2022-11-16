'''
Problem statement:
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

Example 2:

Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).


'''
from collections import defaultdict
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # zip the time, user and website to one list
        tuw = list(zip(timestamp,username,website))

        # we need to sort them by time --> username --> website
        sorted_tuw = sorted(tuw)

        # We will polulate a user history hashmap of various pages visited. The hashmap is of type {user: [pages]}
        user_history = defaultdict(list)
        for t, u, w in sorted_tuw:
            user_history[u].append(w)

        # get various combinations possible for various users
        patternCount = defaultdict(int)
        for user,pages in user_history.items():
            
            # get various combinations possible for various users in the pair of 3 and add them to set so that they are unique
            userCombinations = set(combinations(pages,3))
            
            # for every pair of userCombination, we will update the count. This count will make sense for second user onwards having the same pattern
            for userCombination in userCombinations:
                patternCount[userCombination] += 1
        
        # We need to sort both the keys(pattern lexographically) from from min to max and values(score) form max to min 
        # If we inverse the values of keys from val to -val, then we can sort both of them in ascending order, using minhea
        # here invertedValues represent the values with -ve sign added to it
        invertedValues = [-x for x in patternCount.values()]
        
        # Zip both the keys and values so that we can sort them. We are placing invertedValues first as we first need to sort by score and then need to sort lexographically in natural order
        c = list(zip(invertedValues, patternCount.keys()))
        
        # Heapify will sort them in the ascending order as this is min heapify operation and will take nlog(n) time
        heapq.heapify(c)

        # Top of the heap will represent the sorted value by -ve score, we can return the second element from this popped element 
        return heapq.heappop(c)[1]
