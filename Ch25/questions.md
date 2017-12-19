Answered by Leo Qiu; Marked by Jack Wu

Chapter 23 ECQ:
1.	(a)   Index = -1
     X   Names[Middle] < s
     First ¡û Middle ¨C 1
	(b)  not stored in ascending order
	(c)  the function returns the index of the searching item
		The function returns -1
2	(a)  Apple	(frontqueue)
		Pear
		Banana 0 (endqueue)
				(freelist)
			  0
	(b i)  Class Node:
			def__init__(self):
			self.data = ¡°¡±
			self.pointer = 0
	(b ii)  Queue = [Node() for i in range(51)
		  Fqueue = 0
		  Equeue = 0
	      Freelist = 0
		  for i in range (1, 50):
		  	Queue[i].pointer = i + 1
	(c i)  Queue   Node
		NewItem
		StartOfFreeList    INTEGER
		FrontOfQueue 	INTEGER
		EndOfQueue 		INTEGER
		NewNodePointer 	INTEGER
	(c ii) NullPointer
		FrontOfQueue ¡ûNewNodePointer
		EndOfQueue
		NewNodePointer
		NewNodePointer

Chapter 24 ECQ:
1.	(a)  
YYYYNNNN
YYNNYYNN
YNYNYNYN
X  XXXX
X
X X
(b)        X
??? 
Correction:

Passenger vehicle YYYN
Between 6 o¡¯clock and 19 o¡¯clock -YN-
More than 3 occupants YNN-

Standard charge -X-X
Reduced charge --X-
Free          X---
2.	 
Trailer
Accont Number  Account holder name  Payment Date  Amount  FinalBalance  Message
                                                            Overdraw message
3.	                       Coin insearted
Barrier lowered                            Barrier raised
                     X  Car has exited
Close remotely        Open remotely
        Barrier open
