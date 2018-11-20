from keras.layers import Conv3D, MaxPool3D, Flatten, Dense
from keras.layers import Dropout, Input, BatchNormalization
from sklearn.metrics import confusion_matrix, accuracy_score
from plotly.offline import iplot, init_notebook_mode
from keras.losses import categorical_crossentropy
from keras.optimizers import Adadelta
import plotly.graph_objs as go
from matplotlib.pyplot import cm
from keras.models import Model
import numpy as np
import keras
import h5py

#init_notebook_mode(connected=False)
#matplotlib inline
with h5py.File('full_dataset_vectors.h5', 'r') as dataset:
    print(list(dataset.keys()))
    x_train = dataset["X_train"][:]
    print("x_train ", x_train.shape)
    print(x_train)
    x_test = dataset["X_test"][:]
    print("x_test ", x_test.shape)
    print(x_test)
    y_train = dataset["y_train"][:]
    print("y_train ", y_train.shape)
    print(y_train)
    y_test = dataset["y_test"][:]
    print("y_test ", y_test.shape)
    print(y_test)

xtrain = np.ndarray((x_train.shape[0], 4096, 3))
xtest = np.ndarray((x_test.shape[0], 4096, 3))

## convert to 1 + 4D space (1st argument represents number of rows in the dataset)
xtrain = xtrain.reshape(x_train.shape[0], 16, 16, 16, 3)
xtest = xtest.reshape(x_test.shape[0], 16, 16, 16, 3)

## convert target variable into one-hot
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)
print("xtest new shape ", xtrain)
print("y_test new shape", y_test.shape)
"""
with h5py.File("train_point_clouds.h5", "r") as points_dataset:
    #print(list(points_dataset.keys()))
    digits = []
    for i in range(10):
        digit = (points_dataset[str(i)]["img"][:],
                 points_dataset[str(i)]["points"][:],
                 points_dataset[str(i)].attrs["label"])
        digits.append(digit)
    print(len(list(points_dataset.keys())))

x_c = [r[0] for r in digits[0][1]]
print(len(x_c))
y_c = [r[1] for r in digits[0][1]]
z_c = [r[2] for r in digits[0][1]]
"""
#trace1 = go.Scatter3d(x=x_c, y=y_c, z=z_c, mode='markers',
#                      marker=dict(size=12, color=z_c, colorscale='Viridis', opacity=0.7))

#trace = go.Mesh3d(x=x_c,y=y_c,z=z_c,color='#FFB6C1',opacity=0.50)
#iplot([trace])

#data = [trace1]
#layout = go.Layout(height=500, width=600, title= "Digit: "+str(digits[0][2]) + " in 3D space")
#fig = go.Figure(data=data, layout=layout)
#iplot(fig)

"""
data = [
    go.Surface(
        z=z_data.as_matrix()
    )
]
layout = go.Layout(
    title='Mt Bruno Elevation',
    autosize=False,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)
"""
