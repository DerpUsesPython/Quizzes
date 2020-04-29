print ('3+4=')
Score = 0
mathQ1 = int(input())
if mathQ1 == 7:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')
    
print ('5+5=')
mathQ2 = int(input())
if mathQ2 == 10:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('3+10=')
mathQ3 = int(input())
if mathQ3 == 13:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('7-6=')
mathQ4 = int(input())
if mathQ4 == 1:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('3x4=')
mathQ5 = int(input())
if mathQ5 == 12:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('4-4=')
mathQ6 = int(input())
if mathQ6 == 0:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')
    
print ('8x2=')
mathQ7 = int(input())
if mathQ7 == 16:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('10+10=')
mathQ8 = int(input())
if mathQ8 == 20:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('12+21')
mathQ9 = int(input())
if mathQ9 == 33:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('10x10=')
mathQ10 = int(input())
if mathQ10 == 100:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('You have finished the test.')
print ('Your score was',Score,'out of 10!')
import time
time.sleep(10) #delay for 10 seconds to see results.
print ('bye')
time.sleep(1)







