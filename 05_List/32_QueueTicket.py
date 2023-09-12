n = int(input())
ticket, timein, timeorder, queue = [], [], [], []
toShow = [] # keep output in list and print later

for _ in range(n) :
  x = input().split()
  if x[0] == 'reset' :
    ticket.append(int(x[1])) # set a starting ticket
  elif x[0] == 'new' :
    toShow.append('ticket ' + str(ticket[-1]))
    queue.append(ticket[-1]) # append last ticket to queue
    timein.append(int(x[1])) 
    ticket.append(ticket[-1] + 1) # append next ticket number
  elif x[0] == 'next' :
    order = queue[0] # first element in queue
    toShow.append('call ' + str(order))
    queue.pop(0) # pop the first element that just call
    timeorder.append(0) # append empty element in timeorder
  elif x[0] == 'order' :
    idx = ticket.index(order) 
    timeorder[idx] = int(x[1]) # replace 0 in timeorder 
    toShow.append('qtime ' + str(order) + ' ' + str(timeorder[idx] - timein[idx]))
  elif x[0] == 'avg_qtime' :
    s, c = 0, 0 
    for i in range(len(timeorder)) :
      if timeorder[i] > timein[i] :
        s += (timeorder[i] - timein[i]) 
        c +=1
    toShow.append('avg_qtime ' + str(round(s / c, 4)))

for i in toShow : print(i)