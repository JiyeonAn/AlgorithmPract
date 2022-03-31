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

d.clear()              #d 사전형 클리어 
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

Kind = set(A)            #집합형으로 형변환 apple, banana만 출력
Print(kind)


 '''  
If문 indentation에러 주의
'''

A = 10
B = 5
If A = 1:
  Print(" success")
  If B > 10:           #indentation 해야함
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
  While과 잘쓰이는 input함수란 ? 루푸늘 도는동안 값 인풋 할수있는 펑션
  '''

   While True
     word = input('Enter:')  #Enter : input값 
     If word = 'ok'
     break
     Print('next')
  
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
   
  #range 함수 : for문과 자주쓰임
#리스트를 일일히 만들어서 for문을 돌리는건 귀찮은일
   For i in range(2, 10)
     Print(i)

   For i in range(2,10,3)
   Print(i)   # 2,5,8 출력됨

#해당 숫자를 index로 쓰고 싶을때
  For i in range(10)
     Print(i , 'hello')

#index를 안쓰고 싶을땐??
  For _ in range(10)  #i를 언더바로 표시
     Print('hello')

  #enumerate 함수란?  Index를 일일히 표시해주지 않아도 되는것

 For i, fruint in enumerate(['apple', ',banana,'])
   Print(i, fruit)

  #zip 함수란? 여러 list들을 같은idex 값을 한번에 출력하고싶을때

days = [1,2,3]
fruits =[ 'apple', 'orange', 'banana']
drinks = ['cola', 'sidar' , 'water']

For day, fruit, drink in zip(days,fruits,drinks)
  Print(day, fruit, drink)

'''
사전형의 for문
  - 사전형을 기존의 for문으로 출력하면 키값만 나옴
'''

Xln ={x : 100, y : 200}

For i in Xln
  Print(i)       # x,y 이렇게 출력됨

#.items 를 사용한다 >list형 안의 tuple형으로 정의됨

For k, i in Xln.itm3s
  Print( k, i)   # x, 100  y, 200 출력됨


'''
함수 정의하기 : def 반환값 : return
'''

def say_something()
   Return ('hi')

Result = say_something()
Print(Result)    # hi 출력

def What_is_color(color)
  If color = 'red'
    Print("tomato")

Result = What_is_color('red')
Print(Result)    #tomato 출력

#인수의 타입을 선언하는법
Def add_num(a : int , b : int) -> int #int 값을 넣으면 결과값도 int로 출력하라는 뜻
    return a+b
 Result = add_num(10,20)
 Print(Return)   #30 출력

#but 파이썬은 문자열로 자동 변환가능

''' 
디폴트 인수 사용법: 리스트는 디폴트값이 될수 없다!!!
'''
 def num(x , l=[])
     l.append(x)
     Return l

R = num(100)    #l =[100]
R = num(100)    #l=[100,100]

  Def num2(x , l= None)
   If l is None
      l = []
      l.append(x)


'''
 [목차]
1. 인수의 튜플화(*args)
2. 인수의 사전화(**kwargs)
3. DocStrings란
4. 함수 내 함수
5. 클로저
6. 데코레이터
'''

#1. 인수의 튜플화

def say_something(*args)
     return(*args)

d={'hi', 'Mike'}

result = say_something(*d)
Print(result)         #{hi, Mike} 출력됨

#2.키워드 인수의 사전화

r = { 'x' : 'apple', 'y' : 'banana'}
def fruit(**kwargs)
    For k, v in **kwargs.items()
      T = (k,v)
    return T

Print(fruit(**r))      # x , apple y,banana 출력


#3. DocStrings 란?? Help랑 같은 기능으로 해당함수 템플린 출력

def doc_info()
 Print(doc_info().help)
 Print(doc<info()._doc_) #같은 결과값 출력
 
 #4. 함수 내 함수

 def outer(a,b) :
   def plus(c,d):
      return c + d
   r1 = plus(a,b)
   r2 = plus(b,a)
   print(r1 + r2)
   
outer(1,2)         # r1 = 3, r2 = 3 결과값 6 출력됨.

'''
5. 클로저 : outer먼저 return하고 inner을 불러오는 방식
 inner 함수를 나중에 사용하고 싶을 때 쓰는 로직
'''

def outer(a,b):
  def inner():
      return a+b
   
  return inner
 
 r = outer(1,2)   # inner라는 함수를 먼저 return함
 f = r()          # 비로서 inner함수가 실행됨
 print(f)         # 3 출력
 

 def circle_area_func(pi):
   def circle_area(radias):
      return pi * radias * 100
    
    return circle_area
  
 cal1 = circle_area_func(3.14)
 cal2 = circle_area_func(5160.2)
 
 print(cal1(10)
 print(cal1(20)
       
       








   
  
  







