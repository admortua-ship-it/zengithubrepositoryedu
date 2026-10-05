t = 0
while t == 0:
  maxScore = int(input("Enter maximum score or grade: "))
  actualScore = int(input("Enter actual score or grade: "))
  setPassing = input("Enter set passing score or grade (Optional, N to skip): ")
  
  if setPassing == "N":
    distToPassing = actualScore - (maxScore*0.6)
    mistakes = maxScore - actualScore
    t += 1
  elif setPassing > 0 and setPassing <= maxScore:
    distToPassing = actualScore - (maxScore*0.6)
    mistakes = maxScore - actualScore
    t += 1
  elif setPassing <= 0 and setPassing > maxScore:
    print("Invalid set passing threshold. Please try again.")
    t += 0

if distToPassing >= 0:
  status = "PASSED"
elif actualScore >= maxScore:
  status = "PERFECT"
elif distToPassing < 0:
  status = "FAILED"

print("")
print("SUMMARY:")
print(" --- ")
print(f"Distance to passing threshold: {distToPassing}")
print(f"Mistakes: {mistakes}")
print(f"Status: {status}")
