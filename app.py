from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I'm Mike with devops and github actions. I just pushed my build to GHA and that went to my ECR. From there I created a EC2 instance to pull the image so I can build the app. It was successful!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
