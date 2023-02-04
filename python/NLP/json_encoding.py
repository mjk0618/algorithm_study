'''
import json
import os


with open("klue_nli_dev.json", "r", encoding="cp949") as f:
    content = f.raed()

data = json.loads(content)

encoded_content = json.dump(data, ensure_ascii=False).encode('utf-8')

with open("klue_nli_dev_2.json", "wb") as f:
    f.write(encoded_content)

f.close()
'''

import json
import os
import codecs

with codecs.open("content/Korpora/klue-nli/klue_nli_train.json", "r", encoding="utf-8") as f:
    content = f.read()

data = json.loads(content)

# encoded_content = json.dumps(data, ensure_ascii=False)

# with open("klue_nli_train.json", "w", encoding="utf-8") as f:
#     f.write(encoded_content)

# f.close()