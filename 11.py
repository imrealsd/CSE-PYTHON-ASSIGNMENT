queue=["Kolkata","Cooch Behar","Malda","Howrah"]
print("The original queue was:\n",queue)
key=int(input("Enter 0/1 for enqueue/dequeue:"))
if(key==0):
    value=input("Enter item you want to enqueue:")
    queue.append(value)
    print("After enqueuing the new queue is:\n",queue)
elif(key==1):
    queue.pop(0)
    print("After dequeuing the new queue is:\n",queue)        

