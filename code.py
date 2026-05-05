import os
import pickle

def run(cmd):
    os.system(cmd)  # ❌ command injection

password = "admin123"  # ❌ hardcoded secret

data = pickle.loads(b"cos\nsystem\n(S'ls'\ntR.")  # ❌ unsafe deserialization