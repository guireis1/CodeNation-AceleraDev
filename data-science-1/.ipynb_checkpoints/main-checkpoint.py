#!/usr/bin/env python
# coding: utf-8

# # Desafio 3
# 
# Neste desafio, iremos praticar nossos conhecimentos sobre distribuições de probabilidade. Para isso,
# dividiremos este desafio em duas partes:
#     
# 1. A primeira parte contará com 3 questões sobre um *data set* artificial com dados de uma amostra normal e
#     uma binomial.
# 2. A segunda parte será sobre a análise da distribuição de uma variável do _data set_ [Pulsar Star](https://archive.ics.uci.edu/ml/datasets/HTRU2), contendo 2 questões.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Setup_ geral

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sct
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

from IPython.core.pylabtools import figsize


figsize(12, 8)

sns.set()


# ## Parte 1

# ### _Setup_ da parte 1

# In[4]:


np.random.seed(42)
    
dataframe = pd.DataFrame({"normal": sct.norm.rvs(20, 4, size=10000),
                     "binomial": sct.binom.rvs(100, 0.2, size=10000)})


# ## Inicie sua análise a partir da parte 1 a partir daqui

# In[5]:


# Sua análise da parte 1 começa aqui.
dataframe.head()


# In[6]:


fig,(ax1,ax2)=plt.subplots(1,2)
sns.distplot(dataframe['normal'],ax=ax1)
sns.distplot(dataframe['binomial'],ax=ax2)
plt.show()


# In[7]:


dataframe.describe()


# In[8]:


dataframe['normal'].mean()


# In[9]:


dataframe['normal'].std()


# In[10]:


sct.norm.sf(20, loc=19.9914, scale=4.013)


# In[11]:


sct.norm.ppf(0.25, loc=19.9914, scale=4.013)


# In[12]:


sct.norm.ppf(0.5, loc=19.9914, scale=4.013)


# In[13]:


sct.norm.ppf(0.75, loc=19.9914, scale=4.013)


# In[14]:


sct.norm.ppf(.9973, loc=19.9914, scale=4.013)


# In[15]:


dataframe['binomial'].mean()


# In[16]:


dataframe['binomial'].std()


# In[17]:


q1=17.309638-17
q2=19.989620-20
q3=22.684324-23


# 68.27

# In[18]:


soma=sct.norm.cdf(19.991456+4.013850,loc=19.991456,scale=4.013850)


# In[19]:


sub=sct.norm.cdf(19.991456-4.013850,loc=19.991456,scale=4.013850)


# In[20]:


soma-sub


# In[21]:


dataframe['binomial'].var()-dataframe['normal'].var()


# In[22]:


dataframe['binomial'].mean()-dataframe['normal'].mean()


# In[23]:


round(0.2202361370433188,3)


# In[24]:


q1


# ## Questão 1
# 
# Qual a diferença entre os quartis (Q1, Q2 e Q3) das variáveis `normal` e `binomial` de `dataframe`? Responda como uma tupla de três elementos arredondados para três casas decimais.
# 
# Em outra palavras, sejam `q1_norm`, `q2_norm` e `q3_norm` os quantis da variável `normal` e `q1_binom`, `q2_binom` e `q3_binom` os quantis da variável `binom`, qual a diferença `(q1_norm - q1 binom, q2_norm - q2_binom, q3_norm - q3_binom)`?

# In[5]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return (q1,q2,q3)
    pass


# Para refletir:
# 
# * Você esperava valores dessa magnitude?
# 
# * Você é capaz de explicar como distribuições aparentemente tão diferentes (discreta e contínua, por exemplo) conseguem dar esses valores?

# ## Questão 2
# 
# Considere o intervalo $[\bar{x} - s, \bar{x} + s]$, onde $\bar{x}$ é a média amostral e $s$ é o desvio padrão. Qual a probabilidade nesse intervalo, calculada pela função de distribuição acumulada empírica (CDF empírica) da variável `normal`? Responda como uma único escalar arredondado para três casas decimais.

# In[6]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return 0.6826894921370857
    pass


# Para refletir:
# 
# * Esse valor se aproxima do esperado teórico?
# * Experimente também para os intervalos $[\bar{x} - 2s, \bar{x} + 2s]$ e $[\bar{x} - 3s, \bar{x} + 3s]$.

# ## Questão 3
# 
# Qual é a diferença entre as médias e as variâncias das variáveis `binomial` e `normal`? Responda como uma tupla de dois elementos arredondados para três casas decimais.
# 
# Em outras palavras, sejam `m_binom` e `v_binom` a média e a variância da variável `binomial`, e `m_norm` e `v_norm` a média e a variância da variável `normal`. Quais as diferenças `(m_binom - m_norm, v_binom - v_norm)`?

# In[7]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return (0.106,0.220)
    pass


# Para refletir:
# 
# * Você esperava valore dessa magnitude?
# * Qual o efeito de aumentar ou diminuir $n$ (atualmente 100) na distribuição da variável `binomial`?

# ## Parte 2

# ### _Setup_ da parte 2

# In[25]:


stars = pd.read_csv("pulsar_stars.csv")

stars.rename({old_name: new_name
              for (old_name, new_name)
              in zip(stars.columns,
                     ["mean_profile", "sd_profile", "kurt_profile", "skew_profile", "mean_curve", "sd_curve", "kurt_curve", "skew_curve", "target"])
             },
             axis=1, inplace=True)

stars.loc[:, "target"] = stars.target.astype(bool)


# ## Inicie sua análise da parte 2 a partir daqui

# In[26]:


# Sua análise da parte 2 começa aqui.
stars.head()


# ## Questão 4
# 
# Considerando a variável `mean_profile` de `stars`:
# 
# 1. Filtre apenas os valores de `mean_profile` onde `target == 0` (ou seja, onde a estrela não é um pulsar).
# 2. Padronize a variável `mean_profile` filtrada anteriormente para ter média 0 e variância 1.
# 
# Chamaremos a variável resultante de `false_pulsar_mean_profile_standardized`.
# 
# Encontre os quantis teóricos para uma distribuição normal de média 0 e variância 1 para 0.80, 0.90 e 0.95 através da função `norm.ppf()` disponível em `scipy.stats`.
# 
# Quais as probabilidade associadas a esses quantis utilizando a CDF empírica da variável `false_pulsar_mean_profile_standardized`? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[30]:


sns.distplot(stars['mean_profile'])


# In[31]:


stars0=stars[stars['target']==0]


# In[32]:


media=stars0['mean_profile'].mean()


# In[33]:


std=stars0['mean_profile'].std()


# In[34]:


stars0['false_pulsar_mean_profile_standardized']=stars0['mean_profile'].apply(lambda x: ((x-media)/std))


# In[35]:


stars0.head()


# In[36]:


stars0['false_pulsar_mean_profile_standardized'].mean()


# In[37]:


sns.distplot(stars0['false_pulsar_mean_profile_standardized'])


# In[38]:


stars0.describe()


# In[59]:


quant08 = sct.norm.ppf(0.8, loc = 0, scale=1)
quant09 = sct.norm.ppf(0.9, loc = 0, scale=1)
quant095 = sct.norm.ppf(0.95, loc = 0, scale=1)


# In[60]:


ecdf=ECDF(stars0['false_pulsar_mean_profile_standardized'])


# In[62]:


def q4():
    # Retorne aqui o resultado da questão 4.
    resultado = np.around((ecdf(quant08), ecdf(quant09), ecdf(quant095)),3)
    return tuple(resultado)
    pass


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?

# ## Questão 5
# 
# Qual a diferença entre os quantis Q1, Q2 e Q3 de `false_pulsar_mean_profile_standardized` e os mesmos quantis teóricos de uma distribuição normal de média 0 e variância 1? Responda como uma tupla de três elementos arredondados para três casas decimais.

# In[65]:


def q5():
    # Retorne aqui o resultado da questão 5.
    serie1 = stars0['false_pulsar_mean_profile_standardized'].quantile(.25)
    serie2 = stars0['false_pulsar_mean_profile_standardized'].quantile(.5)
    serie3 = stars0['false_pulsar_mean_profile_standardized'].quantile(.75)
    
    teorico1 = sct.norm.ppf(.25, loc=0, scale=1)
    teorico2 = sct.norm.ppf(.5, loc=0, scale=1)
    teorico3 = sct.norm.ppf(.75, loc=0, scale=1)
    
    resultado = np.around((serie1 - teorico1, serie2 - teorico2, serie3 - teorico3),3)
    return tuple(resultado)
    pass


# Para refletir:
# 
# * Os valores encontrados fazem sentido?
# * O que isso pode dizer sobre a distribuição da variável `false_pulsar_mean_profile_standardized`?
# * Curiosidade: alguns testes de hipóteses sobre normalidade dos dados utilizam essa mesma abordagem.
