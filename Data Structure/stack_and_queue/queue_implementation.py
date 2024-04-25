#implement queue using Arrays
# Queue- FIFO
#push(4), push(2), push(3) [4,3,2]
# top()-> 4
#pop()
#top()-> 2
# operation that needs to be performed
# max_size = 5
# [0,1,2,3,4]---->cnt=0----> assign two pointers(front, rear)
# front pointer is at 0th index where as rear pointer is at 0th index
# push(3)
# first check the cnt< the max_size, if yes, we can push in the array
# [3,1,2,3,4]----> move rear to 1st index and cnt =1
# push(2)
# [3,2,2,3,4]----> rear is now and 2nd index and cnt =2
# push(1)
# [3,2,1,3,4]---> rear is now at 3rd index and cnt =3
# push(8)
# [3,2,1,8,4]---> rear is at 4th index and cnt =4
# push(6)
# [3,2,1,8,6]---> rear is at 5th index(imaginary) and cnt =5
# push(7)
# [3,2,1,8,6] ---> cnt == max_size, so queue is full
# top()
# a[front]---> edge case a[front] != a[rear]
# pop()
# [-1,2,1,8,6]---> front points to first index, cnt deceresed to 4
# top()
# a[front]--->2
# push(9)
# rear is pointing to imaginary index 5 but the cnt is less than max_size, so we can insert
# to push in this case, we need to do (rear) // max_size --> 5//5=0, so we can insert in 0th index
# [9,2,1,8,6]--> rear will move to imaginary index 6 and the cnt will be increased to 5
# pop()
# [9,-1,1,8,6]---> front will move to second index and cnt will be decreased to 4
# push(10)
# to push again we will have to do rear// max_size i.e 6//5 -> 1, i.e 1st index
# [9,10,1,8,6]---> rear will move to imaginary 7th index and cnt will be 5
# to print all the numbers:
# for i in range(front, (rear-1)):
#     print(a[front//n])

# push(x)
# if(cnt == n):
#     return -1
# a[rear //n] =x
# rear ++;
# cnt ++;

#pop()
#if(cnt==0)
#   return -1
# a[front//n] = -1
# front++
# cnt ++

#top()
# if(cnt ==0)
#   return -1
# return a[front//n]

# size()---> cnt


