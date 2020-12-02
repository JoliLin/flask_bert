import numpy as np
import torch
from transformers import BertTokenizer#, BertModel
from pipeline.BertAdapter import BertModel
from pipeline.training_handler import handler
from pipeline.tokenizer import FullTokenizer
from scipy.special import softmax
from pipeline import model

class inference:
    def __init__(self, string=''):
        self.string = [string]
        self.seq_len = 300

        self.tokenizer = BertTokenizer.from_pretrained('./bert-base-chinese')

    def process(self, x):
        x_ = [self.tokenizer.encode(i, add_special_tokens=True, max_length=300, padding='max_length', truncation=True) for i in x]

        return x_

    def testing_data(self):
        x  = torch.LongTensor(self.process(self.string))
        return (x, torch.LongTensor([0]))

handle = handler()
model_name = 'model_0.pt'
model_path = handle.save+model_name

def load():
    #setting
    model_ = model.CustomBertCls( BertModel, './bert-base-chinese', handle.trainable, classes=3 )
    handle.setting(model_, model_name=model_name)

    return model_
    
def run( string, model_ ):
    inf = inference(string)
    testing = inf.testing_data()
    test_loader = handle.torch_data(testing)

    y_pred = handle.predict(model_, test_loader, model_path)
    i = y_pred[0]
    s_ = softmax(np.array(i))
    label = np.argmax(i)
    
    return label.item(), s_[label]
