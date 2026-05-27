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

MAX_LEN = 600

!wget https://cdn.freecodecamp.org/project-data/sms/train-data.tsv
!wget https://cdn.freecodecamp.org/project-data/sms/valid-data.tsv

train_file_path = "train-data.tsv"
test_file_path = "valid-data.tsv"

# cell 3: get data and pop labels off

headers = ["class", "msg"]

train_data = pd.read_csv(train_file_path, sep='\t', names=headers)
test_data = pd.read_csv(test_file_path, sep='\t', names=headers)

train_dataset = train_data["msg"]
train_labels = np.array([1 if label=="spam" else 0 for label in train_data["class"]])
test_dataset = test_data["msg"]
test_labels = np.array([1 if label=="spam" else 0 for label in test_data["class"]])

# cell 4: clean data



# cell 5

def predict_message(pred_text):
    
    # Model logic goes here

    vectorization_layer = keras.layers.TextVectorization(
      max_tokens=MAX_LEN,
      output_mode='int',
      output_sequence_length=MAX_LEN
    )
    vectorization_layer.adapt(train_labels)
    
    model = keras.Sequential([
      
      keras.layers.Embedding(
        
      )
    ])
    
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
