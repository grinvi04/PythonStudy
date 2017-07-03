# 튜플 선언 예제
commentLength = 20

print("=" * commentLength)
print("튜플 선언")
print("=" * commentLength)

t1 = ()
print("t1 = () => {0}".format(t1))
t2 = (1, )
print("t2 = (1, ) => {0}".format(t2))
t3 = (1, 2, 3)
print("t3 = (1, 2, 3) => {0}".format(t3))
t4 = 1, 2, 3
print("t4 = 1, 2, 3 => {0}".format(t4))
t5 = ('a', 'b', ('ab', 'cd'))
print("t5 = ('a', 'b', ('ab', 'cd')) => {0}".format(t5))

# 튜플은 요소 삭제, 요소 수정 시 오류
print("=" * commentLength)
print("튜플은 요소 삭제, 요소 수정 시 오류")
print("=" * commentLength)

print("1. 튜플 요소값 삭제 시 오류")
t1 = (1, 2, 'a', 'b')
# del t1[0] // 오류발생
print("2. 튜플 요소값 변경 시 오류")
t1 = (1, 2, 'a', 'b')
# t1[0] = 'c' // 오류발생


# 인덱싱, 슬라이싱, 더하기, 곱하기 가능
print("=" * commentLength)
print("인덱싱, 슬라이싱, 더하기, 곱하기 가능")
print("=" * commentLength)

print("1. 인덱싱하기")
t1 = (1, 2, 'a', 'b')
print("t1 : {0}".format(t1))
print("t1[0] => {0}".format(t1[0]))
print("t1[3] => {0}".format(t1[3]))

print("2. 슬라이싱하기")
print("t1 : {0}".format(t1))
print("t1[1:] => {0}".format(t1[1:]))

print("3. 튜플 더하기")
t2 = (3, 4)
print("t1 : {0}".format(t1))
print("t2 : {0}".format(t2))
print("t1 + t2 : {0}".format(t1 + t2))

print("4. 튜플 곱하기(반복)")
print("t2 * 3 : {0}".format(t2*3))




#튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 없는가이다. 즉, 리스트의 항목값은 변화가 가능하고 튜플의 항목값은 변화가 불가능하다



