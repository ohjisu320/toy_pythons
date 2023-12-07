# source from ../polls_first_yugyengjo.py

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?"
    ,"상품의 가격에 대해 어떻게 생각하시나요?"
    ,"상품의 디자인에 대해 어떻게 생각하시나요?"
    ,"상품에 대한 전반적인 만족도는 어떠신가요?"
]
list_answer =  ["좋음", "중간", "좋아지길"]
list_statistics = [0, 0, 0] 
number = 0
for str_question in list_question:         
    number += 1                                    # 문항 번호 입력
    print("{}. {}".format(number, str_question))
    pass
    number_02 = 0                                  # 답항 번호 입력("1. 2. 3."반복 필요 > 하위 for문 밖으로 배치)
    for str_answer in list_answer:
        number_02 += 1                             # 답항 번호 입력
        print("{}. {}".format(number_02, str_answer), end=" ")
    print("")
    str_list_answer = input("당신 생각은 몇 번 : ") 
    num_list_answer = int(str_list_answer)
    index = num_list_answer - 1
    list_statistics[index] = list_statistics[index] + 1
    # input
    print("")                                      # 줄바꿈
    print("-------------------------------")
pass
list_average = (list_statistics[0] * 3 + list_statistics[1] * 2 + list_statistics[2] * 1)/(list_statistics[0]+list_statistics[1]+list_statistics[2])
print(list_average)
print("End program!")
