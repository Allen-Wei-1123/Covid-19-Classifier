#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import re
import string


# In[14]:


file = pd.read_csv("fake-news/train.csv").apply(lambda x:x.astype(str).str.lower())


# In[15]:


file = pd.read_csv("fake-news/training-covid.csv")


# In[16]:


file.head()


# In[36]:


file.iloc[1].loc['text']


# In[18]:


keep_cols= ['text']
X = file[keep_cols]
y = file[['label']]


# In[19]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)


# In[20]:


import re
def preprocess(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]',' ',text)
    return text


# In[21]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[22]:


X_train[['text']]


# In[23]:


from nltk.corpus import stopwords
stopwordss = set(stopwords.words('english'))
vectorization = TfidfVectorizer(preprocessor = preprocess,stop_words = stopwordss )


# In[24]:


xv_train = vectorization.fit_transform(X_train['text']);
xv_test = vectorization.transform(X_test['text'])


# In[25]:


from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# In[26]:


LR = LogisticRegression()
clf = Pipeline(steps=[
    ('features',vectorization),
    ('model',LR)
])
clf.fit(X_train['text'],y_train)


# In[27]:


ans = clf.predict(X_test['text'])


# In[28]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, ans)


# In[29]:


import pickle


# In[30]:


pickle.dump(clf, open('model_covid.pkl','wb'))


# In[ ]:




