#!/usr/bin/python

from pyspark  import  SparkContext

words = []
with open('install.txt','r') as f:
    for line in f:
        for word in line.split():

             words.append(word)









sc=SparkContext("local","App_filter")

trans1=sc.parallelize(words)

words_map=trans1.map(lambda x:(x,1))
mapping=words_map.collect()

print "Mapped  RDD -> %s " % (mapping)



