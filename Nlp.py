# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:00:08 2022

@author: ziggy
"""

import nltk
paragraph=  """Speech on APJ Abdul Kalam: Dr. APJ Abdul Kalam is not a new name.
            He served India as the 11th president. He was born on 15 October 1931 in Rameswaram, Tamil Nadu.
            Because of his works in the field of science and especially missile and rockets,
            he is also called the Missile Man of India. He was a famous scientist. 
            He worked with organizations like DRDO (Defense Research and Development Organization)
            and ISRO (Indian Space Research Organization).
            He was a real gem of India. He proved that with determination and hard work anything can be achieved.
            He is one of the many leaders in India who has plenty of admirers. 
            He served the nation for only one term and left us for always on 27 July 2015 due to cardiac arrest.
            """
sentence=nltk.sent_tokenize(paragraph) 
word= nltk.word_tokenize(paragraph)           