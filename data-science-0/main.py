#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[120]:


import pandas as pd
import numpy as np


# In[121]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[122]:


black_friday.head()


# In[123]:


black_friday.shape


# In[124]:


black_friday['Age'].value_counts()


# In[125]:


black_friday['User_ID'].nunique()


# In[126]:


black_friday.dtypes


# In[127]:


black_friday.isnull().sum().sum()/black_friday.size


# In[128]:


black_friday.isnull().sum()


# In[129]:


2/12


# In[130]:


black_friday['Product_Category_3'].value_counts()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[13]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return (537577, 12)
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[14]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return 49348
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[15]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return 5891
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[16]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return 3
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[17]:


def q5():
    # Retorne aqui o resultado da questão 5.
    return 0.694
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[18]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return 373299
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[19]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return 16
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    return 0.385
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    return 348631
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.
    return True
    pass

