# Detect-the-Only-Duplicate-in-a-List
>20th May 2021 02:01 AM

The only way to track my coding progress is to add these practice questions in these repositories. So I've come across this question and I'm trying to solve it.

***You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.***

***Bonus: Can you do this in \mathcal{O}(n)O(n) time and \mathcal{O}(1)O(1) space?***

I'm not too sure about the bonus part yet but the idea behind my current code is to loop through the list comparing the values at each indexes to each other and comparing them. If they're the same it returns the "duplicate".

Now this is a simple newbie approach and so runs into the ***"Time Limit Exceeded"*** problem.
When I've fixed it I'll be updating this with what I improved on the code.


>20th May 2021 04:59 PM


Though the concept of a linked list is still a little confusing to me - I've read a bit about it. 

This final solution considers the array to be a linked list. Any index in the array is pointing to the value of that index.

In the solution I try to use the concept of a marker. By iterating over each element we marks ***its*** corresponding index by setting it to a minus. If we have already marked it negative before that means it's the duplicate value.


