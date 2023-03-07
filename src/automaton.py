import grammar as grammar

#the class for the finite automaton
class finiteAutomaton:
    #the class constructor with all the parameters needed
    def __init__(self,S, initial_states, final_states, alphabet, transitions_list):
        self.S = S
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
    
    #fucntion for detwermining fi its NDFA or DFA
    def is_deterministic(self):
         # Loop through each state in the set of states Q.
        for letter in self.S:
            #initiliazie array 
            reps= []
            for transition in self.transitions_list: #go through the list of transitions given
                if transition[0] == letter: #when trans starts fdrom curr letter
                    if transition[1] in reps: #verify if we have iterate through the destination state already
                        return 'Non-Deterministic Finite Automaton'
                     # If the destination state has not been seen before, it's added to the "reps" list.
                    reps.append(transition[1])
            # check whether the set of input symbols leaving from the current state
            # (i.e., the set of symbols in the "reps" list) is equal to the set of input symbols in the automaton's input alphabet.
            if set(reps) != set(self.alphabet):
                 #If the set of input symbols leaving from the current state is not equal to the input alphabet,
                 # it means that the automaton is non-deterministic, and non dterministic is returned.
                return 'Non-Deterministic Finite Autmaton'
    # If the loop completes without finding any non-deterministic transitions or input symbols,
    # the automaton is deterministic, and determinstic is returned.
        return 'Deterministic Finite Automaton'
    
    def RG_Converter(self):
         # Create an empty dictionary called "prod_rules".
        prod_rules = {}
           # Loop through each symbol in the set of non-terminal symbols S.
        for key in self.S:
            values = []
             # Loop through each transition in the list of transitions transitions_list.
            for transition in self.transitions_list:
                string = ''
                # If the source of the transition is the current symbol (key),
                if transition[0] == key:
                    for i in range(1,len(transition)):
                        # Concatenate the rest of the symbols in the transition to form a string.
                        string = string +transition[i]
                     # Add the string to the "values" list.
                    values.append(string)
            prod_rules[key] = values         # Add the "values" list as the value for the current symbol (key) in the "prod_rules" dictionary.
        #initialize a new grammar 
        regular_grammar = grammar.Grammar(self.S, self.final_states,prod_rules, self.alphabet)     
        return regular_grammar
    
    #function for conversion from NDFA to DFA
    def DFA_Converter(self):
        a = []
        for letter in self.S:
            l = len(self.alphabet)
                    # For each state (letter), create a row with one entry for each symbol in the input alphabet.
            r = ['' for index in range(l)]
            for ex in self.alphabet:
                for transition in self.transitions_list:
                    if transition[0] == letter:
                        if transition[0] == ex:
                              # Concatenate the destination state(s) of the transition(s) to form a string of states.

                            if not transition[-1].islower():
                                r[self.sigma.index(ex)] += transition[-1]
            a.append(r) # Add the row to the first array.

        b = []
        p= []
        not_p = [self.S[0]]
    # Simulate the NDFA with epsilon transitions here

        while not_p:
             # Mark the next unmarked state and create a row for it in the next list.
            arr = [not_p[0]]
             # For each input symbol, calculate the set of states that can be reached from the current state with that symbol
            for i in range(0, len(self.alphabet)):
                w = ''
                for letter in not_p[0]:
                    arr2 = a[self.S.index(letter)][i]
                    if arr2 not in w:
                        w += arr2
                arr.append(w) # Add the resulting set of states to the row.
            # If the set of states has not already been processed, add it to the list of unmarked states.
                if w not in p:
                    not_p.append(w)
            b.append(arr) #add it to the next listt
        # Mark the current state as used and remove it from the list of unmarked states.
            p.append(not_p[0])
            not_p.remove(not_p[0])

    # Merge equivalent states in the next array
        c = []
        # add the unique elements to c

        [c.append(un) for un in b if un not in c]
        #go over each row
        for r in c:
            #move through all eleemnst of tehe row
            for i in range(0, len(r)):
                # If an element is an empty string
                if r[i] == '':
                    r[i] = 'empty' #set as emphty (string)

        trans = []
        for r in c:
            #go over each alphabet letter
            for i in range(0, len(self.alphabet)):
                        # Create a transition tuple of the form (current_state, letter, next_state) and append it to trans

                arr = [r[0], self.alphabet[i], r[i + 1]]
                trans.append(arr)

        states = []
        #iterate over eveery row of the trasnsiitons
        for r in trans:
            #if it s not in states yet, add it
            if r[0] not in states:
                states.append(r[0])

        res = []
        #iterate over each state from the final states
        for state in self.final_states:
            for new in states:
                if state in new:        # If the final state is in the current state, append the current state to `res`

                    res.append(new)

        #initialize and create the new version of the automaton with diff arguments
        resulting_fa = finiteAutomaton(self.initial_states[0], res, self.alphabet, trans, states)
        return resulting_fa