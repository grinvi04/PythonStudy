#위키독스 리스트 예제

#리스트 표현
odd = [1, 3, 5, 7, 9]
print(odd)

#리스트 인덱싱, 슬라이딩
a = [1, 2, 3]
print(a)    #리스트 전체출력
print(a[0]) #리스트 첫번째
print(a[0] + a[1] + a[2])  #리스트 요소 계산
print(a[-1])    #리스트 마지막 요소

# 중첩 리스트
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][-1])

#리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[2:])
b = "12345"
print(b[0:2])

#리스트 연산자
a = [1, 2, 3]
b = [4, 5, 6]

#더하기
print(a+b)

#반복
print(a * 3)

#리스트의 수정, 변경, 삭제
a = [1, 2, 3]

#하나의 값 수정
a[2] = 4
print(a)

#연속된 값 수정
# 범위 수정과 값 수정은 전혀 다르다
a[1:2] = ['a', 'b', 'c']
print(a)
a[1] = ['a', 'b', 'c']
print(a)

#[] 사용해 리스트 삭제
del a[1]
print(a)
del a[1:2]
print(a)

#관련 함수
#append는 마지막 요소에 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#sort는 리스트 정렬
#숫자
a = [1, 4, 8, 3]
a.sort()
print(a)

#문자
a = ['a', 'c', 'b']
a.sort()
print(a)

#reverse는 리스트 뒤집기(정렬 X)
a = ['a', 'c', 'b']
a.reverse()
print(a)

#index는 위치 반환
a = [1,2,3]
print(a.index(1))

#insert는 요소삽입
a = [1, 2, 3]
a.insert(5, 4)
print(a)

#remove는 요소제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

#pop는 요소꺼내고 삭제
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

#요소 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))

#리스트 확장
a = [1, 2, 3]
a.extend([4, 5]) # 리스트만 올수 있음
print(a)



