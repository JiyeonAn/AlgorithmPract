'''
#1. String 과 List[]의 차이점

List는 문자열 변경 바로 가능
ex List)
'''
l = [1,2,3,4,5]
type(l)               #type 형 l 출력
l[0] = 'x'  
print(l)              #출력 결과 ['x', 2, 3, 4, 5]

'''
String 문자열 변경을 원한다면 
ex String)
'''
s = 'Mike'
new_s = s.replace('k', 'z')
print(new_s) #'Mize' 출력

s = 'Naze'
new_s = s[:2] + 'k' + s[3:] 
print(new_s)                  # 'Nake' 출력

'''
#2. List와 Tuple()의 차이점

문자 : 변경가능 객체
List : 참조형 객체, 참조하는 List도 함께 데이터가 변경됨
Tuple : copy 가능

ex List)
'''
n = [1,2,3,4,5]
type(n)
n = x 
x[0] = 'a'
print(n)
print(x)                      # n과 x모두 ['a', 2, 3, 4, 5] 출력됨 

n = [1,2,3]
x = copy(n)
x[0] = 'A'

#or

n = [1,2,3]
x = [4,5,6]
tmp = n
n = x
x = tmp 
print(n)
print(x)                    # n = [4,5,6] x = [1,2,3]

'''
ex tuple)
'''

min, max = 0,10             # 자동 tuple형성

min,max = max, min
print(min, max)             # 10, 0


'''
tuple은 APPEND가 불가능하다 그러므로 질문/답지 같은 변수를 만들 때 유용

질문 : TUPLE
답 : LIST 
로 생성해서 질문에 APPEND되지 않도록 방지
'''

chose_from_three = ('a', 'b', 'c')
answer = []
answer.append('A')        #가능
chose_from_three.append('A')  #syntax 에러

'''
#3. 사전형 {}

dict로 선언 가능
tuple형 dict로 선언도 가능

'''
d = {'x': 100, 'y': 200}
d['z'] = 300
print(d)                # {'x': 100, 'y': 200, 'z': 300}

dict(a=10, b=20)
#or
dict([('a', 10)    ,    ('b', 20)])   










