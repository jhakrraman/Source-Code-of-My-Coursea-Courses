Question 2
Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
Remember that the factorial of a number is defined as the product of an integer and all integers before it. 
For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n))
    
Desired Output : 0 1
                 1 1
                 2 2
                 3 6
                 4 24
                 5 120
                 6 720
                 7 5040
                 8 40320
                 9 362880
                
Question 3
Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for i in range(1,11):
  result = i **3
  print(result)
  
Desired Output : 1
                 8
                 27
                 64
                 125
                 216
                 343
                 512
                 729
                 1000
                
Question 4
Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
Remember that 0 is also a multiple of 7.

pro = 0
res = 0
while(res < 100):
    res = pro * 7
    if(res > 100):
        break
    print(res)
    pro += 1
    
Desired Output : 0
                 7
                 14
                 21
                 28
                 35
                 42
                 49
                 56
                 63
                 70
                 77
                 84
                 91
                 98
                  
Question 5
The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  
Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")
      
retry(create_user, 3)
retry(stop_service, 5)
      
Desired Output : Attempt 0 failed
                 Attempt 1 failed
                 Attempt 2 succeeded
                 Attempt 0 succeeded
                 Attempt 0 failed
                 Attempt 1 failed
                 Attempt 2 failed
                 Attempt 3 succeeded
                 None
