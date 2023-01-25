from CSP import *
from ac3 import *


def printOut(game):
	index = 0
	values = list(game.domains.values())
	for _ in range(len(game.game)):
		for _ in range(len(game.game)):
			print("|",end="")
			print(str(values[index])[1:-1], end="")
			index += 1
		print("|")


def main():
	game = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
		[9, 0, 0, 3, 0, 5, 0, 0, 1],
		[0, 0, 1, 8, 0, 6, 4, 0, 0],
		[0, 0, 8, 1, 0, 2, 9, 0, 0],
		[7, 0, 0, 0, 0, 0, 0, 0, 8],
		[0, 0, 6, 7, 0, 8, 2, 0, 0],
		[0, 0, 2, 6, 0, 9, 5, 0, 0],
		[8, 0, 0, 2, 0, 3, 0, 0, 9],
		[0, 0, 5, 0, 1, 0, 3, 0, 0]]
	problem = CSP(game)
	AC3(problem)
	printOut(problem)


if __name__=="__main__":
	main()

