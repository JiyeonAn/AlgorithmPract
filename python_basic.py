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
변수별 값을 선언하고 싶을 경우엔 tuple보다 dict를 사용한다.

'''
d = {'x': 100, 'y': 200}
d['z'] = 300
print(d)                # {'x': 100, 'y': 200, 'z': 300}

dict(a=10, b=20)
#or
dict([('a', 10)    ,    ('b', 20)])   

d.clear()  #d 사전형 클리어 
d = {'apple' : 1000, 'banana' : 2000}

#tuple형으로 선언하는 경우
t=dict([(apple, 1000),(banana, 2000)])
#list를 사용하는경우
L =[[apple , 1000],[banana, 2000]]

'''
#4. 집합형{} -set

사전형의 simple버전 
다른 그리드타입의 형변환을 도와줌
리스트의 중복을 제거해준다
'''

A = ('apple' , 'banana', 'apple') #tuple형

Kind = set(A)  #집합형으로 형변환 apple, banana만 출력
Print(kind)


 '''  
If문 indentation에러 주의
'''

A = 10
B = 5
If A = 1:
  Print(" success")
  If B > 10:        #indentation 해야함
   Prunt(" suceess")


'''
논리연산자 / 아무것도 들어있지 않다는 값의 표시
/ None
'''

is_ok = True   #논리연산자
If  is_ok : 
   Print("success")

#값이 없는 경우에도 같음 0, 0.00, '' 인경우
If is_ok :
 Print("success")
else 
  Print("empty")

#None이란??  하나의 object. 값이 아님

If is_ok is None:
  Print("success")

'''
While else feat. Break, continue
'''

#While문도 기존 문법과 같이 사용 가능

i = 0

while i < 5
  print(i)
 i += 1
 
 #else문 사용 가능 : break문이 없을 경우 마지막에 한번더 else로직을 타게 한다.
 
 i = 0
 while i<5
   print(i)
   i += 1
   else
    print('success')
    
  '''
  break : while에서 벗어난다.
  continue : 다음 조건으로 while문을 탄다.
  '''
  
  '''
for else feat. Break, continue
   - while문과 비슷함 + for에서 인수 지정 혹은 list, 사전형 선언 가능 
'''
  
  i = [ 1,2,3,4]
  n = 0
  while n < len(i)
    print(i[n])
    n += 1
    
 #for문으로 전환시
 
  for n in i
      print(n)
   
   
  
  







