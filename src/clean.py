from .utils import Refine
from tqdm import tqdm
import re

class clean_kor(Refine):
    def __init__(self):
        super().__init__()
        self.sub1 = re.compile('[^ .?!/@$%~|0-9|ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기, 특수기호 일부를 제외한 모든 글자
        self.sub2 = re.compile('[\s]+')  # white space duplicate
        self.sub3 = re.compile('[\.]+')  # full stop duplicate
        
    def apply(self, inp_path, out_path, encoding='utf8'):
        """
        This function will clean the text.
        It will remain only korean characters, numbers, and some special symbols.

        """
        with open(out_path, "w", encoding=encoding) as out:
            num_line = sum(1 for line in open(inp_path, "r", encoding=encoding))
            lines = super().readline(inp_path, encoding)
            for line in tqdm(lines, desc="cleaning", total=num_line):
                if not line:
                    break
                else:
                    cleaned = self.sub1.sub('', line.strip()) 
                    cleaned = self.sub2.sub(' ', cleaned)
                    cleaned = self.sub3.sub('.', cleaned) 
                    if not cleaned:
                        continue
                    out.write(cleaned+'\n')
        print("process done, saved at {}".format(out_path))