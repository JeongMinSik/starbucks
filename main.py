numbers = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def solution(s: str):
    for k, v in numbers.items():
        s = s.replace(k, str(v))
    return int(s)


rv = solution("one4seveneight")
print(rv)