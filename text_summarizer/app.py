from flask import Flask, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    input_text = ""
    if request.method == "POST":
        input_text = request.form["input_text"]
        parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary_sentences = summarizer(parser.document, sentences_count=3)
        summary = " ".join(str(sentence) for sentence in summary_sentences)
    return render_template("index.html", summary=summary, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
