#예외처리.

#JAVA는 강제적으로. try/catch/finally 로 직접 끝내든 throws 로 던지기
#python 은 하기 싫어도 안해도 됨.
#    직접: try - except - else - finally

#일 단 3가지 오류에대한 차이.
#error : 컴파일 작업을 실행하지 못하는 상황.
#warning : 정리가 안된 소스 (ex.:쓸모없는 변수 설정, close() 안한상황 등)
#exception : 실행하다가 예외적인 상황이 발생. 코드가 정상적으로 돌아가지 않는 상황.

#python 은 인터프리터 방식으로 컴파일을 하기 때문에 error 과 exception 의 차이가 애매하다. 


#하나씩 처리하는 방법.
try:
    a=int(input("x:"))
    b=int(input("y:"))
    z=a//b
    print(z)
    l=[1,23,456]
    print(l[b])
except ZeroDivisionError:
    print("y에 0?")
except IndexError:
    print("list 에 없음")

    
finally:
    print("문제가 있든 없든 무조건 실행  (return보다 먼저)")


#통으로 처리
try:
    a=int(input("x:"))
    b=int(input("y:"))
    z=a//b
    print(z)
    l=[1,23,456]
    print(l[b])

except Exception as asas:
    print(asas)
    
else:
    print("문제 없으면 실행")
    print("문제 있으면  위의 except 로 넘어가고 실행 x")

finally:
    print("문제가 있든 없든 무조건 실행  (return보다 먼저)")