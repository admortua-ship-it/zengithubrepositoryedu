maxScore = int(input("Enter maximum score or grade: "))
actualScore = int(input("Enter actual score or grade: "))
setPassing = input("Enter set passing score or grade (Optional, N to skip): ")

if setPassing == "N":
  distToPassing = actualScore - (maxScore*0.6)
  mistakes = maxScore - actualScore
elif setPassing < 0 and setPassing 
