import numpy as np
n = int(input("Number of students: "))
List = np.empty((n+1,7), dtype=object)
List[0][0] = "Name"
List[0][1] = "Mathematics"
List[0][2] = "Science"
List[0][3] = "English"
List[0][4] = "Total"
List[0][5] = "Average"
List[0][6] = "Grade"

i = 1
while i<=n:
    List[i][0] = input("Enter the name: " )
    List[i][1] = int(input("Mathematics: "))
    List[i][2] = int(input("Science: "))
    List[i][3] = int(input("English: "))
    List[i][4] = np.sum(List[i,1:4])
    List[i][5] = np.average(List[i,1:4])
    avg = List[i][5]
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    List[i][6] = grade
    i = i + 1

