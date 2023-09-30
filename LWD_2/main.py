from simple_iteration import simple_iteration as simp
from seidel import seidel as sd
import secondary_functions as sf
import numpy as np

np.seterr(over="ignore")

sf.test(sd)
sf.test(simp)