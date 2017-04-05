def diff(s1, s2):
    r1 = s1.readlines()
    r2 = s2.readlines()
    print(r1 == r2)

p1 = input("please input file1 path" + '\n')
p2 = input("please input file2 path" + '\n')
s1 = open(p1, 'r')
s2 = open(p2, 'r')
diff(s1, s2)
s1.close()
s2.close()
