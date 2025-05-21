#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd


# In[2]:

class LOFSPlugin:
 def input(self, inputfile):
  self.dfs = []
  tetrad_images_dir = os.path.join(inputfile)
  for d in glob.glob(tetrad_images_dir + os.sep + "*.txt"):
    print (d)
    df = pd.read_table(d, sep="\t")
    self.dfs.append(df)

 def run(self):
  pass

 def output(self, outputfile):
  # In[3]:


  from pycausal.pycausal import pycausal as pc
  pc = pc()
  pc.start_vm()


  # In[4]:


  from pycausal import search as s
  tetrad = s.tetradrunner()
  tetrad.listIndTests()


  # In[5]:


  tetrad.getAlgorithmParameters(algoId = 'imgs_cont', testId = 'fisher-z-test')


  # In[6]:


  tetrad.run(algoId = 'imgs_cont', dfs = self.dfs, testId = 'fisher-z-test', verbose = True)


  # In[7]:


  tetrad.getNodes()


  # In[8]:


  tetrad.getEdges()


  # In[9]:


  import pydot
  #from IPython.display import SVG
  dot_str = pc.tetradGraphToDot(tetrad.getTetradGraph())
  graphs = pydot.graph_from_dot_data(dot_str)
  graphs[0].write_png(outputfile+".1.png")
  #svg_str = graphs[0].create_svg()
  #SVG(svg_str)


  # In[10]:


  tetradGraph = tetrad.getTetradGraph()
  lofs = s.lofs(tetradGraph, self.dfs, dataType = 0, rule = 'RSkewE', score = 'entropy')


  # In[11]:


  lofs.getEdges()


  # In[12]:


  dot_str = pc.tetradGraphToDot(tetrad.getTetradGraph())
  outf = open(outputfile+".txt", 'w')
  outf.write(dot_str)
  graphs = pydot.graph_from_dot_data(dot_str)
  graphs[0].write_png(outputfile+".2.png")

  #svg_str = graphs[0].create_svg()
  #SVG(svg_str)


  # In[13]:
  

  pc.stop_vm()


  # In[ ]:




