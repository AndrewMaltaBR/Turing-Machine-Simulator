__author__ = "Andrew M. Silva and Estela M. Vilas Boas"
# Alphabet
Initial = ">"
Zero = "0"
One = "1"
Void = "_"

# Moviments
Prev = -1
Stop = 0
Next = 1

# Final states
qsim = "sim"
qnao = "nao"

# Problem states
# Structure: (current char, new char, next state, moviment)
q0 = [(Initial, Initial, 0, Next), (Zero, Initial, 1, Next), (One, Initial, 3, Next), (Void, Void, qsim, Stop)] # Search the first char
q1 = [(Initial, Initial, qnao, Stop), (Zero, Zero, 1, Next), (One, One, 1, Next), (Void, Void, 2, Prev)] # Go to final search a zero
q2 = [(Initial, Initial, qsim, Stop), (Zero, Void, 5, Prev), (One, One, qnao, Stop), (Void, Void, qnao, Stop)] # Verify if the the final char is zero
q3 = [(Initial, Initial, qnao, Stop), (Zero, Zero, 3, Next), (One, One, 3, Next), (Void, Void, 4, Prev)] # Go to final search a one
q4 = [(Initial, Initial, qsim, Stop), (Zero, Zero, qnao, Stop), (One, Void, 5, Prev), (Void, Void, qnao, Stop)] # Verify if the final char is one
q5 = [(Initial, Initial, 0, Next), (Zero, Zero, 5, Prev), (One, One, 5, Prev), (Void, Void, qnao, Stop)] # Just returning to begin

States = [q0, q1, q2, q3, q4, q5]

# Configure default input
def ReadInput():
	return list(Initial+input("Input: "))

# Simulate machine execution
def SimpleTuringSimulate(States, Input, pos=0, q=0):
	# Include a Void char when pos is on final
	if(pos+1 == len(Input)):
		Input.append(Void)

	# Show current pass
	print("(q"+str(q)+", "+"".join(Input[0:pos+1])+", "+"".join(Input[pos+1:])+")")

	# If done, do that
	if(q == qsim or q == qnao):
		return

	# If not done, go to next pass
	Q = States[q]
	for condition in Q:
		if(Input[pos] == condition[0]):
			Input[pos] = condition[1]
			break

	SimpleTuringSimulate(States, Input, pos+condition[3], condition[2])

while(True):
	Input = ReadInput()
	SimpleTuringSimulate(States, Input)