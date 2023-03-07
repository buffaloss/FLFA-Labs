import random
from automaton import finiteAutomaton

# the class for the grammar
class Grammar:
    #the constructor for my class
    def __init__(self,Vn,Vt,P,alpha): # the arguments are the non-terminal symbols, termina ones, the set of transitions , ect
        self.Vn = Vn
        self.Vt = Vt
        self.P = P
        self.alphabet = alpha
        self.string = '' #initialize the string as empty at first 
        self.transitions= [] # same for the array of transitions

    #method for generating the string (only one each time it's called)
    def StringGenerator(self):
        self.string='S' # start from S as the initiliaization
        self.transitions = []
        self.transitions.append(self.string)

        while self.string[-1].isupper(): # as long as the last character is UPPERCASE ( non-terminal)
            temp_arr = [] # initialize temporary array
            temp_arr.append(self.string[-1])
            x = random.choice(self.P[self.string[-1]]) 
            self.string = self.string[:-1] + x #the string is excluding the last characer 
                                                                                  #and then randomly associating a transition from the set
            if self.string[-1].isupper(): # if the last caharcer is uppercase
                temp_arr.append(self.string[-2]) #add the last two elements to the array for storing
                temp_arr.append(self.string[-1])
            else:
                temp_arr.append(self.string[-1]) #only add the last one ( since its the terminal chaarcter)
            self.transitions.append(temp_arr)
        self.transitions=self.transitions[1:] #the string will be all the characters excluding the first ( which is S)

        #print result for the generated randomly string
        print(self.string)
        print('')

        #return the  generatwd string
        return self.string 
    
    #method for converting the grammar to a Finite Automaton
    def FA_Converter(self):
        start_states =[] #initialize the states at the beginning
        #find the non-terminal characters from the starting one S
        #by iterating through the rules 
        for state in self.P['S']: 
            start_states.append(state[0]) # taking the first character of each right-hand side

        end_states = [] #initialize the states at the end after the whole process is finished
        #extract all lowercase characters from the set of transitions/rules
        for i in self.P:
            for state in self.P[i]: #iterating 
                if state.islower():  #checking if it's lowercase
                    end_states.append(state) #then add it to the array of end states

        transitions_list = [] #initializa the list of transitions for the finite automaton as empty at first
        for i in self.P:
            for state in self.P[i]: #iterate through the production rules
                temp_arr = []
                temp_arr.append(i) # keep the transation in the temporary array
                #create transition with the left hand side as src state
                #whilst the right hand part of the rule is the destination
                temp_arr += list(state)
                transitions_list.append(temp_arr) # append each one to the list of transitions
                
        print('')
        print('TRANSITIONS LIST: ', transitions_list)
        
        #create object for the Finite Automaton
        #pass the necessary arguments
        automaton = finiteAutomaton(start_states,end_states,self.alphabet,transitions_list)
        return automaton
   
     #method for finding teh grammar type and classifying it
    def classify_grammar(grammar):
    # verify if it is of type 3
     if all(len(production) <= 2 and (production[0].islower() or production[0].isupper()) and
           (len(production) == 1 or production[1].isupper() or production[1] == 'ε') for symbol in grammar for production in grammar[symbol]):
        return "Type 3 (regular)"

    # verify if it is of type 2
     if all(len(production) <= 2 and all(s.isupper() for s in production) for symbol in grammar for production in grammar[symbol]):
        return "Type 2 (context-free)"

    # verify if its of type 1
     for symbol in grammar:
        for production in grammar[symbol]:
            if len(production) < len(symbol) and not any(s.islower() for s in production):
                return "Type 1 (context-sensitive)"

    # Cverify if its of typ 0
     for symbol in grammar:
        for production in grammar[symbol]:
            if symbol in production:
                continue
            if not all(s in grammar for s in production):
                return "Type 0 (unrestricted)"

    # if the grammar does not fit into any categories,classify it as a not a context-free grammar
     return "Not context-free"
