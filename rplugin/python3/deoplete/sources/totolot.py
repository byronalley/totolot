import os
import re
import traceback
import pandas as pd
from deoplete.source.base import Base
from os.path import expanduser

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

rel_path = "repos/github.com/takkii/ruby-dictionary3/"
paths = [os.path.expanduser(os.path.join(p, rel_path)) for p in [
    "~/.cache/dein/",
    "~/.local/share/dein/",
    "~/.config/nvim/.cache/dein/",
    "~/.config/nvim/",
    "~/.vim/bundles"
]]

try:
    path = next(p for p in paths if os.path.exists(p))

    ruby_method = open(os.path.join(path, "autoload/source/ruby_method_deoplete"))
    rubymotion_method = open(os.path.join(path, "autoload/source/rubymotion_method"))
    rurima_list = open(os.path.join(path, "autoload/source/rurima_list"))

except StopIteration:
    print("Don't forget, Install dein plugin manager github repo takkii/ruby-dictionary3.")

index_ruby = list(ruby_method.readlines()) + list(rubymotion_method.readlines()) + list(rurima_list.readlines())

Seri = pd.Series(index_ruby)
sort_ruby = Seri.sort_index()
data_ruby = list(map(lambda s: s.rstrip(), sort_ruby))
ruby_method.close()
rubymotion_method.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'totolot'
        self.filetypes = ['ruby']
        self.mark = '[ruby-dictionary3]'
        rubymatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(rubymatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_ruby
            dic_sort = sorted(dic, key=lambda dic: dic[0])
            return dic_sort
        except Exception:
            traceback.print_exc()
