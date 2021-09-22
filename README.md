# Udacity_Data_Structure_Nanodegree_Project_2
Udacity Data Structures &amp; Algorithms Nanodegree Project 2

For this project, you will answer the six questions laid out in the next sections. The questions cover a variety of topics related to the data structures you've learned in this course. You will write up a clean and efficient answer in Python, as well as a text explanation of the efficiency of your code and your design choices.


PROBLEM 1: To perform LRU Cache, we would first require OrderDict module as a prerequisite. Followed by which, we initialize the class LRU_Cache and use the following methods: 1. __init__(): Constructor function for the class 2. Get(): to get the key value pairs. Time Complexity: O(1) 3. Set(): Assigning the respective values for the keys. 

Time Complexity: O(1) 

Space Complexity of the program: O(n)




PROBLEM 2: To create a file finder program, we would first require os module to traverse through directories. We will create a list of files having the given suffixes and remove the initial part of the path while adding the path name. 

Time Complexity: O(n) 

Space Complexity: O(n)




PROBLEM 3: For huffman coding program, we’ll perform the following steps: 1. Find the frequency of every character in the string 2. Encode the highest frequency character then repeat the process for other characters 

Time Complexity: O(nlogn)

Space Complexity: O(n)




PROBLEM 4: For the active directory problem, we have used recursion method and performed the following tasks recursively: 1. Checking the group name and comparing it to the user’s 2. Checking the user list of the group 3. Returning True after finding the desired user name and False for not. 

Time Complexity: O(n) 

Space Complexity: O(n)



PROBLEM 5: For the blockchain problem, we have created nodes of a linked list that would act like blocks and point to the hash of previous nodes instead of the next one. We used a hash calculator with SHA256 function from hashlib module to create random hash numbers and then added them to the nodes as values along with the timestamps. 

Time Complexity: O(1)

Space Complexity: O(n)



PROBLEM 6: For the Union and Intersection problem, we take input of 2 linked lists and give out a single linked list joining them according to union or intersection. We added the values in sets according to union and intersection in their respective functions and then generated a linked list through the sets. Time Complexity: O(n) Space Complexity: O(n)
