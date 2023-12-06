list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?"
    ,"상품의 가격에 대해 어떻게 생각하시나요?"
    ,"상품의 디자인에 대해 어떻게 생각하시나요?"
    ,"상품에 대한 전반적인 만족도는 어떠신가요?"
]
list_answer =  ["좋음", "중간", "좋아지길"]
# for number_count in ["1", "2", "3", "4"]

number = 0

for str_question in list_question:
    number += 1
    print("{}. {}".format(number, str_question))
    pass
    number_02 = 0
    for str_answer in list_answer:
        number_02 += 1
        print("{}. {}".format(number_02, str_answer), end=" ")
    print("")  
    print("-------------------------------")

print("End program!")
