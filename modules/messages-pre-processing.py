import pandas as pd
from tqdm import tqdm
from datetime import datetime
import numpy
import emoji
import re

filepath = ""
savepath = ""

def remove_emoji(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.split() if not any(i in str for i in emoji_list)])

    return clean_text

tqdm.pandas(desc="Progress")

print("Loading file...")

df = pd.read_csv(filepath)

print("Removing extra spaces...")

df['data'] = df['data'].progress_apply(lambda x: re.sub("\s\s+", " ", x))

print('Removing emojis...')

df['data'] = df['data'].progress_apply(lambda x: remove_emoji(x))

print("Removing empty rows...")

df['data'].replace('', numpy.nan, inplace=True)

df.dropna(subset=['data'], inplace=True)

print("Converting Unix Epoch to Datetime...")

df['timestamp'] = df['timestamp'].progress_apply(lambda x: datetime.fromtimestamp(x * 1e-3))

print("Saving file...")

df.to_csv(savepath, index=None, header=True)