#평가질

##사용법
 #가장 아래 평가질(#여기 입력) 에 name에 이름, age에 나이, height에 키 입력
 #상단 중앙에 run 클릭

##작동 단계
 #이름, 나이, 키를 받음
 #나이가 10살 미만이면 "안녕" 이라고 말함
 #나이가 10살에서 20살 사이면 "안녕하세요" 라고 말함
 #그 외 에는 "안녕하십니까" 라고 말함
 #키가 160 이상 170 미만이면 "좀 작은 키네." 라고 말함
 #키가 170 이상 180 미만이면 "평균 정도의 키네." 라고 말함
 #키가 180 이상 190 미만이면 "키 크고 좋네." 라고 말함
 #키가 190 이상 200 미만이면 "엄청 크네." 라고 말함
 #키가 200 이상 혹은 160 미만이면 "쳐다 보기도 힘들다." 라고 말함

def  평가질(name, age, height):
  if age < 10:
    print("너무 어려, "+ name, height)
  elif age < 20 and age >= 10:
    print("젊네, "+ name, height)
  elif age < 30 and age >= 20:
    print("사회 초년생, "+ name, height)
  elif age < 40 and age >= 30:
    print("어느 정도 여유가 생기는 나이, "+ name, height)
  else:
    print("남은 인생도 힘내자, "+ name, height)
  if height < 170 and height >= 160:
    print("좀 작은 키네. \n")
  elif height < 180 and height >= 170:
    print("평균 정도의 키네. \n")
  elif height < 190 and height >= 180:
    print("키 크고 좋네. \n")
  elif height < 200 and height >= 190:
    print("엄청 크네. \n")
  elif height >= 200 or height < 160:
    print("쳐다 보기도 힘들다. \n")

평가질("이준혁", 16, 179) #여기 입력