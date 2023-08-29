import os

INPUT_DIR = "data/input"

def list_inputs():
    inputs = []
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".mp4"):
            components = os.path.splitext(filename)[0].split(',')
            inputs.append([components[0], components[1], ','.join(components[2:])])
    
    return sorted(inputs, key=lambda x: int(x[0]))
