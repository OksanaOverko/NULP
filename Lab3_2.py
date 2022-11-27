import re
import pandas as pd

valid = []
emails = pd.Series(['test text @test.com', 'test@mail.ua', 'test.2ua', 'test@pp'])
print(emails)

for i in range(len(emails)):
    valid.append(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9.\-+_]+\.[a-z]+", emails[i]))

print("Valid emails:")
val_em = pd.Series(valid)
print(val_em)
