단 = int(input("원하는 단 입력 :"))

"""
print(단,"X 1" ,"=", 단 * 1,"입니다")
print(단,"X 2" ,"=", 단 * 2,"입니다")
print(단,"X 3" ,"=", 단 * 3,"입니다")
print(단,"X 4" ,"=", 단 * 4,"입니다")
print(단,"X 5" ,"=", 단 * 5,"입니다")
print(단,"X 6" ,"=", 단 * 6,"입니다")
print(단,"X 7" ,"=", 단 * 7,"입니다")
print(단,"X 8" ,"=", 단 * 8,"입니다")
print(단,"X 9" ,"=", 단 * 9,"입니다")
"""
for i in range(1,10):
    #print(단,"X 9" ,"=", 단 * 9,"입니다")
    print(f"{단} X {i} = {단*i}")