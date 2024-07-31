grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(grades)
print(students)

students = list(students)
res = students.sort()
print(students)

s0 = students[0]
s1 = students[1]
s2 = students[2]
s3 = students[3]
s4 = students[4]


g0 =(sum(grades[0])/len(grades[0]))
g1 = (sum(grades[1])/len(grades[1]))
g2 = (sum(grades[2])/len(grades[2]))
g3 = (sum(grades[3])/len(grades[3]))
g4 = (sum(grades[4])/len(grades[4]))

grades[0] = g0
grades[1] = g1
grades[2] = g2
grades[3] = g3
grades[4] = g4


dict([[s0, g0], [s1, g1], [s2, g2], [s3, g3], [s4, g4]])
list_ = dict([[s0, g0], [s1, g1], [s2, g2], [s3, g3], [s4, g4]])
print(list_)

