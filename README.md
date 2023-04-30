# PY_CHATBOTS

## Learning materials in chatbot development

### Python Chatbots

* 1.build_a_bot

Course covering stateless systems using regex & spacy word vectors to
derive intent and entities in natural language. Moves on to state and
pending state systems, policies and natural language understanding using
the `rasa_nlu` library. Problem with this part of the course - significant
breaking changes since it was written mean that I have not been able to
reproduce the results.

***

* 2.host_a_bot

Additional dependency: ngrok for server client mediation. To install on mac:
`brew install --cask ngrok`.

Once installed, start a ngrok server with:
`ngrok http 5000`
This establishes an https endpoint which gets forwarded on the specified port.

Create a [facebook app](https://developers.facebook.com/docs/messenger-platform).

Update a **gitignored** secrets file with your facebook app's access token. Locate this
file at `./ignore_me/secrets.toml`. Generic format for this file as below, update with
your details:

```
[fb_messenger]
# VERIFY_TOKEN should be any long random string, used to confirm with Facebook
# that the server is open for business. Generate a random alphanumeric in terminal:
# `openssl rand -base64 38`
VERIFY_TOKEN = '<insert your verify token>'
PAGE_ACCESS_TOKEN = '<insert your page access token>'

```

Start a flask server in a new terminal from the project root with:

`FLASK_APP=2.host_a_bot/server.py flask run`

You will then need to go back to your Facebook dashboard and register the webhook. This
will require your https callback url from your ngrok server interface and your
VERIFY_TOKEN value from secrets.toml.

At this point you'll need enough flask knowledge to get the callback authenticated for
fb. See Todo.

***

<p style="color:red;">TODO:</p>

* [Course Author tutorial on deploying a chatbot to Facebook messenger.](https://www.datacamp.com/tutorial/facebook-chatbot-python-deploy)
* This has been attempted up to the callback authentication stage. There seems to be an
issue with the instructions. Adjusting the `@app.route("/webhook")` to
`@app.route("/")` results in 404 -> 200, but FB is not liking it.
Read through [flask documentation](https://flask.palletsprojects.com/en/2.2.x/) on
specifying URLS, because the webhook url is resulting in a 404 not found.
Read through [FB webhook documentation](https://developers.facebook.com/docs/messenger-platform/webhooks)
to ensure the server handles the request in  the expected way - possible breaking
changes.

* [Explore the RASA training.](https://rasa.com/docs/rasa/) - Once oriented around v3,
`./1.build_a_bot/` could be updated for compatoble with latest v of API.

### Prompt Engineering with LLMs

Notes from free [DeepLearning.AI course](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/).
