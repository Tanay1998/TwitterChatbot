A neural chatbot using sequence to sequence model with
attentional decoder. This is a fully functional chatbot.

This is based on Google Translate Tensorflow model 
https://github.com/tensorflow/models/blob/master/tutorials/rnn/translate/

By Tanay Kothari and Anirudh Jain

<h2>Usage</h2>

Step 1: Download
wget -c 'https://raw.githubusercontent.com/Marsan-Ma/chat_corpus/master/twitter_en.txt.gz'
Unzip it
Run data_preprocess.py to preprocess the twitter dataset
Run data.py to generate the train and test files
Run data_vocab.py to generate the vocab files
Note: all this is currently available in 'twitter' folder

Step 2: update config.py file<br>
Change DATA_PATH to where you store your data (this assumes your data is currently stored in a folder called 'twitter')

Step 4:
python3 chatbot.py --mode [train/chat] <br>
If mode is train, then you train the chatbot. By default, the model will
restore the previously trained weights (if there is any) and continue
training up on that.

If you want to start training from scratch, please delete all the checkpoints
in the checkpoints folder.

If the mode is chat, you'll go into the interaction mode with the bot.

By default, all the conversations you have with the chatbot will be written
into the file output_convo.txt in the processed folder. If you run this chatbot,
