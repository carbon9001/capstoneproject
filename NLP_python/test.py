from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import config
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.tokenize

def tokenize_origin(paragraphs):

	raw_sents = reduce(lambda x, y: x + y, [nltk.tokenize.sent_tokenize(p.strip()) for p in paragraphs if p.strip()!=''])
	return filter(lambda s: len(s.split(" "))>2, raw_sents)



filename = '271590.csv'

df = pd.read_csv(config.COMMENTSPATH+filename)
df = df['review_content']
allcomments = list()
allcomments = tokenize_origin(df)

print len(allcomments)
ng_tfidf=TfidfVectorizer(max_features=300, ngram_range=(2,4), stop_words=nltk.corpus.stopwords.words('english') + ["GTA5", "GTAV",'GTA'])
ng_tfidf=ng_tfidf.fit(allcomments)
result = ng_tfidf.transform(allcomments)
print sum(result,0)
print ng_tfidf.get_feature_names()[260]