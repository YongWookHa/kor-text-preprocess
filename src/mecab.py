from .utils import Refine
from tqdm import tqdm
from konlpy.tag import Mecab

class mecab(Refine):
    def __init__(self, method, method_availables):
        super().__init__()
        self.m = Mecab()
        if method == method_availables[0]:
            self.method = self.m.morphs
        elif method == method_availables[1]:
            self.method = self.m.nouns
        elif method == method_availables[2]:
            self.method = self.m.pos
        else:
            print("mecab method indicate error: {} not in {}".format(\
                method, method_availables))
            raise ValueError

    def apply(self, inp_path, out_path, encoding='utf8'):
        num_lines = sum(1 for line in open(inp_path, "r", encoding=encoding))
        lines = super().readline(inp_path, encoding)
        with open(out_path, "w", encoding=encoding) as out:
            for line in tqdm(lines, total=num_lines):
                if not line:
                    break
                else:
                    applied = self.method(line)
                    if not applied:
                        break
                    for token in applied[:-1]:
                        out.write(token + ' ')
                    out.write(applied[-1]+'\n')
        print("process done, saved at {}".format(out_path))
