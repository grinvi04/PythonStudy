# 문자열 타입
commentLength = 20

# 문자열 생성
print("=" * commentLength)
print("문자열 생성")
print("=" * commentLength)

# 1. 큰따옴표로 양쪽 둘러싸기
print("Hello World")
# 2. 작은따옴표로 양쪽 둘러싸기
print('hello world')
# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")
# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
print("=" * commentLength)
print("문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때")
print("=" * commentLength)

# 1) 문자열에 작은따옴표 (') 포함시키기
print("Python's favorite food is perl")
print('Python"s favorite food is perl')
# 2) 문자열에 큰따옴표 (") 포함시키기
print('Python\'s favorite food is perl')
print("\"Python is very easy.\" he says.")

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
print("=" * commentLength)
print("여러 줄인 문자열을 변수에 대입하고 싶을 때")
print("=" * commentLength)
# 1) 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is short\nyou need python"
print(multiline)
# 2) 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용
multiline = '''
life is short
you need to python
'''
print(multiline)

multiline = """
life is short
you need to python
"""
print(multiline)

# 문자열 연산하기
print("=" * commentLength)
print("문자열 연산하기")
print("=" * commentLength)
# 1) 문자열 더해서 연결하기(Concatenation)
head = "python"
tail = " is fun"
print(head + tail)

# 2) 문자열 곱하기
a = "python"
print(a * 2)    # 여기서 *은 반복, 즉 2번 반복출력하라는 의미

# 3) 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱과 슬라이싱
print("=" * commentLength)
print("문자열 인덱싱과 슬라이싱")
print("=" * commentLength)
a = "life is too short, you need to python"
print(a[3])

# 문자열 인덱싱 활용하기
print(a[0])
print(a[-0])
print(a[12])
print(a[-1])

# 문자열 슬라이싱

# life만 뽑아내기
b = a[0] + a[1] + a[2] + a[3]
print(b)
# 슬라이싱으로 처리(끝번호 index의 값은 포함되지 않음)
print(a[0:4])
# 문자열을 슬라이싱하는 방법
print(a[0:6]) # 공백도 문자와 동일하게 취급된다.
print(a[:10]) # 시작번호 생략 시 문자열의 처음부터 슬라이싱
print(a[20:]) # 끝번호 생략 시 문자열의 끝까지 슬라이싱
print(a) # 문자열 전체 print(a[:])와 같다.

# 문자열 포매팅
print("=" * commentLength)
print("문자열 포매팅")
print("=" * commentLength)
# 1) 숫자 바로 대입
print("I eat %d apples." % 3)
# 2) 문자열 바로 대입
print("I eat %s apples." % "five")
# 3) 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)
# 4) 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

# 문자열 관련 함수들
print("=" * commentLength)
print("문자열 관련 함수들")
print("=" * commentLength)
# 문자 개수 세기(count)
a = "hobby"
print(a.count("b"))
# 위치 알려주기1(find)
a = "Python is best choice"
print(a.find("b"))
print(a.find("k"))
# 위치 알려주기2(index)
a = "Life is too short"
print(a.index("t"))
#print(a.index("k")) # error 발생, find는 없으면 -1리턴하지만 index는 오류발생
# 문자열 삽입(join)
a = ","
print(a.join('a b c d')) # 공백도 인식함
# 소문자를 대문자로 바꾸기(upper)
# 대문자를 소문자로 바꾸기(lower)
# 왼쪽 공백 지우기(lstrip)
# 오른쪽 공백 지우기(rstrip)
# 양쪽 공백 지우기(strip)
# 문자열 바꾸기(replace)
# 문자열 나누기(split) 기본은 공백이고 parameter로 구분자 지정 가능하다.
# 왼쪽 정렬
print("{0:<10}".format("hi"))   # 자리수에 맞춰 빈 공간을 채운다.
# 오른쪽 정렬
print("{0:>10}".format("hi"))
# 가운데 정렬
print("{0:^10}".format("hi"))
# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))
# 소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
# { 또는 } 문자 표현하기
print("{{ and }}".format())





