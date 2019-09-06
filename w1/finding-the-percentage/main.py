if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    student_selected = student_marks[query_name]
    avg = (student_selected[0] + student_selected[1] + student_selected[2]) / 3
    print("{0:.2f}".format(avg))
