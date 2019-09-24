import re
if __name__ == '__main__':
    for i in range(int(input())):
        valid = True
        try:
            re.compile(input())
        except:
            valid = False
        print(valid)
