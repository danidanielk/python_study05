#3항연산자 사용법 = 참일때 if 조건문 else 거짓일 때의 값
#중첩 3항 연산자 사용법 = 참일때 if 조건문 else 참2 if 조건2 else ... 거짓

#숫자를 입력 햇을 때 짝수 인지 홀수 인지 출력해주는 프로그램. (3항연산자)

def no():
    a = int(input("숫자를 입력하셔요 :"))
    return a

#기존방법
def play(no):
    if no%2==0:
        print("짝수")
    else:
        print("홀수")
#3항연산자
def play2(no):
    return print("짝수") if no %2 ==0 else print("홀수")

b=no()
# play(b)
play2(b)




#15,16,17을 list 에 담고
#리스트 각각의 요소가 2의 배수인지 3의배수인지 둘다 아닌지 출력

z=[15,16,17]
for zz in z:
    if zz%2==0:
        print(f"{zz}은 2의 배수")
    elif zz%3==0:
        print(f"{zz}은 3의 배수")
    else:
        print(f"{zz}은 2,3의배수가 아님")
