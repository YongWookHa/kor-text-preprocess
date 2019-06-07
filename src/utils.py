class Refine():
    def __init__(self):
        pass

    def readline(self, inp_path, encoding='utf8'):
        with open(inp_path, "r", encoding=encoding) as f:
            line = f.readline()
            while line:
                yield line
                line = f.readline()
                