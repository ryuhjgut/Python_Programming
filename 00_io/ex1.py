# 입출력

a = input()
print(a, end="")
print(type(a))
print(a, type(a), sep="")  # ,로 구분하면 중간에 공백 들어감, sep사용해서 없애기 가능

# 정수 변환
a = input()
a = int(a)
print(a, type(a))

b = float(input())
print(b, type(b))

# 정수 2개 입력
# 100
# 200

# c = input(int())
# d = input(int())
# print(a, b)

# input(a, b)
a = input().split()
print(a, type(a))
# map
# map(함수, List 객체)
a, b, c = map(int, input().split())
print(a, type(a))

# list() 형태로 변환
a = list(map(int, input().split()))
print(a, type(a))
