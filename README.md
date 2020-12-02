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
