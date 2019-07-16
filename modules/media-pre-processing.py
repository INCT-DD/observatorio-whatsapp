import pandas as pd
from tqdm import tqdm
from datetime import datetime
import numpy
import emoji
import re

filepath = ""
savepath = ""

tqdm.pandas(desc="Progress")

print("Loading file...")

df = pd.read_csv(filepath)

print("Correcting empty rows...")

df['data'].replace('', numpy.nan, inplace=True)

print("Converting Unix Epoch to Datetime...")

df['timestamp'] = df['timestamp'].progress_apply(lambda x: datetime.fromtimestamp(x * 1e-3))

print("Saving file...")

df.to_csv(savepath, index=None, header=True)