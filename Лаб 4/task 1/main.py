import json


# TODO решите задачу
def task() -> float:
    with open("input.json") as file:
        input_ = json.load(file)
        sum_ = 0
        for el in input_:
            sum_+=el["score"]*el["weight"]
        return(round(sum_, 3))


print(task())
