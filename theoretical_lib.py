# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:40:30 2019

@author: marco
"""
import pandas as pd
import csv
import numpy as np
from numpy import linalg 
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from collections import defaultdict
from sklearn.preprocessing import StandardScaler

#Function performing the K_means analysis with all the centroids equal to each other
def K_Means_centr(K, data):
    array = np.array(data).reshape(data.shape[0], data.shape[1])
    n = array.shape[0]
    m = array.shape[1]
    #picking randomly the first centroids
    centroids = np.array([[0.1562837820, 0.37810392], [0.1562837820, 0.37810392], [0.1562837820, 0.37810392]])
    prev_centroids = np.zeros((n,K)) 
    #200 iterations
    for x in range(200):
        prev_centroids = centroids
        euc_dis = np.zeros((n,K))
        clus = defaultdict(list)
        clusters = []
        for i in range(n):
            for j in range(K):
            #computing the euclidean distance from the various points to the centroids
                euc_dis[i][j] += linalg.norm(array[i]-centroids[j])
            #list containing the cluster to which each wine belongs to
            clusters.append(np.where(euc_dis[i] == min(euc_dis[i]))[0][0]+1)
            #dictionary that maps each cluster to the wines that belong to it
            #e.g. {cluster1: [wine1, wine5, wine6, ...]}
            clus[clusters[i]].append(i)
        #computing the centroids by taking the mean
        #of the elements of the cluster
        for k in range(K):
            for j in range(m):
                values = []
                for i in clus[k+1]:
                    values.append(array[i][j])
                centroids[k][j] = np.mean(values)
    return clusters, centroids, clus

#Function performing the K_means analysis with one centroid far from the data
def K_Means_far(K, data):
    array = np.array(data).reshape(data.shape[0], data.shape[1])
    n = array.shape[0]
    m = array.shape[1]
    #picking randomly the first centroids
    centroids = np.array([[0.14572837820, 0.378148930392], [0.1562837820, 0.27710392], [10.1562837820, 11.37810392]])
    prev_centroids = np.zeros((n,K)) 
    #200 iterations
    for x in range(200):
        prev_centroids = centroids
        euc_dis = np.zeros((n,K))
        clus = defaultdict(list)
        clusters = []
        for i in range(n):
            for j in range(K):
            #computing the euclidean distance from the various points to the centroids
                euc_dis[i][j] += linalg.norm(array[i]-centroids[j])
            #list containing the cluster to which each wine belongs to
            clusters.append(np.where(euc_dis[i] == min(euc_dis[i]))[0][0]+1)
            #dictionary that maps each cluster to the wines that belong to it
            #e.g. {cluster1: [wine1, wine5, wine6, ...]}
            clus[clusters[i]].append(i)
        #computing the centroids by taking the mean
        #of the elements of the cluster
        for k in range(K):
            for j in range(m):
                values = []
                for i in clus[k+1]:
                    values.append(array[i][j])
                centroids[k][j] = np.mean(values)
    return clusters, centroids, clus