#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:59:23 2022

@author: thaaff
"""
'''
1. Determine if there are differences in NPS score by country.

    a. Are any differences statistically significant, and how did you decide?
    
2. Is there a difference in NPS by number of jobs posted?

    a. Are any differences statistically significant, and how did you decide?
    
3. Company leadership is interested in segmenting NPS data by company size, but we don’t collect the size of the company.
What segmentation strategy would you suggest based on the data available?

    a. Why did you choose that segmentation strategy?
    
    b. What would you suspect are 1-2 dangers from this approach, and how would you
    convey these to company leadership? Why is your strategy still viable despite those dangers?

4. What strategies/methodologies would you use to extract the most common themes in
verbatim responses from customers in the NPS survey?

    a. What are some themes in these responses? If you’re able to execute some code
    to find some themes, great, but don’t spend too much time here. 
    It’s more important to demonstrate your understanding of methodologies.
    
'''
import pandas as pd
country = pd.read_csv('/Users/thaaff/Downloads/indeedquantitativeuxresearcher/country (1) (2).csv')
verbatims = pd.read_csv('/Users/thaaff/Downloads/indeedquantitativeuxresearcher/verbatims (1) (2).csv')
jobs = pd.read_csv('/Users/thaaff/Downloads/indeedquantitativeuxresearcher/jobs (1) (2).csv')
nps = pd.read_csv('/Users/thaaff/Downloads/indeedquantitativeuxresearcher/nps (1) (2).csv')

by_country = country.groupby('billing_country_code').mean()

#%%
by_country = by_country.drop('advertiser_id', 'nps_scores', axis=1)











