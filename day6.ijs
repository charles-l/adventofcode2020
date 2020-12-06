readfile =. 1!:1
input =. readfile <'input_day6'
words =. <;._1 LF, input
groups =. <@;;._1 ''; words
+/;+/&~:&.> groups

NB. Part 2
groups2 =. <;._1 ''; words
+/;((;#/.;)=#) &.> groups2
