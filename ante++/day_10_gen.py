import pathlib
import random

from tqdm import tqdm


def generate_data():
    data = []
    i = 0
    for _ in tqdm(range(1_000_000)):
        decision = random.random()
        if decision < 0.25:
            data.append(i + 1)
            i += 1
        elif decision < 0.4375:
            data.append(i + 2)
            i += 2
        else:
            data.append(i + 3)
            i += 3
    for i in range(7):
        random.shuffle(data)
    return "\n".join(str(i) for i in data)


(pathlib.Path(__file__).parent / "10.in").write_text(generate_data())
