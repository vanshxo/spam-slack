import os
import joblib
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError




app=Flask(__name__)
slack_bot_token = os.getenv('SLACK_BOT_TOKEN')
slack_signing_token = os.getenv('SLACK_SIGNING_TOKEN')



client =WebClient(slack_bot_token)

model = joblib.load("artifacts/models/svm_model.joblib")
vectorizer = joblib.load("artifacts/models/tfidf_vectorizer.joblib")

# Define function for spam prediction
def predict_spam(text):
    text_tfidf = vectorizer.transform([text])  # Vectorize the input text
    prediction = model.predict(text_tfidf)     # Predict spam or ham
    return 'spam' if prediction == 1 else 'ham'

@app.route("/slack/events", methods=["POST"])
def slack_events():

    slack_event=request.get_json()

    if "challenge" in slack_event:
        return jsonify({"challenge": slack_event["challenge"]})
    
    if "event" in slack_event:
        event = slack_event["event"]
        if event.get("type") == "message" and "subtype" not in event.get("user")!='U07T34RCBJA':
            channel = event.get("channel")
            user_message = event.get("text")
            
            
            prediction=predict_spam(user_message)

            if prediction=='spam':
                response_message = "Your message seems like spam. Please avoid sending spam messages."
            else:
                response_message = "Thanks for the message!"
            try:
                client.chat_postMessage(channel=channel, text=response_message)
            except SlackApiError as e:
                print(f"Error sending message: {e.response['error']}")

        return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(port=3000)
