from flask import Flask, request

from src.rest.save_data import save_to_parquet

app = Flask(__name__)


@app.route("/upload_data", methods=["POST"])
def upload_data():
    return save_to_parquet()


if __name__ == "__main__":
    app.run()
