#!/usr/bin/env python
# coding: utf-8

# # OpenCVを使って画像を読込、表示、保存する

# In[9]:


import cv2
from matplotlib import pyplot as plt


# In[11]:


image = cv2.imread("test.jpg")
print(type(image))


# In[12]:


# 画像の次元数
print("(h, w, c)=", image.shape)


# In[6]:


# OpenCVのカラーの並びはBGRなので、matplotlibで表示しようとするとうまくいかない
plt.imshow(image)
plt.show()


# ### 【課題】元の色のままで表示するプログラムを作成してください

# In[5]:


# ここにコードを書いてください．


# ### 【課題】色反転させて、画像を表示させるプログラムを書いてください。

# In[6]:


# ここにコードを書いてください．


# ### 【課題】上記で色反転させた画像を保存するプログラムを書いてください

# In[7]:


# ここにコードを書いてください．


# ### 【課題】*.pyでファイルをダウンロードして、cv2.imshow()関数を使って画像を表示させるプログラムを書いてください。

# In[ ]:


# 注意！cv2.imshow()関数はjupyterでは使うことができません。
# メニューの[File]-[Download as]からPython(*.py)形式でダウンロードして、コマンドを使って実行する必要があります。

# ここにコードを書いてください．

