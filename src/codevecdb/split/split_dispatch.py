import os

from src.codevecdb.parse_code import batchParseCodeAndInsert
from src.codevecdb.split.get_language import get_language



def split_file_to_function(file):
    print(file)
    file.save('uploads/' + file.filename)  # 保存文件到指定路径
    with open(os.path.join('uploads', file.filename), 'r') as f:
        content = f.read()
    language = get_language(file.filename)
    extracted_functions = []


    semantics = batchParseCodeAndInsert(extracted_functions)
    print(semantics)
