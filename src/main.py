#import the 2 classes
from grammar import Grammar
from automaton import finiteAutomaton
'''
#declare the terminal & non-terminal symbols, as well as the transitions for the VARIANT 17
v_n = ['S','A','B','C']
v_t= ['a','b','c','d']
a= v_t 

p = {'S':['dA'],'A':['aB','bA'],'B':['bC','aB','d'],'C':['cB']}

#create the grammar object and pass the necessary arguments
my_grammar = Grammar(v_n,v_t,p,a)

#assign the automaton as the returned result of the method FA_Converter
my_automaton = my_grammar.FA_Converter()

#Set how many strings we want to be generated
num_strings = 5
print('')
print('Strings generated:')
for i in range(num_strings):
    string = my_grammar.StringGenerator() #generate string

word = input('Enter the word you want to check: ')
if my_automaton.StringChecker(word):
    print('The input word satisfies criteria.')
else:
    print('The input word does not satisfy criteria.')
    '''
    
S = ['S','A','B','C']
initial_states = 'S'
final_states = 'C'
alphabet = ['a','b','c']
transitions_list =[['S','a','S'],['S','a','A'],['A','b','A'],['B','b','C'],['A','a','B'],['B','a','S'],]

final_finite_automaton = finiteAutomaton(initial_states,final_states,alphabet,transitions_list,S)
dfa = final_finite_automaton.DFA_Converter()
print("Automaton Information:")
print(f"S = {dfa.S}")
print(f"Alphabet: {dfa.alphabet}")
print(f"Initial state(s): {dfa.initial_states}")
print(f"Final state(s): {dfa.final_states}")
print("Transitions:")
for r in dfa.transitions_list:
    print(f"{r[0]} --{r[1]}--> {r[2]}")