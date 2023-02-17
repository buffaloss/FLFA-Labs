#the class for the finite automaton
class finiteAutomaton:
    #the class constructor with all the parameters needed
    def __init__(self, initial_states, final_states, alphabet, transitions_list):
        self.initial_states = initial_states
        self.final_states = final_states
        self.alphabet = alphabet
        self.transitions_list = transitions_list
        
    #method for checking if an input string can be obtained via the state transition
    def StringChecker(self,string):
        #if the first character is not in the initial_states , it is not a valid string
        if string[0] not in self.initial_states: 
            return False
        #if the last character is not in the final states, then it's not a valid string
        if string[-1] not in self.final_states:
            return  False
        #check by iterating through each letter , if each one is present in our alphabet of teh FA
        for letter in string:
            if letter not in self.alphabet:
                return False
        
        #create list of transitions of empty states
        #each state is a list itself 
        transitions = [['', letter, ''] for letter in string]
        transitions[0][0] = 'S' #set first element as S (the beginning state of the FA)
        transitions[-1].pop() # remove last eleemtn from last transition (the final state)
        #iterate through th elements , except the last one
        for i in range(len(transitions) - 1):
            curr_state, input_character, next_state = transitions[i]
            #iteration for checking
            for state in self.transitions_list:
                if curr_state == state[0] and input_character == state[1]: #if they match
                   #update the next state and the starting state of teh next one
                   transitions[i][2] = state[2]
                   transitions[i + 1][0] = state[2]
                   break
            #check for an emptry next state
            #meaning if there is no valid trasnition 
            if transitions[i][-1] == '':
                return False
            
        print('')
        print('Transitions attempted for the input word: ',transitions)
        return True
