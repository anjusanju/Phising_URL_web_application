import os
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
import ipaddress
import re
import urllib.request
from bs4 import BeautifulSoup
import socket
import requests
from googlesearch import search
import whois
from datetime import date, datetime
import time
from dateutil.parser import parse as date_parse
from urllib.parse import urlparse



class UNRD:
    class FeatureExtraction:
    features = []
    def __init__(self,url):
        self.features = []
        self.url = url
        self.domain = ""
        self.whois_response = ""
        self.urlparse = ""
        self.response = ""
        self.soup = ""

        try:
            self.response = requests.get(url)
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except:
            pass

        try:
            self.urlparse = urlparse(url)
            self.domain = self.urlparse.netloc
        except:
            pass

        try:
            self.whois_response = whois.whois(self.domain)
        except:
            pass

    def __init__(self):
        self.dataset = []
        self.x_train,self.x_test,self.y_train,self.y_test = [], [], [], []
        self.load_dataset()
        self.train_test_split()
        self.model = None
        self.result = []
        self.preprocess()
    def preprocess(self):
        self.initialize_algorithm()
        self.train_data()
    def load_dataset(self):
        self.dataset = pd.read_csv("UNRD.csv")
    def train_test_split(self):
        x_train,self.x_test,y_train,self.y_test=train_test_split(self.dataset['Label'], self.dataset["Binary Label"], test_size=0.01, random_state=7)
        self.x_train = []
        self.y_train = []
        for i in range(len(x_train)):
            try:
                if str(y_train[i]) in ['Attack ', 'Normal']:
                    self.x_train.append([str(x_train[i])])
                    self.y_train.append(str(y_train[i]))
            except:
                pass
        self.x_train='00'+pd.Series(self.x_train).astype(str)
        self.y_train=pd.Series(self.y_train).astype(str)
    def initialize_algorithm(self):
        self.model.gbc = pickle.load(file)(max_iter=50)
    def print_result(self):
        return self.result[0]
    