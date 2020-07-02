#간단한 대화
#나이 입력에 따라 대화 내용이 바뀜
#맨 아래 chat에 ("이름", 나이) 입력

def chat(name1, age):
 if age >= 10 and age < 20:
   print("선생님: 학생, 자기소개 좀 해줄래?" )
   print("%s: 안녕하세요, 제 이름은 %s이고, 나이는 %d살 입니다." % (name1, name1, age))
   print("선생님: 자 우리 %s 친구 에게 박수\n" % name1)
 if age >= 20 and age < 27:
   print("교수: 거기 학생, 자기소개 좀 해줄 수 있을까요?" )
   print("%s: 안녕하세요, 제 이름은 %s이고, 나이는 %d살 입니다." % (name1, name1, age))
   print("교수: 네 %s 학생 잘 부탁드립니다.\n" % name1)
 if age >= 27 and age < 30:
   print("면접관: 지원자분, 자기소개 좀 해주실래요?" )
   print("%s: 안녕하세요, 제 이름은 %s이고, 나이는 %d살 입니다." % (name1, name1, age))
   print("면접관: 네 %s 지원자분.\n" % name1)

chat("이준혁", 16)
chat("이혁수", 20)
chat("차정후", 28)