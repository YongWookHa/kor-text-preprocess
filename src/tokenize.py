from .utils import Refine
from tqdm import tqdm
from konlpy.tag import Mecab
from os.path import normpath

class Tokenizer(Refine):
    def __init__(self, args):
        super().__init__()

        if args.mecab:
            self.cls = self.mecab
            self.args = [normpath(args.input), normpath(args.output), args.encoding]
            if args.morphs + args.nouns + args.pos != 1:
                print("Please select ONE method in [morphs, nouns, pos]")
                raise ValueError
            if args.morphs:
                self.method = Mecab().morphs
            elif args.nouns:
                self.method = Mecab().nouns
            elif args.pos:
                self.method = Mecab().pos
            else:
                print("found no method in [morphs, nouns, pos]")
                raise ValueError
        else:
            print("Tokenizer class indicate error: {} not available"\
                .format())
            raise ValueError

    def apply(self):
        self.cls(*self.args)

    def mecab(self, inp_path, out_path, encoding='utf8'):
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
                    if type(applied[0]) == tuple: # pos
                        for tup in applied[:-1]:
                            out.write(tup[0] + tup[1] + ' ')
                        out.write(applied[-1][0] + applied[-1][1] + '\n')
                    else:
                        for token in applied[:-1]: # morphs & nouns
                            out.write(token + ' ')
                        out.write(applied[-1] + '\n')
                        
        print("process done, saved at {}".format(out_path))
