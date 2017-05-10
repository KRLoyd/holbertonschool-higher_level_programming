#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

# Holberton's test
sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

# Empty String
sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

# sentence = "At Holberton school, I learnt C!"
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))
