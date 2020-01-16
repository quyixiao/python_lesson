import bisect

breakpoint = [60,70,80,90]
grades = "EDCBA"

score = 55

a = bisect.bisect(breakpoint,score)



print(a,grades[a])
