def is_valid(self, identifier):
	"""
	Return True if identifier is valid, always True in this base implementation.
	"""
	return True

class BinaryExpression(Node):
	def __init__(self, left, right, identifier):
		super().__init__(left, right)
		self.identifier = identifier
	def __str__(self):
		return f"({self.left} {self.identifier} {self.right})"

class BinaryOp(Node):
	def __init__(self, left, right, identifier):
		super().__init__(left, right)
		self.identifier = identifier
	def __str__(self):
		return f"({self.left} {self.identifier} {self.right})"

class UnaryOp(Node):
	def __init__(self, left, right, identifier):
		super().__init__(left, right)
		self.identifier = identifier
	def __str__(self):
		return f"({self.left} {self.identifier} {self.right})"

class NumberExpression(Node):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return f"{self.value}"

class VariableExpression(Node):
	def __init__(self, identifier):
		self.identifier = identifier
	def __str__(self):
		return f"{self.identifier}"

class AssignExpression(Node):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return f"{self.left} = {self.right}"

class VarAssignExpression(Node):
	def __init__(self, identifier):
		self.identifier = identifier
	def __str__(self):
		return f"{self.identifier}"

class VarCallExpression(Node):
	def __init__(self, identifier):
		self.identifier = identifier
	def __str__(self):
		return f"{self.identifier}"

class FuncCallExpression(Node):
	def __init__(self, identifier):
		self.identifier = identifier
	def __str__(self):
		return f"{self.identifier}"

class BreakExpression(Node):
	def __init__(self):
		pass
	def __str__(self):
		return "break"

class ContinueExpression(Node):
	def __init__(self):
		pass
	def __str__(self):
		return "continue"

class ReturnExpression(Node):
	def __init__(self):
		pass
	def __str__(self):
		return "return"

class Return(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"return {self.expression}"

class UnaryPlusExpression(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"{self.expression}"

class UnaryMinusExpression(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"{self.expression}"

class UnaryNotExpression(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"not {self.expression}"

class UnaryNegExpression(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"{self.expression}"

class UnaryEqExpression(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"{self.expression}"

class UnaryNotEqExpression(Node):
	def __init__(self, expression):
		self.expression = expression
	def __str__(self):
		return f"not {self.expression}"

class UnaryPlusEqExpression(Node):