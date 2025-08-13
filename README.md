# GPT-3 Tokenizer
Just a simple python class to make it easier to use tiktoken (gpt-3 tokenizer - cl100k_base)
## Usage :
Run ``git clone https://github.com/abgache/tokenizer.git`` in your project file and change the TXT_DATASET_PATH variable by the path of your dataset (TXT). 
add ``import tokenizer as tkn`` in the begining of all the scripts where you'll need the tokenizer and create the tokenizer using 
```python
tokenizer = tkn.create_tokenizer(text_limit=1000000)
```
### Functions :
**Print the model information:**
```python
tokenizer.summary()
```  
**Get all the tokens (in the tokenizer):**
```python
token_list = tokenizer.get_token_list()
```  
**Encode a token (give a token in input and it send it's token ID):**
```python
token = "on"
encoded_token = tokenizer.encode_token(token)
```  
**Decode a token (token ID to token):**
```python
token_id = 1
token = tokenizer.decode_token(token_id)
```  
**Tokenize a string (text to token_id list):**
```python
text = "This a small text."  
token_list = tokenizer.tokenize_string(text)
```  
**Save the tokenizer:**
```python
path = "tokenizer.json"
tokenizer.save(path)
```  
**Load the tokenizer:**
```python
path = "tokenizer.json"
tokenizer.load(path)
