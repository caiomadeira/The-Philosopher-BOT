# def f(x):
#     return {'tposX': (80 - 38 ), 'tposY': 105, 'wrap_value': 25, }[x]
#
#
# v = f('tposX')
#
# print(v)
def f(x, tweet_txt):
    if len(tweet_txt) > 240:
        return {'tposX': 38, 'tposY': 105, 'wrap_value': 25, }[x]

    elif len(tweet_txt) <= 25:
        return {'tposX': 38 - 80, 'tposY': 80 - 150, 'wrap_value': 25 - 20, }[x]


def f_q(x_q, tweet_txt):
    if len(tweet_txt) > 240:
        return {'tposX': 32, 'tposY': 10, 'wrap_value': 0, }[x_q]

    elif len(tweet_txt) <= 25:
        return {'tposX': 42, 'tposY': 23, 'wrap_value': 5, }[x_q]


p = f('posX')