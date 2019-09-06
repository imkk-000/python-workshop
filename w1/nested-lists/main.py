if __name__ == '__main__':
    students = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if students.get(score) is None:
            students[score] = [name]
        else:
            students[score].append(name)
    selectedScore = sorted(list(students))[1]
    for studentName in sorted(students[selectedScore]):
        print(studentName)

