NB. Even WORSE code than the first part. And J continues to be stupid fast.
readfile =. 1!:1
nums =. ". (LF; ' ') stringreplace readfile <'input_day1'
(,2020=nums+/nums+/nums) # ,nums*/nums*/nums
