import pandas as pd
from sklearn.preprocessing import LabelEncoder

from matplotlib import pyplot as plt
import numpy as np
import math

def showHistograms(X, y, feature_dict, label_dict):
	fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,6))

	for ax,cnt in zip(axes.ravel(), range(4)):

		# set bin sizes
		min_b = math.floor(np.min(X[:,cnt]))
		max_b = math.ceil(np.max(X[:,cnt]))
		bins = np.linspace(min_b, max_b, 25)

		# plottling the histograms
		for lab,col in zip(range(1,4), ('blue', 'red', 'green')):
			ax.hist(X[y==lab, cnt],
				color=col,
				label='class %s' %label_dict[lab],
				bins=bins,
				alpha=0.5,)
		ylims = ax.get_ylim()

		# plot annotation
		leg = ax.legend(loc='upper right', fancybox=True, fontsize=8)
		leg.get_frame().set_alpha(0.5)
		ax.set_ylim([0, max(ylims)+2])
		ax.set_xlabel(feature_dict[cnt])
		ax.set_title('Iris histogram #%s' %str(cnt+1))

		# hide axis ticks
		ax.tick_params(axis="both", which="both", bottom="off", top="off",
			labelbottom="on", left="off", right="off", labelleft="on")

		# remove axis spines
		ax.spines["top"].set_visible(False) 
		ax.spines["right"].set_visible(False)
		ax.spines["bottom"].set_visible(False)
		ax.spines["left"].set_visible(False)

	axes[0][0].set_ylabel('count')
	axes[1][0].set_ylabel('count')

	fig.tight_layout()

	plt.show()



feature_dict = {i:label for i,label in zip(
                range(4),
                  ('sepal length in cm',
                  'sepal width in cm',
                  'petal length in cm',
                  'petal width in cm', ))}

df = pd.io.parsers.read_csv(
    filepath_or_buffer='iris.data',
    header=None,
    sep=',',
    )
df.columns = [l for i,l in sorted(feature_dict.items())] + ['class label']
df.dropna(how="all", inplace=True) # to drop the empty line at file-end

X = df[[l for i,l in sorted(feature_dict.items())]].values
y = df['class label'].values

enc = LabelEncoder()
label_encoder = enc.fit(y)
y = label_encoder.transform(y) + 1

label_dict = {1: 'Setosa', 2: 'Versicolor', 3:'Virginica'}

showHistograms(X, y, feature_dict, label_dict)

