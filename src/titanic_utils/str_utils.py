import pandas as pd

def extract_titles(name):
    return name.split()[0]


print(__name__)

if __name__ == "__main__":
    print(extract_titles("Mr. John Doe"))