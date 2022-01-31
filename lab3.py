#3.1
str_list = ['a', 'd', 'e', 'b', 'c']
print(str_list) #first_unsorted

str_list.sort()
print(str_list) #second_sorted

#3.2
str_list.append('f')
print(str_list)

#3.3
str_list.remove('d')
print(str_list)

#3.4
print(str_list[2]) #Results: c

#3.5
my_list = ['a','123',123,'b','B','False',False,123,None,'None']
print(len(set(my_list))) #Results: 9 unique items

#3.6
print(len("This is my third python lab.".split())) #Results: 6 words

#3.7
num_list = [12, 32, 43, 35]
num_list.sort()
print(num_list[0]) # minimum = 12
print(num_list[-1]) # maximum = 43

#3.8
game_board = [  [0,0,0],
                [0,0,0],
                [0,0,0] ]

print(game_board)
game_board[1][1]=1
print(game_board) #Results: absolute middle value is changed from 0 to 1
