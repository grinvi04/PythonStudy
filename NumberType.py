
a = 3
b = 4

# 문자열 변수 포맷은 아래와 같이 쓰는게 최신
# %연산자로 출력은 예전 방식
# print("a : ", a, ", b : ", b) 이렇게 써도 되긴 함
print("a : {0}, b: {1}".format(a, b))

print("a + b = {0}".format(a+b))
print("a - b = {0}".format(a-b))
print("a * b = {0}".format(a*b))
print("a / b = {0}".format(a/b))

# x의 y제곱을 나타내는 ** 연산자
print("a ** b = {0}".format(a**b))
print("b ** a = {0}".format(b**a))

# 나눗셈 후 나머지를 반환하는 % 연산자
print("a % b = {0}".format(a%b))
print("b % a = {0}".format(b%a))

# 나눗셈 후 소수점 아랫자리를 버리는 // 연산자
print("a // b = {0}".format(a//b))
print("b // a = {0}".format(b//a))

# 음수에 // 연산자를 적용하는 경우
# // 연산자는 나눗셈의 결과에서 무조건 소수점을 버리는것이 아니라 나눗셈의 결과값보다 작은 정수 중, 가장 큰 정수를 리턴하기 때문
print("-7 / 4 = {0}".format(-7 / 4))
print("-7 // 4 = {0}".format(-7 // 4))