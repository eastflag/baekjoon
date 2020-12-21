# map의 역할, 문자열 리스트를 숫자형 리스트로 변환,
# array destructing 역할
a = '123456789'
b = list(a)
c = map(int, b)
print(list(c))