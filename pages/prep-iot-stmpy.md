# State Machines in Micro Python

The state machines were so far expressed as diagrams, that means **pictures**.
In this part we are going to explore how we can implement the state machines as Python **code**.

The Microbit we are going to program does not run all Python code, but only a reduced set of it.
This subset is called MicroPython.
To run state machines on it, we will provide you with some code that serves as a template or a skeleton.
We create the state machines by manually translating a diagram step for step into a Python function that executes transitions. 


### Idea 1: Storing the State

In a "normally coded" program, the progress of an application is stored indirectly in the form of the program counter.
Simplified said, the program remembers **in which line** it currently is, and then proceeds, statement for statement, including loops and branches.

To execute a state machine, we use an **extra variable that explicitly stores the current state** of the program, and which corresponds to the state in the state machine.
For simplicity, we store the variable as a string, which corresponds to the name of the state from the diagram.


### Idea 2: A Transition Function

Now that we have taken care of the control state by an explicit variable, we need to think how to implement the transitions. 
Let's think again what a transition actually does:

- It is triggered by an event.
- It takes a state machine from one state to another state.
- While it executes, it can do some actions and maybe decide between alternative branches.


To implement transitions, we define a function that executes them. 
The method receives 4 parameters; 

* `state` - the current state of the machine
* `event` - the event that triggered the machine
* `timers` - a variable to start and stop timers

The listing below shows the transition function for a simple example. (Ignore the parameter `self` for now.)
Within the method, we place first an if-statement which distinguishes the different states of the machine.
It has one branch for each state.
Within each state branch, there is another if-statement, which distinguishes the different events.

```python
``` 

Within these branches, we then do actions; 

* start a timer
* stop a timer
* call a function to do something in the Microbit, like switching on an LED
* change a variable (use self)







```python
class StateMachineA(StateMachine):
	
	def step(self, state, event, timers):
		if state == "initial":
			state = "s1"
		elif state == "s1":
			if event == "t1":
				self.start_timer("t2", 3000)
				display.show(event)
				self.state = "s2"
			elif event == "C":
				self.start_timer("t1", 1000)
		elif self.state == "s2":
			if event == "t2":
				self.start_timer("t1", 1000)
				display.show(event)
				self.state = "s1"
```

We are going to 


