import pandas as pd
import numpy as np
from random import shuffle

class DOPS:
    def __init__(self, df):
        print('Initializing DOPS')
        self.df = df

    def obfuscate(self, num_partitions, axis):
        self.num_partitions = num_partitions
    
        if axis == "X":
            self.farthestX = np.amax(self.df.values.tolist(), axis=0)[0]  
            self.Xpartitions = self.partitionX_dataset()
            self.df = self.shuffle(self.Xpartitions)

        elif axis == "Y":   
            self.farthestY = np.amax(self.df.values.tolist(), axis=0)[1]
            self.Ypartitions = self.partitionY_dataset()
            self.df = self.shuffle(self.Ypartitions)

    def partitionX_dataset(self):
        """   
        Return a list of X partitions
        """
        size = 0 
        partition_size = self.farthestX/self.num_partitions
        partitions = []
        while not(size == self.farthestX):
            partition = []
            for instance in self.df.values.tolist():
                if (instance[0] > size) and (instance[0] <= size + partition_size) :
                    partition.append(instance)
            partitions.append(partition)
            size += partition_size
        return partitions

    def partitionY_dataset(self):
        """   
        Return a list of Y partitions 
        """
        size = 0 
        partition_size = self.farthestY/self.num_partitions
        partitions = []
        while not(size == self.farthestY):
            partition = []
            for instance in self.df.values.tolist():
                if (instance[1] > size) and (instance[1] <= size + partition_size) :
                    partition.append(instance)
            partitions.append(partition)
            size += partition_size
        return partitions
        
    def shuffle(self, partitions):
        """
        Return an obfuscated dataset after shuffling elements in a partition
        """
        obf_dataset = np.array([[0,0]])
        for partition in partitions:
            listX = []
            listY = []
            obf_partition = []
            for instance in partition:
                listX.append(instance[0])
                listY.append(instance[1])
            shuffle(listX)
            shuffle(listY)
            np.array(listX)
            np.array(listY)
            obf_partition = np.column_stack((listX,listY))
            obf_dataset = np.concatenate((obf_dataset, obf_partition))
        obf_dataset = np.delete(obf_dataset, 0, 0)
        obf_df = pd.DataFrame({self.df.columns[0]:obf_dataset[:,0],self.df.columns[1]:obf_dataset[:,1]})
        return obf_df

    def get_obf_df(self):
        print(self.df)
    
