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

# cell 3: clean up data

train_dataset = tf.data.experimental.CsvDataset(
    filenames=train_file_path,
    record_defaults=[tf.string, tf.string],
    header=False,     
    field_delim='\t' 
)

test_dataset = tf.data.experimental.CsvDataset(
    filenames=test_file_path,
    record_defaults=[tf.string, tf.string],
    header=False,     
    field_delim='\t' 
)

# pop labels off & clean data

def pad_and_truncate(text):
    padding = tf.strings.repeat(" ", MAX_LEN)
    padded_text = tf.strings.join([text, padding])
    
    return tf.strings.substr(padded_text, 0, MAX_LEN)

train_labels = train_dataset.map(lambda *cols: cols[0])
train_dataset = train_dataset.map(lambda *cols: cols[1])
test_labels = test_dataset.map(lambda *cols: cols[0])
test_dataset = test_dataset.map(lambda *cols: cols[1])

train_dataset = train_dataset.map(pad_and_truncate)
test_dataset = test_dataset.map(pad_and_truncate)

# cell 4



# cell 5

def predict_message(pred_text):
    
    # Model logic goes here
    
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
