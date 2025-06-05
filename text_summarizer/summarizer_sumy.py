from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

parser = PlaintextParser.from_string(text, Tokenizer("english"))
summarizer = LexRankSummarizer()
summary = summarizer(parser.document, sentences_count=3)

for sentence in summary:
    print(sentence)
