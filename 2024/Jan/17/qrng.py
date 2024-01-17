from projectq import MainEngine
from projectq.ops import H, Measure

eng = MainEngine()

q1 = eng.allocate_qubit()

H | q1

Measure | q1

eng.flush()

print(f"Measured: {int(q1)}")
