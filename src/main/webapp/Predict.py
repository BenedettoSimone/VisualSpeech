from keras.preprocessing.image import load_img
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image


def predict():
    model = load_model('model_4.h5', compile=False)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    img = load_img('test.png', color_mode="grayscale", target_size=(224, 224), interpolation="nearest")

    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_batch = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_batch)
    prediction_class = np.argmax(prediction, axis=1)

    class_names = ["Stop navigation", "Excuse me", "I am sorry", "Thank you", "Good bye", "I love this grace",
                   "Nice to meet you", "You are welcome", "How are you", "Have a good time", "Begin", "Choose",
                   "Connection", "Navigation", "Next", "Previous", "Start", "Stop", "Hello", "Web"]
    print(class_names[prediction_class[0]])
    print(prediction_class[0])

    return class_names[prediction_class[0]]

