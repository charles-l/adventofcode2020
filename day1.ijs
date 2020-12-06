NB. Such terrible code, but J is stupid fast.
readfile =. 1!:1
nums =. ". (LF; ' ') stringreplace readfile <'input_day1'
(,2020=nums+/nums) # ,nums*/nums

NB. Part 2
(,2020=nums+/nums+/nums) # ,nums*/nums*/nums
