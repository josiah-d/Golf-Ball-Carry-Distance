# imports
import matplotlib.pyplot as plt
from glob2 import glob

from clean_json import CleanJSON

if __name__ == '__main__':
    cj = CleanJSON()
    cj.cleaned_paths()
    cj.to_csv()
