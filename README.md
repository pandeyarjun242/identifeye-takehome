### identifeye-takehome

## Implements a Simple Patient-Exam processing system

# To change input file. 
1. Open process.py
2. Change file name in line 70

Sample Input:

ADD PATIENT 123 JOHN DOE
ADD PATIENT 321 JOE SCMOE
ADD PATIENT 321 JOHN SNOW
ADD PATIENT 789 JANE CROW
ADD EXAM 321 444
ADD EXAM 789 445
ADD EXAM 789 554
DEL PATIENT 321

Sample Output:
Name: JOHN DOE, Id: 123, Exam Count: 0
Name: JANE CROW, Id: 789, Exam Count: 2
