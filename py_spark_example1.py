#!/usr/bin/python

from pyspark  import  SparkContext

words = []
with open('install.txt','r') as f:
    for line in f:
        for word in line.split():

             words.append(word)


sc=SparkContext("local","App_first")


trans1=sc.parallelize(words)

action1=trans1.count()

print  "number of Elements in RDD -> %i" %(action1)
