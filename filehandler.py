def mark_calc (final_weight):
    if final_weight >= 70:
        return "Distinction"
    elif final_weight >= 60:
        return "Merit"
    elif final_weight >= 50:
        return "Pass"
    else:
        return "Fail"

input_file = open("student_mark.txt", "w")
input_file.write("Paul\n")
input_file.write("Computing, 50, 25\n")
input_file.write("Networking, 60, 25\n")
input_file.write("Dissertation, 70, 50\n")
input_file.write("\n")
input_file.write("Alex\n")
input_file.write("Computing, 70, 35\n")
input_file.write("Networking, 80, 55\n")
input_file.write("Dissertation, 60, 50\n")
input_file.close()

input_file = open("student_mark.txt", "r")



line = input_file.readlines().strip()

#I don't know how to complete it















input_file.close()
