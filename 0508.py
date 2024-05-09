N = int(input())
a = [int(input()) for i in range(N)]
list_1 = []
list_2 = []
list_3 = []
list_4 = []
Sum1 = 0
Sum2 = 0
Sum3 = 0
Sum4 = 0
# print("a is ",a)
for j in range(N):
    # print("j is ",j)
    if j % 4 == 1:
        list_1.append(a[j])
        Sum1 = sum(list_1)
# print(list_1)
    elif j % 4 == 2:
        list_2.append(a[j])
        Sum2 = sum(list_2)
    elif j % 4 == 3:
        list_3.append(a[j])
        Sum3 = sum(list_3)
    else:
        list_4.append(a[j])
        Sum4 = sum(list_4)

X = Sum1 - Sum3
Y = Sum2 - Sum4
print(X, Y)
# print(Sum1)







# for i in range(N):
#     #XとYの選別
#     i += 1
#     if i % 2 ==0:
#         #Xの動き方
#         if i % 4 == 2:



# 指針
# 4で割って
# あまり１ならY*1
# あまり２ならX*１
# あまり３ならY＊−１
# あまり０ならX*-1



        
#         else:
#     else:
#         #Yの動き方
#         if i % 4 == 1:
            
#         else:
            





# class Coordinate:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
# #xの進み方を定義
#     def x_function(self):
#         x_sum_score = (self.x1 - self.x2)
#         return x_sum_score
# #Yの進み方を定義
#     def y_function(self):
#         y_sum_score = (self.y1 - self.y2)
#         return y_sum_score

