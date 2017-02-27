from pycparser import c_parser, c_ast, parse_file

# A simple visitor for FuncDef nodes that prints the names and
# locations of function definitions.
class FuncDefVisitor(c_ast.NodeVisitor):

    def __init__(self):
        self._results = []

    def visit_FuncDef(self, node):
        self._results.append((node.decl.name, node.coord.line))

    def results(self):
        return self._results


class FunsGraph():

    def __init__(self, filepath):
        self.filepath = filepath

    def func_defs(self):
        ast = parse_file(self.filepath, use_cpp=True, cpp_args=r'-Iutils/fake_libc_include')
        v = FuncDefVisitor()
        v.visit(ast)

        yield from v.results()

        # with open(self.filepath, 'rt') as f:
        #     lines = f.readlines()


if __name__ == '__main__':
    test_filepath = 'memmgr.c'

    f = FunsGraph(test_filepath)

    for func_def in f.func_defs():
        print(func_def)

