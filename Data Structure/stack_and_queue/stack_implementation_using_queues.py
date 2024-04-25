# Implementing stack using queue
# steps to follow:-
# 1) create two queue
# 2) Add x-> q2
# 3) insert element of q1-> q2 (element by element)
# 4) swap(q1, q2)

# pop()
# remove the top of q1

# psudo code for push operation
# push(x)
# q2.push(x)
# while(q1 is not empty)
# q2.push(q1.top());
# q1.pop()
# swap(q1, q2)

# pop()
#q1.pop()

# top()
# q1.top()

# implement stack using single queue
# push(x){
# q1.push(x);
# for(i=0, i<q1.size-1, i++)
# q1.push(q,top())
# q1.pop();


