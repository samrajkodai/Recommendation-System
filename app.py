import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tag_pool = ['Communication',
     'Self-learning',
     'Attitude',
     'Listening Skills',
     'Leadership',
     'Adaptability',
     'Team Player',
     'python Django',
     'Postgre SQL',
     'Restframe work',
     'Angular',
     'Cypress',
     'Selenium',
     'Java',
     'SaaS sales experience',
     'Lead generation',
     'Problem solving',
     'good candidate',
     'communication',
     'communication engineering',
     'python',
     'python 34',
     'SQL',
     'java program',
     'java demo',
     "applicant is good",
     "data science",
     "datascience",
     "nlp for datascience",
     'nlp',
     'machine learning',
     'deep learning',
     'learning',
     'i am a java developer',
     'junior java developer',
     'junior nlp engineer',
     'junior data scientist',
     'selenium developer',
     'restframe',
     'i am new python 3.10',
     'django developer',
     'django restframework'
     ]

new_list = tag_pool

label = []
for i in range(len(tag_pool)):
    label.append([tag_pool[i]])

# converting our tags into dataframe
df = pd.DataFrame(label, columns=['text'])

x = df['text']

# applying tf-idf for converting sentence into vectors
cv = TfidfVectorizer(stop_words='english')
x = cv.fit_transform(x)

# performing cosine similarity for x with respect to x
cos_sim = cosine_similarity(x, x)

# find the indices  
indices = pd.Series(df['text'].index, df['text'])


## making predictions
def get_recommendations(title,cosine_sim=cos_sim):
    result=[]
    try:
        # checking the user input with recommendation model
        idx=indices[title]
        similarity_scores=enumerate(cosine_sim[idx])
        similarity_scores=sorted(similarity_scores,key=lambda x:x[1],reverse=True)
        similarity_index=[i[0] for i in similarity_scores if i[1]!=0]
        for i in df['text'].iloc[similarity_index]:
            result.append(i)
    except:
        # checking the user input with list
        for i in range(len(df['text'])):
            if title.lower() in df['text'][i].lower():
                result.append(df['text'][i])
    
    return result


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        final = get_recommendations(request.form['new_freq'])
        return jsonify(final)

    return None


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('./main.html', mynewlist=new_list)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
