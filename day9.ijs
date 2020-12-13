NB. Oof. Not very elegent. The extra prepend/drop code at the
NB. end is especially gross, becuase the rolling window makes
NB. things awkward to deal with. Might have been better to use boxes

readfile =. 1!:1
window_n =. 25
nums =. , _1 }. ".;._1 LF, readfile <'input_day9'
NB. extract atom
]part_1 =. 0{ ((window_n # 0) , ((-window_n) }. 0 = (+/@,@((_1&{)=((+/[) & (window_n&{.))) )"1(window_n+1)&{.;.3 nums)) # nums

NB. part 2
subsetsums =. (+/\\. nums)
startpos =.  <. ((part_1 = ,subsetsums) i. 1) % $nums
len =. ($nums) | (part_1 = ,subsetsums) i. 1
(<./ + >./) len {. startpos }. nums
