# d=input()
# count=0
# vowels=['a','e','i','o','u','A','E','I','O','U']
# for i in range(len(d)):
#     if d[i] in vowels:
#         count+=1
# print(count)


# def vovelscount(d):
#     count=0
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     for i in range(len(d)):
#         if d[i] in vowels:
#             count+=1
#     return count
# d=input()
# print(vovelscount(d))
# f=input()
# count=[]
# for i in range(len(f)):
#     count.append(f.count(f[i]))
# max_count = max(count)
# max_char = ''
# for j in range(len(count)):
#     if count[j] == max_count:
#         if max_char == '' or ord(f[j]) < ord(max_char):
#             max_char = f[j]
# print(max_char)


# linked list

class node():
    def __init__(self,data):
        self.data=data
        self.next=None
def print_linked_list(current_node):
    while current_node!= None:
        print(current_node.data)
        current_node=current_node.next
def insertattailnode(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
def insertatheadnode(head,ele):
    temp=node(ele)
    if head==None:
        return temp
    temp.next=head
    return temp
head=None
nums=[10,20,30,40,50,60,70]
for i in nums:
    head=insertattailnode(head,ele)

















# d1=node(10)
# d2=node(20) 
# d3=node(30)
# print(d1.data)
# print(d2.data)
# print(d3.data)
# print(d1.next)
# print(d2.next)
# print(d3.next)
# d1.next=d2
# d2.next=d3
# d3.next=None
# print(d1.next)
# print(d2.next)
# print(d3.next)