# dictionary 예제
dic = {
    'name' : 'pay'
    , 'phone' : '0119993323'
    , 'birth' : '1118'
}

print(dic)

dic = {
    'a' : 'hi'
}

print(dic)

#요소 삭제
del dic['a']
print(dic)

#요소 추가
dic['a'] = 12
print(dic)

#중복키 사용불가
dic = {1:'a', 1:'b'}
print(dic)

#관련함수
dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

#key 리스트만들기
dic.keys()
print(dic.keys()) # dict_keys 객체를 리스트형태로 리턴해주나 리스트관련 함수는 사용불가

list = list(dic.keys()) #dict_keys 객체를 리스트로 변환
print(list)

#values 리스트 만들기
print(dic.values()) #dict_values 객체 리턴

#Key, Value 쌍 얻기(items)
print(dic.items()) #dict_items 객체 리턴

#Key: Value 쌍 모두 지우기(clear)
print(dic.clear())

#Key로 Value얻기(get)
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic.get('name'))

#a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고 할 경우 a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 리턴한다는 차이가 있다.
print(dic.get('nokey'))
#print(dic['nokey'])

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('nokey' in dic)
