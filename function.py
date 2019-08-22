import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns;


class correlation_matrix_by_frequency():

    def __init__(self, dataframe, return_correlation_df=True):
        self.df = dataframe
        self.return_corr = return_correlation_df

    def calculate_correlation(self):
        '''This class contains objects to handle two coloumn data frame
        The endpoint returns correlation of intents with entities (first col and last col not the other way around)'''

        cols = list(self.df.columns)
        unique_intents = self.df[cols[0]].unique()

        all_entities = []
        for i in self.df[cols[1]]:
            for j in i:
                all_entities.append(j)
        unique_entities = np.unique(all_entities)

        dict_entities = {}
        for i in self.df.entities:
            for j in i:
                self.update_count(dict=dict_entities, key=j)

        ''' Creating nested dicts of the following structure -> 
            {
             intent1 :{dict of entities}, 
             intent2: {dict of entities} 
             }
        '''
        nested_dict = {}
        for i in unique_intents:
            nested_dict[i] = {}
        ''' dict of  entities'''
        entity_dict = {}
        for i in unique_entities:
            entity_dict[i] = 0
        for i in unique_intents:
            nested_dict[i] = entity_dict.copy()
        '''now we will recursively update the dict of entities withing each dict of intent'''
        for i in range(len(self.df)):
            for j in self.df.iloc[i][1]:
                nested_dict[self.df.intents[i]][j] += 1
        df_final = pd.DataFrame.from_dict(nested_dict, orient='index')

        for i in unique_entities:
            self.normalize_entities(i, df_final, dict_entities)


        return df_final

    def plot_heatmap(self,df_):
        ax = sns.heatmap(df_)
        plt.show()


    def normalize_entities(self, entity, df_final, dict_entities):
        normalized = []
        for i in range(len(df_final)):
            normalized.append(df_final[entity][i] / dict_entities[entity])
        df_final[entity] = normalized

    def update_count(self, dict, key):
        '''Static function- if ran once cannot be traced or undone, carefull use '''
        try:
            dict[key] += 1
        except KeyError:
            dict[key] = 1




