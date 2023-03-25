# identifeye-takehome

## Implements a Simple Patient-Exam processing system

### Format for running file:
1. python process.py [input file name]  
Eg: python process.py input.txt

Sample Input File:

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
