﻿import re
import traceback
from deoplete.source.base import Base

# ------------------------------- KEYWORD -------------------------------------------------------------------------

file = open("ruby_complete", "r", encoding="utf_8")
data = file.readlines()
file.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'Bignyanco'
        self.filetypes = ['ruby']
        self.mark = '[neo_dictionary2]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data
            dic.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()
