import json
import pathlib

import matplotlib.pyplot as plt

user_path = pathlib.Path.home() / "KeyboardInputRecord.json"

data = json.load(open(user_path, "r"))

keys = sorted(data.keys(), key=lambda x: -data[x])
values = [data[i] for i in keys]

plt.plot(keys, values)
plt.show()
