import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class ATS1:
    def __init__(self, top_n_keywords=10):
        additional_stopwords = {'knowledge', 'required', 'plus', 'experience', 'looking', 'framework', 'skill', 'like'}
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = set(stopwords.words('english'))
        if additional_stopwords:
            self.stopwords.update(additional_stopwords)
        self.vectorizer = TfidfVectorizer()
        self.top_n_keywords = top_n_keywords

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())
        tokens = [word for word in tokens if word.isalpha()]  # Remove punctuation and non-alphabetic tokens
        tokens = [word for word in tokens if
                  word not in self.stopwords]  # Remove stopwords and additional non-essential words
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
        return ' '.join(tokens)

    def fit(self, job_description, cv_text):
        # Preprocess the texts
        self.preprocessed_job_description = self.preprocess_text(job_description)
        self.preprocessed_cv_text = self.preprocess_text(cv_text)

        # Vectorize the texts using TF-IDF
        self.tfidf_matrix = self.vectorizer.fit_transform(
            [self.preprocessed_job_description, self.preprocessed_cv_text])

    def calculate_similarity(self):
        # Compute cosine similarity
        similarity = cosine_similarity(self.tfidf_matrix[0:1], self.tfidf_matrix[1:2])
        return similarity[0][0] * 100

    def extract_keywords(self):
        # Extract important keywords based on TF-IDF scores
        feature_names = self.vectorizer.get_feature_names_out()
        job_desc_vector = self.tfidf_matrix[0].toarray()[0]

        # Extract top N keywords based on their TF-IDF scores
        top_indices = job_desc_vector.argsort()[-self.top_n_keywords:][::-1]
        important_keywords = {feature_names[i] for i in top_indices}

        # Extract keywords not in CV
        job_tokens = set(self.preprocessed_job_description.split())
        cv_tokens = set(self.preprocessed_cv_text.split())
        missing_keywords = important_keywords - cv_tokens

        return important_keywords, missing_keywords

    def ats_result(self, job_description, cv_text):
        self.fit(job_description, cv_text)
        similarity = self.calculate_similarity()

        # Extract important and missing keywords
        important_keywords, missing_keywords = self.extract_keywords()
        return similarity, missing_keywords

class ATS2:
    def __init__(self, top_n_keywords=10):
        self.nlp = spacy.load('en_core_web_sm')
        self.vectorizer = TfidfVectorizer()
        self.top_n_keywords = top_n_keywords

    def extract_keywords(self, text):
        doc = self.nlp(text)
        keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ'] and not token.is_stop]
        return keywords

    def calculate_similarity(self, text1, text2):
        vectors = self.vectorizer.fit_transform([text1, text2])
        return cosine_similarity(vectors)[0, 1]

    def match(self, cv_text, job_desc_text):
        cv_keywords = self.extract_keywords(cv_text)
        job_desc_keywords = self.extract_keywords(job_desc_text)

        # Join keywords back into a string
        cv_keywords_text = ' '.join(cv_keywords)
        job_desc_keywords_text = ' '.join(job_desc_keywords)

        # Calculate similarity
        similarity_score = self.calculate_similarity(cv_keywords_text, job_desc_keywords_text)

        return similarity_score

    def missing_keywords(self, cv_text, job_desc_text):
        cv_keywords = set(self.extract_keywords(cv_text))
        job_desc_keywords = set(self.extract_keywords(job_desc_text))

        missing_keywords = job_desc_keywords - cv_keywords

        return missing_keywords

    def ats_result(self, job_description, cv_text):
        similarity_score = (self.match(cv_text, job_description))*100
        missing_keywords = self.missing_keywords(cv_text, job_description)

        return similarity_score, list(missing_keywords)[:self.top_n_keywords]


def similarity_score(job_description,cv_text):
    ats1 = ATS1(top_n_keywords=10)
    ats2 = ATS2(top_n_keywords=10)
    similarity1, missing_keywords1 = ats1.ats_result(job_description=job_description,
                                                     cv_text=cv_text)
    similarity2, missing_keywords2 = ats2.ats_result(job_description=job_description,
                                                     cv_text=cv_text)
    similarity = (similarity1+similarity2)/2
    missing_keywords = list(missing_keywords1)+list(missing_keywords2)

    return similarity, missing_keywords


