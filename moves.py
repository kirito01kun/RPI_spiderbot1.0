dict = {'pos_a': (5, 10), 'pos_b': (15, 20)}

newkey = 'obs' + str(1)
dict[newkey] = (1, 5)
for ele in dict:
    print(dict[ele][0])