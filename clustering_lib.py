# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:01:45 2019

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

#Function performing the K_means analysis
def K_Means(K, data):
    #creating an array with the values of the dataframe
    array = np.array(data).reshape(data.shape[0], data.shape[1]) 
    n = array.shape[0]
    m = array.shape[1]
    #picking randomly the first centroids
    centroids = array[np.random.choice(n, size = K, replace = False)]
    prev_centroids = np.zeros((n,K)) 
    iterations = 0
    #until the centroids don't change or the iterations are maximum 200
    while iterations != 200 or np.array_equal(centroids, prev_centroids) == False:
        #saving the previous values of the cluster for the next while loop
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
        for k in range(K):
            for j in range(m):
                values = []
                for i in clus[k+1]:
                    #taking the values of the wines belonging to the i-th cluster
                    values.append(array[i][j])
    #computing the mean for each cluster and taking it as new centroid
                centroids[k][j] = np.mean(values)
        iterations += 1
    return clusters, centroids, clus

#Function performing the elbow_method
def elbow_method(K_values, data):
    #creating an array with the values of the dataframe
    array = np.array(data).reshape(data.shape[0], data.shape[1])
    WCSS = {}
    for K in K_values:
        #performing the k-means analysis for the K number of clusters
        clust, centr, clus = K_Means(K, data)
        WCSS_total = 0
        for k in range(1, K+1):
            WCSS_k = 0
            for i in clus[k]:
                #computing the WCSS for the k-th cluster of the K's clusters
                WCSS_k += np.sum((array[i] - centr[k-1])**2)
            #computing the overall WCSS with K number of clusters 
            WCSS_total += WCSS_k
        #dictionary mapping for each number of clusters the overall WCSS
        #e.g. {1 cluster: 22479.80, 2 cluster: 1890.67, 3 cluster: 2780.89, ... }
        WCSS[K] = WCSS_total
    #creating a dataframe having two columns: the first one the number of clusters the second one the corresponding
    #WCSS value
    elbow = pd.DataFrame({"Number of Clusters K": list(WCSS.keys()), "WCSS": list(WCSS.values())})
    #Plotting the curve of the Elbow Method
    plt.figure(figsize = (16,5))
    plt.title("Elbow Method")
    sns.lineplot(x = "Number of Clusters K", y = "WCSS", data = elbow)
    plt.xticks(elbow["Number of Clusters K"])
    plt.axvline(3, color = "r")
    plt.show()