import ast

stop_word = {'ctx', 'value', 'name', 'values', 'kw_defaults', 'kwonlyargs', 'kwarg', 'n', 'body', 'args', 'defaults',
             'vararg', 'arguments'}
file_contents = []


def format_constant_string(constant_string):
    return "'{}\'".format(constant_string)


class FuncParser(ast.NodeVisitor):

    def __init__(self):
        self.librairies = set()
        self.subLibraries = set()
        self.methodAttributes = set()
        self.classAttributes = set()
        self.attributes = set()

    def visit_Load(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Store(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Str(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Num(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Module(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_arguments(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Expr(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_FunctionDef(self, node):
        file_contents.append([node.__class__.__name__])
        file_contents.append([node.name])
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Call(self, node):

        attrib = node.func
        if attrib.__class__.__name__ == 'Attribute':
            # When calling a function like  triangle.perimeter(a,b)
            if attrib.value.__class__.__name__ == 'Attribute':
                expression = self.visit_Attribute(attrib.value) + '.' + attrib.attr
            elif attrib.value.__class__.__name__ == 'Constant':
                expression = format_constant_string(attrib.value.value) + '.' + attrib.attr
            elif attrib.value.__class__.__name__ == 'Call':
                expression = attrib.value.func.id
            else:
                expression = attrib.value.id + '.' + attrib.attr
            self.attributes.add(expression)
        elif attrib.__class__.__name__ == 'Name':
            self.classAttributes.add(attrib.id)
            self.methodAttributes.add(attrib.id)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_arg(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_BinOp(self, node):
        temp = (node.op)
        op = "BinOp: " + temp.__class__.__name__ + "()"
        file_contents.append([op])
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Import(self, node):
        for elt in node.names:
            self.librairies.add(elt.name)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_ImportFrom(self, node):
        self.librairies.add(node.module)
        # self.subLibraries.add([node.module,[elt.name for elt in node.names]])
        ast.NodeVisitor.generic_visit(self, node)

    def visit_alias(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Attribute(self, node):
        attrib = node.value
        if attrib.__class__.__name__ == 'Attribute':
            return ast.NodeVisitor.generic_visit(self, attrib)
        elif attrib.__class__.__name__ == 'Constant':
            expression = format_constant_string(attrib.value) + '.' + node.attr
            self.attributes.add(expression)
        else:
            self.attributes.add(node.value.id + '.' + node.attr)
            return node.value.id + '.' + node.attr

        # ast.NodeVisitor.generic_visit(self, node)

    def generic_visit(self, node):
        ast.iter_fields(node)
        ast.NodeVisitor.generic_visit(self, node)

