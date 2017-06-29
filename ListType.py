#위키독스 리스트 예제
# java의 배열과 같다고 생각하면 된다.
commentLength = 20

#리스트 표현
print("=" * commentLength)
print("리스트 표현")
print("=" * commentLength)
odd = [1, 3, 5, 7, 9]
print("odd : {0}".format(odd))

#리스트 인덱싱, 슬라이싱
print("=" * commentLength)
print("리스트 인덱싱, 슬라이싱")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))    #리스트 전체출력
print("a[0] : {0}".format(a[0])) #리스트 첫번째
print("a[0] + a[1] + a[2] = {0}".format(a[0] + a[1] + a[2]))  #리스트 요소 계산
print("a[-1] : {0}".format(a[-1]))    #리스트 마지막 요소

# 중첩 리스트
print("=" * commentLength)
print("중첩 리스트")
print("=" * commentLength)
a = [1, 2, 3, ['a', 'b', 'c']]
print("a : {0}".format(a))
print("a[0] : {0}".format(a[0]))
print("a[-1] : {0}".format(a[-1]))
print("a[3] : {0}".format(a[3]))
print("a[-1][-1] : {0}".format(a[-1][-1]))

#리스트의 슬라이싱
print("=" * commentLength)
print("리스트의 슬라이싱")
print("=" * commentLength)
a = [1, 2, 3, 4, 5]
print("a : {0}".format(a))
print("a[0:2] : {0}".format(a[0:2]))
print("a[2:] : {0}".format(a[2:]))
b = "12345"
print("b : {0}".format(b))
print("b[0] : {0}, b[1] : {1}".format(b[0], b[1]))
print("b[0:2] : {0}".format(b[0:2]))

#리스트 연산자
print("=" * commentLength)
print("리스트 연산자")
print("=" * commentLength)
a = [1, 2, 3]
b = [4, 5, 6]

print("a : {0}".format(a))
print("b : {0}".format(b))

#더하기
print("=" * commentLength)
print("리스트 더하기")
print("=" * commentLength)
print("a + b : {0}".format(a+b))

#반복
print("=" * commentLength)
print("리스트 반복")
print("=" * commentLength)
print("a * 3 : {0}".format(a * 3))

#리스트의 수정, 변경, 삭제
print("=" * commentLength)
print("리스트의 수정, 변경, 삭제")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))

#하나의 값 수정
print("=" * commentLength)
print("리스트 값 수정(하나)")
print("=" * commentLength)
print("a[2] : {0}".format(a[2]))
a[2] = 4
print("a[2] : {0}".format(a[2]))

#연속된 값 수정
# 범위 수정과 값 수정은 전혀 다르다
print("=" * commentLength)
print("리스트 값 수정(범위)")
print("=" * commentLength)
print("a : {0}".format(a))
a[1:2] = ['a', 'b', 'c']
print("a[1:2] = ['a','b','c'] : {0}".format(a))
a = [1, 2, 3]
a[1] = ['a', 'b', 'c']
print("a[1] = ['a', 'b', 'c'] : {0}".format(a))

#[] 사용해 리스트 삭제
print("=" * commentLength)
print("[] 사용해 리스트 삭제")
print("=" * commentLength)
print("a : {0}".format(a))
del a[1]
print("del a[1] : {0}".format(a))
del a[1:2]
print("del a[1:2] : {0}".format(a))
a[0] = []
print("a[0] : {0}".format(a))

#관련 함수
#append는 마지막 요소에 추가
print("=" * commentLength)
print("관련함수 append")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))
a.append(4)
print("a.append(4) : {0}".format(a))
a.append([5,6])
print("a.append([5,6]) : {0}".format(a))

#sort는 리스트 정렬
#숫자
print("=" * commentLength)
print("관련함수 sort")
print("=" * commentLength)
a = [1, 4, 8, 3]
print("a : {0}".format(a))
a.sort()
print("a.sort() : {0}".format(a))
a.sort(reverse=True)
print("a.sort(reverse=True) : {0}".format(a))

#문자
a = ['a', 'c', 'b']
print("a : {0}".format(a))
a.sort()
print("a.sort() : {0}".format(a))

#reverse는 리스트 뒤집기(정렬 X)
print("=" * commentLength)
print("관련함수 reverse(정렬은 안됨)")
print("=" * commentLength)
a = ['a', 'c', 'b']
print("a : {0}".format(a))
a.reverse()
print("a.reverse() : {0}".format(a))

#index는 위치 반환
print("=" * commentLength)
print("관련함수 index(위치반환)")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))
print("a.index(1) : {0}".format(a.index(1)))

#insert는 요소삽입
print("=" * commentLength)
print("관련함수 insert(요소삽입)")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))
a.insert(5, 4) # 마지막 index보다 큰 값을 넣으면 자동으로 마지막 index값으로 들어간다.
print("a.insert(5, 4) : {0}".format(a))

#remove는 요소제거
print("=" * commentLength)
print("관련함수 remove(요소제거)")
print("=" * commentLength)
a = [1, 2, 3, 1, 2, 3]
print("a : {0}".format(a))
a.remove(3)
print("a.remove(3) : {0}".format(a))

#pop는 요소꺼내고 삭제
print("=" * commentLength)
print("관련함수 pop(요소껀고 삭제)")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))
print("a.pop() : {0}".format(a.pop()))
print("after pop : {0}".format(a))

#요소 개수 세기
print("=" * commentLength)
print("요소 개수 세기")
print("=" * commentLength)
a = [1, 2, 3, 1]
print("a : {0}".format(a))
print("a.count(1) : {0}".format(a.count(1)))


#리스트 확장
print("=" * commentLength)
print("리스트 확장")
print("=" * commentLength)
a = [1, 2, 3]
print("a : {0}".format(a))
a.extend([4, 5]) # 리스트만 올수 있음
print("a.extend([4, 5]) : {0}".format(a))



