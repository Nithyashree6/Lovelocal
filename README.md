# Lovelocal
As a part of selection process, LoveLocal had assigned few question to solve. Here are the solved question files attached below
## Easy 1 
#### Given a string s consisting of words and spaces, return the length of the last word in the string.A word is a maximal substring consisting of non-space characters only.
#### Explaination :The function takes in a string s as input.
#### It finds the last word in the string by splitting the string into words using spaces as separators.
#### Counting Characters:Count the characters from the last non-space character until a space is encountered or the beginning of the string is reached.This count represents the length of the last word.
#### Returning the Length:Return the count obtained as the length of the last word in the string.

## Medium 1
#### Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#### Explaination : The function traverses the tree from the root.
#### Based on the values of p and q, it determines whether to move to the left or right subtrees.
#### If both p and q are on different sides of the current node, or one of them is equal to the current node's value, then the current node is the lowest common ancestor.
#### The code creates a binary search tree with some nodes.
#### It tests the lowestCommonAncestor function with different pairs of nodes (p and q) to find their lowest common ancestor and prints the value of the resulting node.

## Hard 2
#### You are given a string s. You can convert s to a palindrome by adding characters in front of it.Return the shortest palindrome you can find by performing this transformation.
#### isPalindrome(sub): This nested function checks if a given substring sub is a palindrome by comparing it to its reversed version.
#### The code iterates through the string s from the end towards the beginning (j decreases from len(s) - 1 to 0).
#### At each iteration, it checks if the substring from the start of s up to index j forms a palindrome.
#### When it finds the longest palindrome starting from the beginning of s, it notes the index (i) where this palindrome ends.
#### The function constructs the shortest palindrome by taking the remaining characters from index i to the end of s (s[i:]), reversing them ([::-1]), and appending this reversed substring at the beginning of the original string.
#### The function returns the shortest palindrome constructed by adding characters to the start of the input string s.
