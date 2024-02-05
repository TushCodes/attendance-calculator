def calculate_attendance():
    total_classes = int(input("Enter the total number of classes: "))
    attended_classes = int(input("Enter the number of classes attended: "))
    
    attendance_percentage = (attended_classes / total_classes) * 100
    
    print(f"Your attendance percentage is: {attendance_percentage}%")
    
    if attendance_percentage >= 75:
        print("Congratulations! You have above 75% attendance.")
    else:
        print("Oops! You have below 75% attendance.")
        
        classes_to_cover = 75 - attendance_percentage
        print(f"You need to cover {classes_to_cover} more classes to reach 75% attendance.")
        print("If you leave 1 class, your attendance will be:")
        print(f"{(attended_classes / (total_classes + 1)) * 100}%")
        print("If you leave 2 classes, your attendance will be:")
        print(f"{(attended_classes / (total_classes + 2)) * 100}%")
        print("If you leave 3 classes, your attendance will be:")
        print(f"{(attended_classes / (total_classes + 3)) * 100}%")
        print("If you leave 4 classes, your attendance will be:")
        print(f"{(attended_classes / (total_classes + 4)) * 100}%")

calculate_attendance()
