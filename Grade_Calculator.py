def main():
    # Input the number of exams, assignments, and projects
    num_exams = int(input("Enter the number of exams: "))
    num_assignments = int(input("Enter the number of assignments: "))
    num_projects = int(input("Enter the number of projects: "))

    # Initialize variables for total weighted score and total weight
    total_weighted_score = 0
    total_weight = 0

    # Loop through each exam to input weight and marks
    for i in range(1, num_exams + 1):
        exam_weight = float(input(f"Enter weight for exam {i}: "))
        exam_marks = float(input(f"Enter marks for exam {i}: "))
        total_weighted_score += exam_marks * exam_weight
        total_weight += exam_weight

    # Loop through each assignment to input weight and marks
    for a in range(1, num_assignments + 1):
        assign_weight = float(input(f"Enter weight for assignment {a}: "))
        assign_marks = float(input(f"Enter marks for assignment {a}: "))
        total_weighted_score += assign_marks * assign_weight
        total_weight += assign_weight

    # Loop through each project to input weight and marks
    for p in range(1, num_projects + 1):
        project_weight = float(input(f"Enter weight for project {p}: "))
        project_marks = float(input(f"Enter marks for project {p}: "))
        total_weighted_score += project_marks * project_weight
        total_weight += project_weight

    # Calculate the final percentage based on the total weighted score and total weight
    final_percentage = (total_weighted_score / total_weight)
    print(f"Your final percentage is: {final_percentage:.2f}%")

    # Optional: Calculate desired grade
    desired_grade = input(
        "Do you want to calculate what score you need for a desired grade? (yes/no): ")
    if desired_grade.lower() == "yes":
        desired_percentage = float(input("Enter your desired percentage: "))
        remaining_weight = 100 - total_weight
        required_score = (desired_percentage -
                          final_percentage) * (remaining_weight / 100)
        print(
            f"You need to score {required_score:.2f} on the remaining exams to achieve {desired_percentage}% overall.")


# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
