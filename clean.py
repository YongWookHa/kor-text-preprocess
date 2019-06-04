from .main import Refine, tqdm
import re

class clean_kor(Refine):
    def __init__(self):
        super().__init__()
        self.hangul = re.compile('[^ .?!/@$%~|0-9|ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기, 특수기호 일부를 제외한 모든 글자
        # self.hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
        
    def clean(self, inp_path, out_path, enc='utf8'):
        """
        This function will clean the text.
        It will remain only korean characters, numbers, and some special symbols.

        """
        with open(out_path, "w", encoding="utf8") as out:
            num_line = sum(1 for line in open(inp_path, "r", encoding="utf16"))
            lines = super().readline(inp_path, enc)
            for line in tqdm(lines, desc="cleaning", total=num_line):
                if not line:
                    break
                else:
                    cleaned = self.hangul.sub('', line)
                    if not cleaned:
                        continue
                    out.write(cleaned)