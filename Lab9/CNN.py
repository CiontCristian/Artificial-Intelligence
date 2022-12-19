
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = (x_train / 255.0)
x_test = (x_test / 255.0)

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

model = Sequential([
    Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
    MaxPooling2D(pool_size=2),
    Flatten(),
    Dense(10, activation='softmax'),
])

model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
    x_train,
    to_categorical(y_train),
    batch_size=1,
    epochs=3,
    validation_data=(x_test, to_categorical(y_test)),
)

'''
Epoch 1/3
60000/60000 [==============================] - 60s 998us/step - loss: 0.2598 - accuracy: 0.9228 - val_loss: 0.1313 - val_accuracy: 0.9618
Epoch 2/3
60000/60000 [==============================] - 60s 1ms/step - loss: 0.1276 - accuracy: 0.9623 - val_loss: 0.1002 - val_accuracy: 0.9686
Epoch 3/3
60000/60000 [==============================] - 59s 984us/step - loss: 0.1017 - accuracy: 0.9702 - val_loss: 0.0936 - val_accuracy: 0.9706
'''
