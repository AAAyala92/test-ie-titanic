import pandas as pd


def extract_titles(name):
    if "." in name:
        return name.split()[0]
    else:
        raise ValueError


print(__name__)

if __name__ == "__main__":
    print(extract_titles("Mr. John Doe"))
