u = 0
print("Welcome to the 'Pass or Bagsak' Program!")
print("This program will help you determine if you passed or failed based on your scores.")

while u == 0:
  t = 0
  while t == 0:
        
    maxScore = int(input("Enter maximum score or grade: "))
    if maxScore <= 0:
      print("Invalid maximum score. Please try again.")
      t += 0
    
    elif maxScore > 0:
      actualScore = int(input("Enter actual score or grade: "))
      if actualScore < 0:
        print("Invalid actual score. Please try again.")
        t += 0
      
      elif actualScore >= 0:
          setPassing = int(input("Enter set passing score or grade (Optional, 0 to skip): "))
          if setPassing > 0 and setPassing <= maxScore:
            distToPassing = actualScore - setPassing
            mistakes = maxScore - actualScore
            t += 1
          elif setPassing == 0:
            distToPassing = actualScore - (maxScore*0.6)
            mistakes = maxScore - actualScore
            t += 1
          else:
            print("Invalid set passing threshold. Please try again.")
            t += 0

  if distToPassing >= 0:
    status = "PASSED"
    d = f"+ {str(distToPassing)}"
  elif actualScore >= maxScore:
    status = "PERFECT"
    d = f"+ {str(distToPassing)}"
  elif distToPassing < 0:
    status = "FAILED"
    d = f"- {str(abs(distToPassing))}"

# To create a "Remarks" section later.

  print("")
  print("SUMMARY:")
  print(" --- ")
  print(f"Distance to passing threshold: {d}")
  print(f"Mistakes: {mistakes}")
  print(f"Status: {status}")

  prompt = input("Do you want to try again? (Y/N): ")
  if prompt == "Y" or prompt == "y":
        u += 0
        print("")
  elif prompt == "N" or prompt == "n":
    u += 1
    print("Thank you for using the program. Goodbye!")
  else:
    print("Invalid input. Please try again.")
    u += 0
