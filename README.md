# GPT-3 Translator
Translation scripts using GPT-3 API.

Make sure you have a valid API Token to use GPT-3. Get yours at https://beta.openai.com/.
Create a file named secrets.py with the variable API_Token with your valid token.

I have tried to use all GPT-3 engines to reach the results and the only that gives back an accurate result is DAVINCI.

OpenAI module is required
$ pip install openai

secrets.py (ignored): Create your own in your local machine.
  -- API_Token = "YOUR AWESOME API"

prompt.py: Contain the training content for the predictive model
  -- en_ru

en-ru.py: Translate English to Russian
