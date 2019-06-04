from .main import Refine, tqdm

class NLP(Refine):
    def __init__(self):
        super().__init__()

    def next_sentence_prediction(self, inp_path, out_path, sep='. ', enc='utf8'):
        """
        Read lines from input file and split sentences by [SEP].
        ex1) In:"A[SEP]B[SEP]C[SEP]D.\n" -> Out:"A[SEP]\tB[SEP]\nC[SEP]\tD[SEP]\n" 
        ex2) In:"A[SEP]B[SEP]C[SEP]\n D[SEP]E[SEP]\n" -> \
             Out:"A[SEP]\tB[SEP]\nC[SEP]\tD[SEP]\n"
        """

        num_lines = sum(1 for line in open(inp_path, "r", encoding=enc))
        lines = super().readline(inp_path, enc)
        with open(out_path, "w", encoding=enc) as out:
            remainder = []
            for line in tqdm(lines, total=num_lines):
                if not line:
                    break
                start = 0
                while True:
                    end = line.find(sep, start)
                    if end == -1:
                        break
                    remainder.append(line[start:end+len(sep)])
                    start = end + len(sep)
                for i, sen in enumerate(remainder[:-1]):
                    if i % 2 == 0:
                        out.write(sen+"\t")
                    else:
                        out.write(sen+'\n')
                        
