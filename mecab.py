from .main import Refine, tqdm
from konlpy.tag import Mecab

class mecab(Refine):
    def __init__(self, method):
        super().__init__()
        self.m = Mecab()
        method_available = ['morphs', 'nouns', 'pos']
        if method == method_available[0]:
            self.method = self.m.morphs
        elif method == method_available[1]:
            self.method = self.m.nouns
        elif method == method_available[2]:
            self.method = self.m.pos
        else:
            print("mecab method indicate error: {} not in {}".format(\
                method, method_available))
            raise ValueError

    def apply(self, inp_path, out_path, enc='utf8'):
        num_lines = sum(1 for line in open(inp_path, "r", encoding=enc))
        lines = super().readline(inp_path, enc)
        with open(out_path, "w", encoding=enc) as out:
            for line in tqdm(lines, total=num_lines):
                if not line:
                    break
                else:
                    applied = self.method(x)
                    if not applied:
                        break
                    for token in applied:
                        out.write(token + ' ')
                    out.write('\n')
        print("process done, saved at {}".format(out_path))
