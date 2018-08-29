from textblob import TextBlob
def amazon(review):
	analysis = TextBlob(review)
	return str(analysis.sentiment.polarity)