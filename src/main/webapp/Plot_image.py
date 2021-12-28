import re
import glob
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from keras.preprocessing.image import load_img

dir_name = 'frame/'

# Get list of all files in a given directory
list_of_files = glob.glob(dir_name + '*')

# sort all files numerically
list_of_files.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

images = []
for file_path in list_of_files:
    img = load_img(file_path, color_mode="rgb", target_size=(224, 224), interpolation="nearest")
    images.append(img)
    print(file_path)

fig = plt.figure(figsize=(8., 8.))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(7, 7),  # creates 2x2 grid of axes
                 axes_pad=0,  # pad between axes in inch.
                 )

for ax, im in zip(grid, images):
    # Iterating over the grid returns the Axes.
    ax.imshow(im)
    ax.grid(False)
    ax.axis('off')

    # Hide axes ticks
    ax.set_xticks([])
    ax.set_yticks([])

fig.savefig('test.png')
