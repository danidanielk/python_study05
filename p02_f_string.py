#python 3.6.x 버전 부터 f-string 이라는 포맷팅 이 나왔다.


#기존에 쓰던 방식
no= 3
eat= "밥"
print("저는 하루 %d 번 %s먹어요"% (no,eat))


#f-string
print(f"저는 하루{no}번{eat}먹어요")