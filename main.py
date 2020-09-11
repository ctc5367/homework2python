def getGradePoint(grade):
  if grade == "A":
    return 4.00
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
    return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0

def run():
  grade1 = input("Enter your course 1 letter grade: ");
  grade1credit = input("Enter your course 1 credit:");
  grade1credit = float(grade1credit)
  gp1 = getGradePoint(grade1)
  print(f"Grade point for couse 1 is: {gp1}")

  grade2 = input("Enter your course 2 letter grade: ");
  grade2credit = input("Enter your course 2 credit:");
  grade2credit = float(grade2credit)
  gp2 = getGradePoint(grade2)
  print(f"Grade point for couse 1 is: {gp2}")

  grade3 = input("Enter your course 3 letter grade: ");
  grade3credit = input("Enter your course 3 credit:");
  grade3credit = float(grade3credit)
  gp3 = getGradePoint(grade3)
  print(f"Grade point for couse 1 is: {gp3}")

  gpa = float ((gp1*grade1credit+ gp2*grade2credit+ gp3*grade3credit)/(grade1credit+grade2credit+grade3credit));
  print(f"Your GPA is: {gpa}");


if __name__ ==  "__main__":
  run()
