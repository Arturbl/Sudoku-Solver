
def AC3(problem):
	queue = problem.constraints
	while queue:
		value = queue.pop(0)
		Xx = value[0]
		Xy = value[1]

		if revise(problem, Xx, Xy):
			if len(problem.domains[Xx]) == 0:
				print("There is no Solution")
				return False
			for Xk in problem.neighbours[Xx]:
				if Xk != Xy:
					queue.append([Xk, Xx])
	return True


def revise(problem, Xx, Xy):
	revised = False
	for value in problem.domains[Xx][:]:
		if not any(value != y for y in problem.domains[Xy]):
			problem.domains[Xx].remove(value)
			revised = True
	return revised
