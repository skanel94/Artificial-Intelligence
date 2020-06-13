import sys
import csp
import copy

# ______________________________________________________________________________
# KenKen Problem

#sunarthsh gia na a8roizw tis times metavlhtwn stis klikes
def add(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum
#sunarthsh gia na afairw tis times metavlhtwn stis klikes
def sub(*args):
	return abs(args[0]-args[1])
#sunarthsh gia na pollaplasiazw tis times metavlhtwn stis klikes
def mult(*args):
	product = 1
	for arg in args:
		product *= arg
	return product
#sunarthsh gia na diairw tis times metavlhtwn stis klikes
def div(*args):
	quot = float(args[0]) / float(args[1])
	if (quot > 1):
		return quot
	else:
		return 1/quot
#otan o periorismos einai monadikos epistrefei thn idia th timh	
def eq(*args):
	return args[0]

#sunarthsh gia na kanw parse sthn ka8e grammh kai na diaxwrizw ta dedomena
#sxetika me to poies metavlhtes summetexoun se klika, ti praksh ginetai,
#kai poio einai t zhtoumeno apotelesma	
def parseLines(line):
	flagX=flagY=0
	tokens = lines.split()
	
	coordinates = []
	for ch in tokens[0]:
		if ch=='(':
			flagX=1
			continue
		if flagX==1:
			x=ch
			flagX=0
			flagY=1
			continue
		if flagY==1:
			if ch==',':
				continue
			else:
				y=ch
				flagY=0
				coordinates.append("v" + str(x) + str(y))
	
	if (tokens[1] == "add"):
		func = "add"
	elif (tokens[1] == "sub"):
		func = "sub"
	elif (tokens[1] == "mult"):
		func = "mult"
	elif (tokens[1] == "div"):
		func = "div"
	elif (tokens[1] == "''"):
		func = "eq"
	else:
		print ("Wrong Input!")
		
	result = tokens[2]
	
	return [coordinates,func,result]

#sunarthsh periorismwn tou kenken
def kenken_constraint(A ,a ,B ,b):
	flagA = False
	flagB = False

	#metavlhtes pou exoun ginei assigned
	c_assignedA = 0
	c_assignedB = 0

	count = 0
	
	#eksetazw mia pros mia tis grammes ths domhs mou gia na dw poies
	#metavlhtes summetexoun se periorismous
	for line in info:

		#Otan enas periorismos 8a afora "monadikh" metavlhth
		#auto shmainei pws auth h metavlhth 8a prepei na parei auth tn timh
		if len(line[0]) == 1:
			if A == line[0][0]:
				if a == int(line[2]):
					flagA = True				
			elif B == line[0][0]:
				if b == int(line[2]):
					flagB = True

		if line[1] == "add" :
			if A in line[0]:
				x = a 
				for C in line[0]:
					if C!=A: 		
						if C in game.infer_assignment():
							c_assignedA+=1
							cval = game.choices(C)
							c = cval[0]
							if count == 0 :
								x = add(a,c)
								count+=1
							else:
								x = add(x,c)

				if x == int(line[2]) and (c_assignedA+1) == len(line[0]):
					flagA = True
				elif x >= int(line[2]) and (c_assignedA+1) <= len(line[0]):
					flagA = False
				elif x == int(line[2]) and (c_assignedA+1) < len(line[0]):
					flagA = False
				else:
					flagA = True

			if B in line[0]:
				x = b
				for C in line[0]:
					if C!=B: 		
						if C in game.infer_assignment():
							c_assignedB+=1
							cval = game.choices(C)
							c = cval[0]
							if count == 0 :
								x = add(b,c)
								count+=1
							else:
								x = add(x,c)

				if x == int(line[2]) and (c_assignedB+1) == len(line[0]):
					flagB = True
				elif x >= int(line[2]) and (c_assignedB+1) <= len(line[0]):
					flagB = False
				elif x == int(line[2]) and (c_assignedB+1) < len(line[0]):
					flagB = False
				else:
					flagB = True

		if line[1] == "mult" :
			if A in line[0]:
				x = a 
				for C in line[0]:
					if C!=A: 		
						if C in game.infer_assignment():
							c_assignedA+=1
							cval = game.choices(C)
							c = cval[0]
							if count == 0 :
								x = mult(a,c)
								count+=1
							else:
								x = mult(x,c)

				if x == int(line[2]) and (c_assignedA+1) == len(line[0]):
					flagA = True
				elif x >= int(line[2]) and (c_assignedA+1) <= len(line[0]):
					flagA = False
				elif x == int(line[2]) and (c_assignedA+1) < len(line[0]):
					flagA = False
				else:
					flagA = True
					
			if B in line[0]:
				x = b
				for C in line[0]:
					if C!=B:
						if C in game.infer_assignment():
							c_assignedB+=1
							cval = game.choices(C)
							c = cval[0]
							if count == 0 :
								x = mult(b,c)
								count+=1
							else:
								x = mult(x,c)

				if x == int(line[2]) and (c_assignedB+1) == len(line[0]):
					flagB = True
				elif x >= int(line[2]) and (c_assignedB+1) <= len(line[0]):
					flagB = False
				elif x == int(line[2]) and (c_assignedB+1) < len(line[0]):
					flagB = False
				else:
					flagB = True
				
		if line[1] == "sub" :
			if A in line[0]:
				for C in line[0]:
					if C!=A:
						if C in game.infer_assignment():
							cval = game.choices(C)
							c = cval[0]
							x = sub(a,c)
							if x == int(line[2]):
								flagA = True
						else:
							for y in game.curr_domains[C]:
								x = sub(a,y)
								if x == int(line[2]):
									flagA = True
							
			if B in line[0]:
				for C in line[0]:
					if C!=B:
						if C in game.infer_assignment():
							cval = game.choices(C)
							c = cval[0]
							x = sub(b,c)
							if x == int(line[2]):
								flagB = True
						else:
							for y in game.curr_domains[C]:
								x = sub(b,y)
								if x == int(line[2]):
									flagB = True			
		if line[1] == "div" :
			if A in line[0]:
				for C in line[0]:
					if C!=A:
						if C in game.infer_assignment():
							cval = game.choices(C)
							c = cval[0]
							x = div(a,c)
							if x == int(line[2]):
								flagA = True
						else:
							for y in game.curr_domains[C]:
								x = div(a,y)
								if x == int(line[2]):
									flagA = True
							
			if B in line[0]:
				for C in line[0]:
					if C!=B:
						if C in game.infer_assignment():
							cval = game.choices(C)
							c = cval[0]
							x = div(b,c)
							if x == int(line[2]):
								flagB = True
						else:
							for y in game.curr_domains[C]:
								x = div(b,y)
								if x == int(line[2]):
									flagB = True
	
	return a!=b and flagA and flagB


class KenKen(csp.CSP):

	#kata tn arxikopoihsh enos antikeimenou KenKen 8a xreiastw
	#to mege8os tou board kai ta stoixeia twn periorismwn pou
	#phra sthn eisodo.
	def __init__(self,size,info):
		#dhmiourgw mia lista me tis metavlhtes
		variables = []
		for x in range(size):
			for y in range(size):
				variable = "v" + str(x) + str(y)
				variables.append(variable)
		
		#ftiaxnw to pedio twn timwn poy mporei n parei ka8e metavlhth
		domain = []
		for x in range(size):
			domain.append(x+1)
		
		#dhmiourgw ena dict gia ta domains, me key tis metavlhtes
		#kai value to domain me tis dunates times.
		domains = dict()
		for x in variables:
			domains[x] = domain
			
		#ftiaxnw epishs ena deepcopy gia na exw panta krathmeno
		#to Original Domains me tis metavlhtes pou eixa arxika kai ta
		#pedia tous
		originalDomains = copy.deepcopy(domains)
		
		#dhmiourgw ena dict gia tous geitones ka8e metavlhths
		#...ws geitones 8ewrw t stoixeia p vriskontai sthn idia
		#sthlh kai idia grammh gia ka8e metavlhth.
		neighbors = dict()
		for var in variables:
			for neigh in variables:
				if var != neigh:
					if var[1]==neigh[1] or var[2]==neigh[2]:
						neighbors.setdefault(var,[]).append(neigh)
				
		csp.CSP.__init__(self, variables, domains, neighbors, kenken_constraint)

		

#___________________________________MAIN______________________________________________________
#_____________________________________________________________________________________________	

if __name__ == "__main__":

	inFile = sys.argv[1]

	with open(inFile,'r') as i:
		puzzle = i.readlines()

	kenkenLines = [line.strip() for line in puzzle if line is not '']

	#The first line of my input-file,will have the size of the board.
	boardSize = int(kenkenLines[0])

	#After I save the size of the board in a variable, I delete it from the list
	#so I can parse it to gain the constraints I need.
	kenkenLines.pop(0)	
	info = []
	for lines in kenkenLines:
		info.append(parseLines(lines))	
	

	############################
	# DOKIMES GIA MAIN KLHSEIS #
	############################
	game = KenKen(boardSize,info)
	
	#BT:
	x = csp.backtracking_search(game)
	print("Final Results: ",x)
	#BT+MRV:
	#x = csp.backtracking_search(game, select_unassigned_variable=csp.mrv)
	#print("Final Results: ",x)
	#FC:
	#x = csp.backtracking_search(game, inference=csp.forward_checking)
	#print("Final Results: ",x)
	#FC+MRV:
	#x = csp.backtracking_search(game, select_unassigned_variable=csp.mrv, inference=csp.forward_checking)
	#print("Final Results: ",x)
	#MAC:
	#x = csp.backtracking_search(game, inference=csp.mac)
	#print("Final Results: ",x)
	#Min - Conflicts:
	#x = csp.min_conflicts(game)
	#print("Final Results: ",x)
