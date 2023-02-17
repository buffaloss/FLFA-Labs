# Laboratory work no.1: Intro to formal languages. Regular grammars. Finite Automata.

### Course: Formal Languages & Finite Automata
### Author: Golban Beatricia, FAF-213, variant 17

----

## Objectives:

* Understand what a language is and what it needs to have in order to be considered a formal one.

* Provide the initial setup for the evolving project that you will work on during this semester.

* Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches).

* Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms.

* Create a separate folder where you will be keeping the report.

* Implement a type/class for your grammar.

* Add one function that would generate 5 valid strings from the language expressed by your given grammar.

* Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton.

* For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it.


## Implementation description

The laboratory work consists of one main Python file and 2 classes: Grammar and finiteAutomaton. 

Firstly, I declared the set of non-terminal and terminal characters in lists, as well as creating a dictionary for storing the set of trasitions. 

```
v_n = ['S','A','B','C']
v_t= ['a','b','c','d']
a= v_t 

p = {'S':['dA'],'A':['aB','bA'],'B':['bC','aB','d'],'C':['cB']}
```

In order to avoid the issue of key duplication when trying to validate strings, simple lists were chosen because they are easier to  use for the represenation of the state transitions. This way, it is possible to iterate through and modify them as needed throughout the code.

The grammar class takes multiple arguments: non-terminal and terminal symbols, a set of transitions and an alphabet and passes them to the constructor.

```
class Grammar:
    def __init__(self,Vn,Vt,P,alpha):
        self.Vn = Vn
        self.Vt = Vt
        self.P = P
        self.alphabet = alpha
        self.string = '' 
        self.transitions= []
```

This class has 2 methods: 
* StringGenerator - generates a string by randomly choosing transitions that correspond the the non-terminal characters, until it reaches a terminal symbol and a final state.
* FA_Converter - converts the grammar into a finite automaton by taking the non-terminal and terminal characters, creating a list of all the transitions that were used. 

The finiteAutomaton class tkaes as arguments the initial and final states, the alphabet and the list of transition functions.

```
class finiteAutomaton:
    def __init__(self, initial_states, final_states, alphabet, transitions_list):
        self.initial_states = initial_states
        self.final_states = final_states
        self.alphabet = alphabet
        self.transitions_list = transitions_list
```
The finiteAutomaton class has one method:
* StringChecker - takes an input string and verifies if it can be derived from the Finite Automaton's transition function by checking if the initial and final states match, and then then the alphabet itself. It then tries to find the transitions that were used for this input string.

For more detailed explanations, refer to the documented source code.

## Conclusions / Screenshots / Results

To sum up, the program for the first laboratory work is able to generate valid strings from the language expressed by the given grammar, with a set of specific rules.Furthermore, it has the functionality of converting the grammar to a Finite Automaton and can verify if an inout string from the user corresponds to the set of rules & transitions, by checking if it can be obtained via the state transition from it.

Below it can be observed 2 examples of how the program code firstly generates 5 strings,then takes as input some word and checks if it fits the criteria.

## Practical Results
![Invalid string](/Reports/Images/lab1_img1.png)

![Valid string](/Reports/Images/lab1_img2.png)