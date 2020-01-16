import bisect

breakpoint = [60, 70, 80, 90]
grades = "EDCBA"
score = 55
a = bisect.bisect(breakpoint, score)
print(a, grades[a])

def get_grade(score, breakpoint=[60, 70, 80, 90], grades="EDCBA"):
    return grades[bisect.bisect(breakpoint, score)]


get_grade1 = lambda score, breakpoint=[60, 70, 80, 90], grades="EDCBA": grades[bisect.bisect(breakpoint, score)]

print(get_grade(55))
print(get_grade1(55))
