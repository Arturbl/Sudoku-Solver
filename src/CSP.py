
class CSP:

	def __init__(self,game):
		self.game = game
		self.vars = list()
		self.constraints = list()
		self.domains = dict()
		self.neighbours = dict()
		self.populate_vars_domains(self.game)
		self.populate_constraints_neighbours()


	def populate_constraints_neighbours(self):
		for var in self.vars:
			new_domain= list() 
			for i in range(9):
				#check_Columns
				if (var.split()[0] +' '+ str(i)) !=var:
					self.constraints.append(([var, f'{int(var.split()[0])} {i}']))
					new_domain.append(f'{int(var.split()[0])} {i}') 

				#check_Lines
				if (str(i) + ' ' + var.split()[1]) !=var:
					self.constraints.append([var, f'{i} {int(var.split()[1])}'])
					new_domain.append(f'{i} {int(var.split()[1])}') 
			# Evaluate in clusters 
			row_cluster = (int(var.split()[1]) // 3) * 3
			column_cluster = (int(var.split()[0]) // 3) * 3
			for y in range(row_cluster, row_cluster + 3):
				for x in range(column_cluster, column_cluster + 3):
					coordenate = str(x) + ' ' + str(y)
					if coordenate != var:
						self.constraints.append([var, coordenate])
						if coordenate not in new_domain:
							new_domain.append(coordenate)
			self.neighbours[var] = new_domain

	def populate_vars_domains(self,game):
		for row in range(9):
			for column in range(9):
				self.vars.append(str(column)+' '+str(row))
				domain_for_coordenate= []
				if game[row][column] ==0:
					domain_for_coordenate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
				else:
					domain_for_coordenate.append(game[row][column])
				self.domains[str(column)+' '+str(row)] = domain_for_coordenate