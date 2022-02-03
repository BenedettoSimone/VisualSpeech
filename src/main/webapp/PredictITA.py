from keras.preprocessing.image import load_img
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image


def predict_ita():
    model = load_model('2_adam_30epR.h5', compile=False)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    img = load_img('test.png', color_mode="grayscale", target_size=(224, 224), interpolation="nearest")

    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_batch = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_batch)
    prediction_class = np.argmax(prediction, axis=1)

    class_names = ["Buongiorno", "Automobili", "Regali", "Telefono", "Università", "Come stai",
                   "Tutto bene", "Dobbiamo studiare", "Andiamo a casa", "Prendiamo un caffè"]
    print(class_names[prediction_class[0]])
    print(prediction_class[0])

    return class_names[prediction_class[0]]

