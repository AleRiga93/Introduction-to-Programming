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
output_file = open("student_result.txt", "w")


name = input_file.readline().strip()

final_weight = 0
total_weight = 0

line = input_file.readline().strip()
while line and line != "":
    parts = line.split(", ")

if len(parts) == 3:
    name = (parts[0])
    mark = float(parts[1])
    weight = float(parts[2])

    final_weight += (mark * weight) / 100
    total_weight += weight

grade = mark_calc (final_weight)

output_file.write(f"{name}, {final_weight}, {grade}")

name = input_file.readline().strip()

input_file.close()
output_file.close()