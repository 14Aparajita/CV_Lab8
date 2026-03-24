from tensorflow.keras import layers, models

def build_model():
    inputs = layers.Input(shape=(32,32,3))

    x = layers.Conv2D(32,(3,3),padding='same')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.SeparableConv2D(64,(3,3),padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    x = layers.MaxPooling2D()(x)

    x = layers.SeparableConv2D(128,(3,3),padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)
    x = layers.MaxPooling2D()(x)

    x = layers.GlobalAveragePooling2D()(x)
    x = layers.Dense(128,activation='relu')(x)

    outputs = layers.Dense(10,activation='softmax')(x)

    return models.Model(inputs,outputs)
