
import pandas as pd
import numpy as np
from time import time
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

early_stopping = EarlyStopping()

train=pd.read_csv('train_features.csv')
train_labels=pd.read_csv('train_labels.csv')
test=pd.read_csv('test_features.csv')
submission=pd.read_csv('sample_submission.csv')

start = time()

def min_max_scaler(mylist):
  max = mylist[0]
  min = mylist[0]
  newlist = []
  for i in range(len(mylist)):
    if max < mylist[i]: max = mylist[i]
    if min > mylist[i]: min = mylist[i]


  for j in range(len(mylist)):
    newelement = (mylist[j] - min) / (max - min) 
    newlist.append(newelement)

  return newlist

train = train[['id','time','acc_x','acc_y','acc_z','gy_x','gy_y','gy_z']]
train = train.assign(loc = lambda x: np.hypot(np.hypot(x['gy_x'],x['gy_y']),x['gy_z']))
train = train.assign(acc = lambda x: np.hypot(np.hypot(x['acc_x'],x['acc_y']),x['acc_z']))
train = train.assign(move = lambda x: np.sqrt(np.sqrt(x['gy_x']**2+x['acc_x']**2)**2+np.sqrt(x['gy_y']**2+x['acc_y']**2)**2+np.sqrt(x['gy_z']**2+x['acc_z']**2)**2))
train = train.assign(angle_x = lambda x: np.arctan(-x['acc_x']/np.sqrt(x['acc_z']**2 + x['acc_y']**2))*180/np.pi)
train = train.assign(angle_y = lambda x: np.arctan(-x['acc_y']/np.sqrt(x['acc_x']**2 + x['acc_z']**2))*180/np.pi)
train = train.assign(angle_z = lambda x: np.arctan(-x['acc_z']/np.sqrt(x['acc_x']**2 + x['acc_y']**2))*180/np.pi)
train = train.assign(roll = lambda x: np.arctan(x['acc_y']/x['acc_z']))
train = train.assign(pitch = lambda x: np.arctan(x['acc_x']/x['acc_z']))

test = test[['id','time','acc_x','acc_y','acc_z','gy_x','gy_y','gy_z']]
test = test.assign(loc = lambda x: np.hypot(np.hypot(x['gy_x'],x['gy_y']),x['gy_z']))
test = test.assign(acc = lambda x: np.hypot(np.hypot(x['acc_x'],x['acc_y']),x['acc_z']))
test = test.assign(move = lambda x: np.sqrt(np.sqrt(x['gy_x']**2+x['acc_x']**2)**2+np.sqrt(x['gy_y']**2+x['acc_y']**2)**2+np.sqrt(x['gy_z']**2+x['acc_z']**2)**2))
test = test.assign(angle_x = lambda x: np.arctan(-x['acc_x']/np.sqrt(x['acc_z']**2 + x['acc_y']**2))*180/np.pi)
test = test.assign(angle_y = lambda x: np.arctan(-x['acc_y']/np.sqrt(x['acc_x']**2 + x['acc_z']**2))*180/np.pi)
test = test.assign(angle_z = lambda x: np.arctan(-x['acc_z']/np.sqrt(x['acc_x']**2 + x['acc_y']**2))*180/np.pi)
test = test.assign(roll = lambda x: np.arctan(x['acc_y']/x['acc_z']))
test = test.assign(pitch = lambda x: np.arctan(x['acc_x']/x['acc_z']))

X=tf.reshape(np.array(train.iloc[:,2:]),[-1, 600,14])
y = tf.keras.utils.to_categorical(train_labels['label']) 
#sgd = tf.keras.optimizers.SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)

from tensorflow.keras.layers import Dropout,Flatten
model = Sequential()
model.add(LSTM(64,input_shape=(600,14)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(61, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X,y, epochs=100, batch_size=128, validation_split=0.2)


print(f'\nWhen hidden layers are 2, Elapse training time : {time() - start} seconds\n')
start = time()
loss_and_metrics = model.evaluate(X, y)
print(f'\nLoss : {loss_and_metrics[0]:.6}')
print(f'Accuracy : {loss_and_metrics[1]*100:.6}%')
print(f'When hidden layers are 2, Elapse test time : {time() - start} seconds')
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend(['train_loss', 'val_loss'])
plt.show()

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.ylabel('acc')
plt.xlabel('epoch')
plt.legend(['train_accuracy', 'val_accuracy'])
plt.show()


test_X=tf.reshape(np.array(test.iloc[:,2:]),[-1, 600, 14])

prediction=model.predict(test_X)
submission.iloc[:,1:]=prediction
submission.to_csv('submission.csv', index=False)