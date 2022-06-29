#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:37:21 2022

@author: jhonnyrv
"""




from selenium import webdriver
from datetime import datetime
from time import sleep 
#from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from sentiment import *
import requests
from bs4 import BeautifulSoup
import json
import random
import pandas as pd
import re
import ast
from mongoDB import *
from itertools import permutations
import sys
from dateutil import parser
import numpy as np
from webdriver_manager.chrome import ChromeDriverManager
from mongoDB import *
import time





# =============================================================================
# Google translator scraping
# =============================================================================
    
class google_translator:
    
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2 })
        # driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options) 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.google.com/search?q=traductor+google&oq=traductor+google&aqs=chrome..69i57.6156j0j7&sourceid=chrome&ie=UTF-8') 


    def choose_idiom1(self, idm):
        
        try:
            
                                            
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[1]/div[1]/div').click()
            inputElement = self.driver.find_element_by_id("sl_list-search-box")
            inputElement.send_keys(idm)
            inputElement.send_keys(Keys.ENTER)
            
        except:
            try:
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[1]/div[1]/div').click()
                inputElement = self.driver.find_element_by_id("sl_list-search-box")
                inputElement.send_keys(idm)
                inputElement.send_keys(Keys.ENTER)
                
            except:
                pass
        
        try:
            
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[6]/g-expandable-container/div/g-expandable-content/span/div/div[1]/span/span').click()
            print('Idioma no encontrado')
       
        except:
            pass
        
    def choose_idiom2(self, idm):
        
        try:
            
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[1]/div[2]/div').click()
            inputElement = self.driver.find_element_by_id("tl_list-search-box")
            inputElement.send_keys(idm)
            inputElement.send_keys(Keys.ENTER)
            
        except:
            try:
                                                   
                self.driver.find_element_by_xpath(' /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[1]/div[2]/div').click()
                inputElement = self.driver.find_element_by_id("tl_list-search-box")
                inputElement.send_keys(idm)
                inputElement.send_keys(Keys.ENTER)
                
            except:
                pass

        try:
            
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[6]/g-expandable-container/div/g-expandable-content/span/div/div[1]/span/span').click()
            print('Idioma no encontrado')
       
        except:
            pass
        
    def text_translate1(self, text):
        
        self.driver.execute_script("window.scrollTo(0, 0);")
        
        
        try:     
                                                            
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[1]/span/span').click()
            
        except:
            try:
                
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[1]/span/span').click()
            except:
                pass
            
        try:
            
            inputElement = self.driver.find_element_by_id("tw-source-text-ta")
            inputElement.send_keys(text)
            
            
        except:
            
            pass
        
        try:
            
            time.sleep(0.3)
                                                    
            b1 = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[3]')
                                             
            siz1 =  b1.size
            siz1['height']
            a = b1.get_attribute('innerHTML')
            soup = BeautifulSoup(a, features="lxml")
            
            
            spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
            df1 = [span.get_text() for span in spans_traduction]
            
            
            return df1[0]
    
    
        except:
            
            try:
                time.sleep(0.3)                          
                b1 = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[3]/div/div[2]')
                siz1 =  b1.size
                siz1['height']
                a = b1.get_attribute('innerHTML')
                soup = BeautifulSoup(a, features="lxml")
        
        
                spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
                df1 = [span.get_text() for span in spans_traduction]
                
                
                return df1[0]
            
            except:
                
                try:
                                                            
                    b1 = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[1]/div[1]')
                    siz1 =  b1.size
                    siz1['height']
                    a = b1.get_attribute('innerHTML')
                    soup = BeautifulSoup(a, features="lxml")
            
            
                    spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
                    df1 = [span.get_text() for span in spans_traduction]
                    
                    
                    return df1[0]
                
                except:
                    b1 = self.driver.find_element_by_xpath(' /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[3]/div/div[2]')
                    siz1 =  b1.size
                    siz1['height']
                    a = b1.get_attribute('innerHTML')
                    soup = BeautifulSoup(a, features="lxml")
            
            
                    spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
                    df1 = [span.get_text() for span in spans_traduction]
                    
                    
                    return df1[0]
                    
                
        
    
    def text_translate(self, df, columns):
        
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.3)
         
        # =============================================================================
        # Eliminamos el texto     
        # =============================================================================
               
        try:     
                                                            
            self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[1]/span/span').click()
            
        except:
            try:
                
                self.driver.find_element_by_xpath('/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[1]/span/span').click()
            except:
                pass
        
        # =============================================================================
        # Enviamos el texto que vamos a traducir
        # =============================================================================
            
        try:
            
            inputElement = self.driver.find_element_by_id("tw-source-text-ta")
            inputElement.send_keys(df[columns])
            time.sleep(2)
            
        except:
            
            pass
            
        
        # =============================================================================
        # Agaramos el texto traducido y lo guardamos en una variable  
        # =============================================================================
                
        try:
            
            b1 = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[3]')
                                             
            siz1 =  b1.size
            siz1['height']
            a = b1.get_attribute('innerHTML')
            soup = BeautifulSoup(a, features="lxml")
            
            
            spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
            df1 = [span.get_text() for span in spans_traduction]
    
            df['text_traduction'] = df1[0]
            
            return df['text_traduction']
    
    
        except:
            
            try:
                                                        
                b1 = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[3]/div/div[2]')
                siz1 =  b1.size
                siz1['height']
                a = b1.get_attribute('innerHTML')
                soup = BeautifulSoup(a, features="lxml")
        
        
                spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
                df1 = [span.get_text() for span in spans_traduction]
        
                df['text_traduction'] = df1[0]
                
                
                
                return df['text_traduction']
            
            except:
                
                try:
                                                                                                            
                    b1 = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/g-expandable-container/div/div/div[2]/div[1]/div[1]')
                    siz1 =  b1.size
                    siz1['height']
                    a = b1.get_attribute('innerHTML')
                    soup = BeautifulSoup(a, features="lxml")
            
            
                    spans_traduction = soup.find_all('span', {'class' : 'Y2IQFc'})
                    df1 = [span.get_text() for span in spans_traduction]
            
                    df['text_traduction'] = df1[0]
                    
                    
                    
                    return df['text_traduction']
                
                except:
                    pass
                    
                pass
    
    
# =============================================================================
# Descargamos la data que vamos a traducir 
# =============================================================================

database = 'CarmenMelendez'
client = auth_mongo("nucleo.analitico", 'PzDyzpJwM5T;@dY', database)
df = extract_mongo(client, database, 't_aecarri_comentarios')


# =============================================================================
# Limpiamos la data
# =============================================================================

class normalization_data:
    
    def __init__(self):
        
        pass
    
    def remove_url(self, text):
        text = re.sub(r'http\S+', '', text)
        return text
        
    def remove_username(self, text):
        text = re.sub(r'@\S+', '', text)
        return text
    
    def remove_characters(self, text):
        text = re.sub(r"\/|\&|\||\°|\\","",str(text))
        return text
    
    def remove_line_breaks(self, text):
        text = re.sub(r"\n","",str(text))
        return text
    
    def remove_white_space_beginning_and_final(self, text):
        text = text.rstrip()
        text = text.lstrip()
        return text


a = normalization_data()  
df['text'] = df.apply(lambda x: a.remove_url(x['text']), axis=1)
df['text'] = df.apply(lambda x: a.remove_username(x['text']), axis=1)
df['text'] = df.apply(lambda x: a.remove_characters(x['text']), axis=1)
df['text'] = df.apply(lambda x: a.remove_line_breaks(x['text']), axis=1)
df['text'] = df.apply(lambda x: a.remove_white_space_beginning_and_final(x['text']), axis=1)

# =============================================================================
# Creamos una instancia de la clase google_translator
# =============================================================================
    
driver = google_translator()

# =============================================================================
# Elegimos el idioma del texto que vamos a introducir para traducir
# =============================================================================

driver.choose_idiom1('espa')

# =============================================================================
# Elegimos a que idioma queremos traducir
# =============================================================================

driver.choose_idiom2('ingl')

# =============================================================================
# Llamamos al metodo text_translate para traducir el texto
# =============================================================================

df = df.head(10)
df['text_traduction'] = df.apply(lambda x: driver.text_translate(x, 'text'), axis=1)




