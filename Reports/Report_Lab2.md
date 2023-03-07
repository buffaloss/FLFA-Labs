# Laboratory work no.2: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.
### Course: Formal Languages & Finite Automata
### Author: Golban Beatricia, FAF-213, variant 17

----

## Objectives:

1. Understand what an automaton is and what it can be used for.

2. Continuing the work in the same repository and the same project, the following need to be added:
   
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):
      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
        
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.


## Implementation description

For this laboratory work, I implemented new functionalities.

Firstly, I created a function that classifies the grammar according to its type in the Chomsky hierarchy.

There are 3 main steps in this function: 

- checking if the grammar is of type 3 (regular), by verifying if all productions have at most two symbols, and the first symbol is a terminal or non-terminal and the second symbol is a non-terminal or epsilon. 

- checking if the grammar is of type 2 (context-free), by verifying if all productions have at most two symbols, and both symbols are non-terminals. 

- checking if the grammar is of type 1 (context-sensitive), by verifying if any production has a right-hand side that is shorter than its left-hand side, and all symbols on the right-hand side are non-terminals. 

- checking if the grammar is of type 0 (unrestricted), by verifying if any production has a right-hand side that contains symbols not in the grammar or the left-hand side of the production.

Below can be observed the first part, which refers to the Type 3 classification, which is Regular Grammars.

```
# verify if it is of type 3
     if all(len(production) <= 2 and (production[0].islower() or production[0].isupper()) and
           (len(production) == 1 or production[1].isupper() or production[1] == 'ε') for symbol in grammar for production in grammar[symbol]):
        return "Type 3 (regular)"
```

Secondly, I implemented a functionn for converting a finite automaton to a regular grammar. The function RG_Converter() takes a regular finite automaton and converts it into a regular grammar by extracting the production rules from the automaton's transition list, creating a dictionary of rules for each non-terminal symbol. It then returns a new grammar object that has the same start and final states, production rules, and alphabet as the original automaton.

```
  for transition in self.transitions_list:
                string = ''
                if transition[0] == key:
                    for i in range(1,len(transition)):
                        string = string +transition[i]
                    values.append(string)
```

Thirdly, I added a method that check whether the FA is deterministic or not.It iterates through the transitions of the automaton and checks whether there are any non-deterministic transitions, and whether all input symbols from each state are included in the input alphabet. If there are no non-deterministic transitions and all input symbols are included in the input alphabet, the automaton is classified as deterministic.

```
for transition in self.transitions_list: 
                if transition[0] == letter: 
                    if transition[1] in reps: 
                        return 'Non-Deterministic Finite Automaton'
                    reps.append(transition[1])
            if set(reps) != set(self.alphabet):
                return 'Non-Deterministic Finite Autmaton'
```
If none of those conditions were met, then the function returns 'Deterministic Finite Automaton'.

Lastly, but not least, I implemented a function that converts a non-deterministic finite automaton (NDFA) to a deterministic finite automaton (DFA). It does this by simulating the NDFA with epsilon transitions and constructing a table of states and input symbols that lead to new sets of states.

```
while not_p:
            arr = [not_p[0]]
            for i in range(0, len(self.alphabet)):
                w = ''
                for letter in not_p[0]:
                    arr2 = a[self.S.index(letter)][i]
                    if arr2 not in w:
                        w += arr2
                arr.append(w) 
                if w not in p:
                    not_p.append(w)
            b.append(arr)
            p.append(not_p[0])
            not_p.remove(not_p[0])
```

Then, it merges equivalent states in the table and creates a new set of transitions between the merged states. Finally, it creates a new deterministic finite automaton with the merged states and transitions and returns it.


For more detailed explanations, refer to the documented source code.

## Conclusions 

To sum up,in this laboratory work, I implemented several functions that are essential in understanding the Chomsky hierarchy, conversion of a finite automaton to a regular grammar, and determining whether the FA is deterministic or non-deterministic.

By classifying the grammar based on the Chomsky hierarchy, I was able to understand the different types of grammars and how they can be used in language recognition. Additionally, the implementation of the conversion of a finite automaton to a regular grammar allowed me to understand how grammars can be used to recognize a language.  Finally, implementing a functionality that converts an NDFA to a DFA gave me insights into how we can use deterministic automata to recognize languages that can be represented by non-deterministic automata.

Overall, these functions are essential in understanding the basics of automata and formal language theory, and they provide a foundation for more complex language recognition tasks.