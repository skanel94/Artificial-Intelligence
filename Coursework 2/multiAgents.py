# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import sys

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.
        
        getAction chooses among the best options according to the evaluation function.
        
        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
		
        # Choose one of the best actions		
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]      
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best 
		
        "Add more of your code here if you want to"
		
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
		
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)		
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        
        "*** YOUR CODE HERE ***"

        for ghostState in newGhostStates:
			ghostPos = ghostState.getPosition() 
			# H 8esh  enos  GHOST apo thn opoia 8a kanei mia kinhsh pou de kseroume kai
			# sthn opoia de 8eloume na pesei panw mas !!!
			ghostX = ghostPos[0]
			ghostY = ghostPos[1]

			# Otan h nea mas 8esh sumpiptei me th 8esh ( h me mia pi8anh epomenh 8esh ) pou einai to ghost
			# epistrefoume mia poluu mikrh timh ( apogoreutikh ),wste na mhn epilegei pote san kinhsh
			if (ghostX,ghostY)==newPos:
				return -sys.maxint-1
			if (ghostX-1,ghostY)==newPos:
				return -sys.maxint-1
			if (ghostX+1,ghostY)==newPos:
				return -sys.maxint-1
			if (ghostX,ghostY-1)==newPos:
				return -sys.maxint-1
			if (ghostX,ghostY+1)==newPos:
				return -sys.maxint-1			

			# H nea 8esh tou Pacman
			x = newPos[0]
			y = newPos[1]
			min = sys.maxint

			# An auth h nea 8esh vrisketai sth lista twn faghtwn tote epistrefoume 0
			if newPos in currentGameState.getFood().asList():
				return 0

			# Gia ka8e faghtaki pou exei apomeinei elegxoume thn eukleidia apostash tou apo tn newPos tou Pacman
			for foodPoint in newFood.asList():
				dist = ((x-foodPoint[0])**2 + (y-foodPoint[1])**2) ** 0.5
				#Kai kratame telika thn apostash pros to pio kontino faghtaki
				if(dist<min):
					min = dist

        #Ki epeidh sth getAction tou ReflexAgent epilegetai h kinhsh me th megaluterh timh
        #epistrefw arnhtikes times epeidh , h kaluterh lush gia mena einai oi pio kontines
        #apostaseis ( sunepws oso pio mikres ginetai )
        return -min

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)
	
    def Result(self,state,agent,action):
		return state.generateSuccessor(agent,action)
	
    def TerminalTest(self,state,depth):
		if depth == self.depth or state.isWin() or state.isLose():
			return True
		else:
			return False
			
    def Utility(self,state):
		return self.evaluationFunction(state)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def miniMax(state):
			#Pairnoume tis epitrepomenes kinhseis tou Pacman
			pacmanActions = state.getLegalActions(0)
			#Orizoume gia max th mikroterh timh tou susthmatos
			max = -sys.maxint
			maxAction = 'STOP'
			#Gia ka8e dunath kinsh tou Pacman
			for a in pacmanActions:
				#To va8os arxika einai 0
				currDepth = 0
				#Kratw ka8e fora th timh pou m epistrefei h minValue
				currMax = minValue(self.Result(state,0,a), currDepth, 1)
				#Kai sugkrinw me t Max timh m .. an einai megaluterh h nea timh tote thn kratw opws k t action
				if currMax > max:
					max = currMax
					maxAction = a
			#Telika 8a epistreps to action p einai th megaluterh timh
			return maxAction
		
		
		
        def maxValue(state, currDepth):
			#Otan kaleitai h maxValue shmainei oti einai h seira tou Pacman pali k sunepws allazoume epiepedo (+1)
			currDepth = currDepth + 1
			#Elegxoume an eimaste se termatikh katastash ( opws auth oristhke pio panw )
			if self.TerminalTest(state,currDepth):
				#Ki an eimaste, aksiologoume thn katastash kai thn epistrefoume
				return self.Utility(state)
			v = -sys.maxint
			for a in state.getLegalActions(0):
				#Gia ka8e epitrepomenh kinhsh loipon epilegoume ayth me th megaluterh timh
				v = max(v, minValue(self.Result(state,0,a), currDepth, 1))
			#Kai thn epistrefoume
			return v


			
        def minValue(state, currDepth, ghostNum):
			#Elegxoume an eimaste se termatikh katastash ( opws auth oristhke pio panw )
			if self.TerminalTest(state,currDepth):
				#Ki an eimaste, aksiologoume thn katastash kai thn epistrefoume
				return self.Utility(state)
			v = sys.maxint
			#Gia ka8e epitrepomenh kinhsh tou fantasmatos
			for a in state.getLegalActions(ghostNum):
				#An eimaste sto teleutaio fantasma,epomenh kinhsh 8a kanei o pacman.. alliws 8a paiksei to epomeno fantasma
				if ghostNum == state.getNumAgents() - 1:
					v = min(v, maxValue(self.Result(state,ghostNum,a), currDepth))
				else:
					v = min(v, minValue(self.Result(state,ghostNum,a), currDepth, ghostNum + 1))
			#Kai telos ( to ka8e fantasma ) 8a epistrepsei th mikroterh value
			return v
			
			
        #8a klh8ei h MiniMax kai dosmenou enos gameState,8a epistrepsei thn kinhsh me th megaluterh value
        return miniMax(gameState)
		
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
	"""
      Your minimax agent with alpha-beta pruning (question 3)
	"""
	
	def getAction(self, gameState):
		"""Returns the expectimax action using self.depth and self.evaluationFunction"""
		"*** YOUR CODE HERE ***"
		#H value einai h sunarthsh pou mesolavei twn maxValue,minValue kai
		#apofasizei to an prepei na ginei kladema h oxi
		def value(state, agentIndex, depth, alpha, beta):
			#Gia termatikh katastash
			if self.TerminalTest(state,depth):
				#Ginetai aksiologhsh
				return self.Utility(state)
			#Alliws an paizei fantasma kalese th minValue
			elif agentIndex != 0:
				return minValue(state, agentIndex, depth, alpha, beta)
			#Alliws an paizei o Pacman kalese th maxValue
			else:
				return maxValue(state, agentIndex, depth, alpha, beta)

        
		#Oi sunarthseis maxValue kai minValue einai oloidies mautes pou xrhsimopoihsh sth MiniMax ulopoihsh mou
		#me ta extra orismata twn alpha kai beta kai ton eswteriko elegxo tou kladematos!
		def maxValue(state, agentIndex, depth, alpha, beta):
			v = -sys.maxint
			for action in state.getLegalActions(0):
				v = max(v, value(self.Result(state,0,action), agentIndex+1, depth, alpha , beta))
				if v > beta:
					return v
				alpha = max(alpha, v)
			return v
		def minValue(state, ghostNum, depth, alpha, beta):
			v = sys.maxint
			for action in state.getLegalActions(ghostNum):
				if ghostNum == state.getNumAgents() - 1:				
					v = min(v, value(self.Result(state,ghostNum,action), 0, depth+1, alpha, beta))
				else:				
					v = min(v, value(self.Result(state,ghostNum,action), ghostNum+1, depth, alpha, beta))
				if v < alpha:
					return v
				beta = min(beta, v)					
			return v

			
		#Arxikopoihsh twn alpha,beta
		alpha = -sys.maxint
		beta = sys.maxint
		#Gia ka8e dunath action tou pacman kalw th value
		for action in gameState.getLegalActions(0):
			v = value(self.Result(gameState,0,action), 1, 0, alpha, beta)
			#An h timh pou 8a m epistrepsei einai megaluterh apo tou alpha
			if v > alpha :
				#Tote thn kratw kai orizw ws kaluterh kinhsh..thn kinhsh pou exei auto to value
				alpha = v
				bestAction = action
				
		#Ki epistrefei telika th kaluterh kinhsh
		return bestAction

		util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #Orismos Expectimax sunarthshs gia ton max player ( Pacman ) , o kwdikas edw einai pali o kwdikas ths MiniMax
        #ulopoihshs .. elafrws allagmenos sta shmeia pou prepei .. ( kai ta opoia 8a anaferw amesws parakatw )
        def Expectimax(state):
			pacmanActions = state.getLegalActions(0)
			max = -sys.maxint
			maxAction = 'STOP'
			for a in pacmanActions:
				currDepth = 0
				currMax = chanceValue(self.Result(state,0,a), currDepth, 1)
				if currMax > max:
					max = currMax
					maxAction = a
			return maxAction
				
        def maxPlayer(state, currDepth):
			currDepth = currDepth + 1
			if self.TerminalTest(state,currDepth):
				return self.Utility(state)
			v = -sys.maxint
			for a in state.getLegalActions(0):
				v = max(v, chanceValue(self.Result(state,0,a), currDepth, 1))
			return v
	
        def chanceValue(state, currDepth, ghostNum):
			if self.TerminalTest(state,currDepth):
				return self.Utility(state)
			v = sys.maxint
			sum = 0
			for a in state.getLegalActions(ghostNum):
				#Sto shmeio auto .. 8eloume pleon oxi na dialegoume th mikroterh timh opws kaname mexri tr..
				#ALLa NA KRATAME ka8e timh kai na thn pros8etoume s ena a8roisma
				if ghostNum == state.getNumAgents() - 1:
					v =  maxPlayer(self.Result(state,ghostNum,a), currDepth)
				else:
					v = chanceValue(self.Result(state,ghostNum,a), currDepth, ghostNum + 1)
				sum = sum + v
			#To opoio prin epistrafei 8a to diairoume me to plh8os twn kinhsewn pou eixe na kanei to fantasma
			#(Praktika me tn paragonta diakladwshs tou dentrou)
			return float(sum)/float(len(state.getLegalActions(ghostNum)))
			
        #Kai telos epistrefw thn kaluterh dunath kinhsh ws pros tn Expectimax sunarthsh
        return Expectimax(gameState)
		
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
		"""
		Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
		evaluation function (question 5).

		DESCRIPTION: <write something here so we know what you did>
		"""
		"*** YOUR CODE HERE ***"
		#Se periptwsh nikhs gurname mia polu megalh timh ws mia katastash pou epi8umoume
		if currentGameState.isWin():
			return sys.maxint
		#Se periptwsh httas gurname mia polu mikrh timh ws mia katastash pou apofeugoume
		if currentGameState.isLose():
			return -sys.maxint
		
		#Pairnw tis suntetagmenes tou Pacman	
		pacmanX = currentGameState.getPacmanPosition()[0]
		pacmanY = currentGameState.getPacmanPosition()[1]

#############################################################################		
#		#Pairnw to plh8os twn fantasmatwn									#
#		numGhosts = currentGameState.getNumAgents() - 1						#
#		ghostDist = sys.maxint												#
#		i = 1																#
#		#Gia ka8e fantasma													#
#		while i <= numGhosts:												#
#			#Pairnw tis suntetagmenes tou									#
#			ghostX = currentGameState.getGhostPosition(i)[0]				#
#			ghostY = currentGameState.getGhostPosition(i)[1]				#
#			#Ypologizw thn eukleidia apostash tou ka8enos apo ton Pacman	#
#			nextGDist = ((pacmanX-ghostX)**2 + (pacmanY-ghostY)**2) ** 0.5	#
#			ghostDist = min(ghostDist, nextGDist)							#
#			i += 1															#
#############################################################################
	  	  
		foodDist = sys.maxint
		#Gia ka8e faghtaki pou exei apomeinei
		for foodPoint in currentGameState.getFood().asList():
			#Ypologizw thn eukleidia apostash tou apo ton Pacman
			nextFDist = ((pacmanX-foodPoint[0])**2 + (pacmanY-foodPoint[1])**2) ** 0.5
			foodDist = min(foodDist,nextFDist)
		
		#Me vash to score tou currentGameState .. prosdidw to analogo value sxetika me
		#tis apostaseis twn faghtwn kai to posa pallets exoun apomeinei gia to dosmeno state
		score = currentGameState.getScore() - foodDist*1.7 - len(currentGameState.getCapsules())*1.3
		
		return score
		
		util.raiseNotDefined()
		
	
# Abbreviation
better = betterEvaluationFunction

