# %%
import pandas as pd
import numpy as np
from IPython.display import YouTubeVideo
import matplotlib.pyplot as plt
import math
print("Hello Notebook")

# %%
2**3

# %%
math.pi

# %%

# %%
plt.plot([2, 4, 10, 7])

# %%
video = YouTubeVideo('5JDNc_jX2OY')
display(video)

# %%

p = np.linspace(0, 20, 100)
plt.plot(p, np.sin(15*p))
plt.show()


# %%
df = pd.read_csv(
    'https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/iris.csv')
df.sample(10)

# %% [markdown]
# $$ax^2+bx+c=0$$

# %% [markdown]
#
