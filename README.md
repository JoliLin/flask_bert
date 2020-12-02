# Flask with BERT
----
Using flask to demo a fine-tuned BERT model

# Requirement
----
+ flask
+ numpy
+ scipy
+ torch
+ transformers
+ boto3

# Structure
----
flaskapp_demo<br>
-__storm_health__<br>
---model_0.pt<br>
-bert-base-chinese<br>
---bert_config.json<br>
---pytorch_model.bin<br>
---vocab.txt<br>
-pipeline<br>
-template<br>
---index.html<br>
---prototype.html<br>
---server_information.html<br>
-storm_prototype.py<br>
-wsgi.py<br>

# Setting
----
```
1. git clone
2. Download these three files for using offline BERT and put them in bert-base-chinese*
https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-vocab.txt
https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-config.json
https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-chinese-pytorch_model.bin
3. Rename
bert-base-chinese-vocab.txt -> vocab.txt
bert-base-chinese-config.json -> bert_config.json
bert-base-chinese-pytorch_model.bin -> pytorch_model.bin
4. Download fine-tuned model and put it in __storm_health__
https://drive.google.com/file/d/1tvV4TV36HtoqZxUrSnB3EKx_VYFNvYUk/view?usp=sharing
```
