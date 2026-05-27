try:
  # %tensorflow_version only exists in Colab.
  !pip install tf-nightly
except Exception:
  pass
import tensorflow as tf
import pandas as pd
from tensorflow import keras
!pip install tensorflow-datasets
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt

!wget https://cdn.freecodecamp.org/project-data/sms/train-data.tsv
!wget https://cdn.freecodecamp.org/project-data/sms/valid-data.tsv

train_file_path = "train-data.tsv"
test_file_path = "valid-data.tsv"

# cell 3: get data, separate labels, and clean messages

headers = ["class", "msg"]

train_data = pd.read_csv(train_file_path, sep='\t', names=headers)
test_data = pd.read_csv(test_file_path, sep='\t', names=headers)

train_dataset = train_data["msg"]
train_labels = np.array([1 if label=="spam" else 0 for label in train_data["class"]])
test_dataset = test_data["msg"]
test_labels = np.array([1 if label=="spam" else 0 for label in test_data["class"]])

vocabulary = {}
for msg in train_dataset:
  for word in msg.split():
    if word not in vocabulary:
      vocabulary[word] = 1
    else:
      vocabulary[word] += 1

VOCAB_SIZE = len(vocabulary)
MAX_LEN = len(max(train_message, key=lambda p: len(p.split())).split())

# onehot_encoded_train = [one_hot(message, VOCAB_SIZE) for message in train_dataset]

# train_dataset = keras.preprocessing.pad_sequences(train_dataset, maxlen=MAX_LEN, padding="post")
# test_dataset = keras.preprocessing.pad_sequences(test_dataset, maxlen=MAX_LEN, padding="post")

vectorizer = keras.layers.TextVectorization(max_tokens=VOCAB_SIZE, output_sequence_length=MAX_LEN)
vectorizer.adapt(train_dataset)
vectorized_train_dataset = vectorizer(train_dataset)
vectorized_test_dataset = vectorizer(test_dataset)

# cell 4: train model

model = keras.Sequential([
  keras.layers.Embedding(input_dim=VOCAB_SIZE, output_dim=128, input_length=MAX_LEN),
  keras.layers.Flatten(),
  keras.layers.Dense(1, activation="softmax")
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(vectorized_train_dataset, train_label, validation_data=(vectorized_test_dataset, test_label), epochs=100)

# cell 5

def predict_message(pred_text):
    
    vectorized_text = vectorizer(pred_text)
    prediction = model.predict(vectorized_text)[0][0]
    prediction = [prediction, "ham" if np.round(prediction) == 0 else "spam"]
    
    return (prediction)

pred_text = "how are you doing today?"

prediction = predict_message(pred_text)
print(prediction)



def test_predictions():
    test_messages = [
        "how are you doing today",
        "sale today! to stop texts call 98912460324",
        "i dont want to go. can we try it a different day? available sat",
        "our new mobile video service is live. just install on your phone to start watching.",
        "you have won £1000 cash! call to claim your prize.",
        "i ll bring it tomorrow. don t forget the milk.",
        "wow, is your arm alright. that happened to me one time too",
    ]

    test_answers = ["ham", "spam", "ham", "spam", "spam", "ham", "ham"]
    passed = True

    for msg, ans in zip(test_messages, test_answers):
        prediction = predict_message(msg)
        if prediction[1] != ans:
            passed = False

    if passed:
        print("You passed the challenge. Great job!")
    else:
        print("You haven't passed yet. Keep trying.")

test_predictions()
