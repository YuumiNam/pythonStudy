# 자연수 뒤집어 배열로 구하기
# 입력값 n = 12345 , 출력값 return [5,4,3,2,1]


def solution(n) :
    answer = []
    n = list(str(n))
    n.reverse()

    for el in range(0,len(n)) :
        answer.append(int(n[el]))
    return answer

print(solution(12345))



#제일 작은 수 제거하기 단, 배열이 비어있다면 [-1] 리턴
#입력값 arr = [4,3,2,1] , 출력값 return[4,3,2]

def solution(arr) :
    if len(arr) == 1 :
        return [-1]
    else : 
        arr.remove(min(arr))
        return arr

a = [2,1,3,4]

print(solution(a))



#두 정수 사이의 모든 합
#입력값 3,5 출력값 12

def solution(a,b) :
    answer = 0
    if a > b :
        for i in range(b,a+1) : 
            answer += i  
    elif a < b : 
        for i in range(a,b+1) :
            answer += i
    else :
        answer = a
    return answer

print(solution(3,5))



#정수 제곱근 판별
#그 후 제곱근보다 1 큰수의 제곱을 구하기
def solution(n):
    answer = 0
    for i in range(1,n) : 
        if i * i == n :
            answer = i
            break
        elif i * i > n : #더 빠르게 효율적으로
            break
    if answer == 0 : 
        return -1
    return (answer+1) * (answer+1)

print(solution(9))



# 모듈은 변수, 함수, 클래스 등을 모아 놓은 스크립트 파일이고
# 패키지는 여러 모듈을 묶은 것이다.
# 다른 파일에 제곱을 구하는 함수를 만들고 오자

from cat import Cat
from dog import Dog
from square import squared

print(squared(3)) #square.py파일에 있는 제곱함수를 가져와서 쓴 모습


#모듈은 클래스에도 적용가능
#animal클래스 다른 파일에 만들기
#dog클래스 cat클래스도 각각 다른 파일에 만들기
#dog,cat 클래스 사용하기

cat = Cat()
dog = Dog()

print(cat.butler)
print(cat.name)
print(dog.name)
print(dog.master)

