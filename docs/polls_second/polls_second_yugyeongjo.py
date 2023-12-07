# source from ../polls_first_dongchulhan.py

list_question = [  
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
    ]
list_answer = ["좋음", "중간","좋아지길"]

list_statistics = [0, 0, 0]

for num_question_counts in [1,2,3,4]:
    num_question_counts = num_question_counts - 1
    num_question = num_question_counts + 1
    str_question = list_question[num_question_counts]
    print("{}. {}" .format(num_question, str_question))

    for num_answer_counts in [1,2,3]:
        num_answer_counts = num_answer_counts -1
        num_answer= num_answer_counts +1
        str_answer = list_answer[num_answer_counts]
        print("{}.{}" .format(num_answer,str_answer), end = "")
    print("")
    print("")

    str_ask = "당신 생각은 몇 번 :"
    num_ask = int(input("{}".format(str_ask)))
    index = num_ask - 1
    list_statistics[index] = list_statistics[index] +1


    if num_question_counts != 3:
        print("")
        print("-----------------")

print("")
print("--------------통계---------------")
print("설문지 답항별 갯수 표시 {}".format(list_statistics))
print("")
print("답변별 가중치 (좋음:3, 중간:2, 좋아지길:1)")

average = ((3*list_statistics[0] + 2*list_statistics[1] + 1*list_statistics[2]) / (list_statistics[0] + list_statistics[1] + list_statistics[2]))
print("답항 가중 평균 : {}".format(average))