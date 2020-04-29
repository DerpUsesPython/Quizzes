print ('Which is a noun? Enter the number of the correct answer. 1: Run 2: Table 3: Swim 4: Walk')
Score = 0
LAQ1 = int(input())
if LAQ1== 2:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('Which is a verb? Enter the number of the correct answer. 1: Run 2: Table 3: Bath 4: Glasses')
LAQ2 = int(input())
if LAQ2 == 1:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')
    
print ('Which is plural? Enter the number of the correct answer. 1: Run 2: Tables 3: Swim 4: Walk')
LAQ3 = int(input())
if LAQ3 == 2:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('Which is singular? Enter the number of the correct answer. 1: Miles 2: Tables 3: Switches 4: Leg')
LAQ4 = int(input())
if LAQ4 == 4:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('Which is an adjective? Enter the number of the correct answer. 1: People 2: County 3: Fast 4: Bell')
LAQ5 = int(input())
if LAQ5 == 3:
    print ('CORRECT')
    Score = Score + 1
else:
    print ('Wrong!')

print ('You have finished the test.')
print ('Your score was',Score,'out of 5!')
import time
time.sleep(10) #delay for 10 seconds to see results.
print ('bye')
time.sleep(1)
