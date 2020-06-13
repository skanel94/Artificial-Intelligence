from heapq import *

class PriorityQueue:
	
	h = []
	count=0
	
	#Sunarthsh eisagwghs twn stoixeiwn sthn PriorityQueue
	def push(self,item, priority):
		if (self.h).count((priority,item))==0:
			heappush((self.h), (priority,item))
			self.count = self.count + 1

	#Sunarthsh eksagwghs twn stoixeiwn sthn PriorityQueue
	def pop(self):
		self.count = self.count - 1
		return heappop((self.h))[1]

	#Sunarthsh elegxou gia kenh PriorityQueue
	def isEmpty(self):
		return self.count==0
	
	#Sunarthsh enhmerwshs ths PriorityQueue
	def update(self,item,priority):
		i = priority
		
		#8a ginei true MONO an vrw zeygos me item alla me proteraiothta
		#mikroterh h ish me toy priority
		
		max = -1
		for i in range(0,self.count):			#psaxnw sto heap na vrw an uparxei allo stoixeio me idio pedio item
			if ((self.h)[i])[1] == item:		#an uparxei
				if((self.h)[i])[0] > max: 		#checkarw (gia ola ta stoixeia autou tou item) na vrw auto me to pio mikro priority
					max = ((self.h)[i])[0]		#otan to vrw , an uparxei , 8etw auto max
					position = i				#kai kratw th 8esh tou
					
		if max == -1:							#sthn periptwsh pou den uparxei stoixeio me idio item sthn pq to eisagw
			self.push(item, priority)
			self.count = self.count + 1
		else:									#alliws an to priority toy 
			if(priority<max):
				(self.h)[position] = (priority,item)
				heapify((self.h))
	
	#Sunarthsh print gia thn PriorityQueue
	def printQueue(self):
		print (self.h)
		print (self.count)	
		

#Sunarthsh (auksousas) taksinomhshs me xrhsh PriorityQueue
def PQSort(lst):
	sortLst = []
	pq = PriorityQueue()										#Dhmiourgia mias priority queue
	for x in lst:												#Ola ta stoixeia ths listas lst pou phre san orisma
		pq.push(str(x), x)										#ta eisagei sthn oura proteraiothtas
	while pq.isEmpty()== False:									#Mexri na adeiasei h oura	
		sortLst.append(int(pq.pop()))							#Eksagoume ta stoixeia ths ouras ena ena kai ta topo8etoume sth nea lista
	return sortLst												#Taksinomhmenh ( kata auksousa seira ) epistrefei h nea lista apo th sunarthsh