import re

with open('input.txt') as f:
    data = f.readlines()

stream = list(data[0].strip())


def clean(stream):
    # remove all ignored characters (! + next character)
    while('!' in stream):
        for i in range(len(stream)):
            if stream[i] == '!':
                if i+1 < len(stream):
                    del stream[i+1]
                del stream[i]
                break

    text_stream = "".join(stream)

    # remove all garbage
    pat1 = re.compile(r'<.*?>')
    pat2 = re.compile(r'{,')
    pat3 = re.compile(r',}')
    text_stream = re.sub(pat1, '', text_stream)
    text_stream = re.sub(pat2, '{', text_stream)
    text_stream = re.sub(pat3, '}', text_stream)

    # replace {} with []
    text_stream = text_stream.replace("{","[").replace("}","]")
    
    return text_stream


def make_to_list(stream):
    return eval(stream)


def calc_score(stream, points):
    score = 0
    for group in stream:
        score += calc_score(group, points+1)

    return score + points
    

stream = make_to_list(clean(stream))
print(calc_score(stream, 1))


