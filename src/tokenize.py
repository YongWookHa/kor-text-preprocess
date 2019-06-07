from .utils import Refine
from tqdm import tqdm
from konlpy.tag import Mecab

class Tokenizer(Refine):
    def __init__(self, tokenizer_class, method):
        super().__init__()
        if tokenizer_class == 'mecab':
            self.cls = Mecab()
            if method == 'morphs':
                self.method = self.cls.morphs
            elif method == 'nouns':
                self.method = self.cls.nouns
            elif method == 'pos':
                self.method = self.cls.pos
            else:
                print("mecab method indicate error: {} not available"\
                    .format(method))
                raise ValueError
        else:
            print("Tokenizer class indicate error: {} not available"\
                .format(tokenizer_class))
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
                        continue
                    for token in applied[:-1]:
                        out.write(token + ' ')
                    out.write(applied[-1]+'\n')
        print("process done, saved at {}".format(out_path))
