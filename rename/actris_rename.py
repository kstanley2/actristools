#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 15:41:24 2021

@author: kieran

Code created to rename columns in pandas dataframes to names for ACTRIS

Functions include:
    columns_rename
        - function to rename column headers in pandas dataframe.
        - Function requires:
            - a pandas dataframe with the first column as a date_time.
"""

###############################################################################
##### create function to rename column headers to ACTRIS convention         ###
###############################################################################

def columns_rename(df):

    ### import modules
    import pandas as pd
    
    ### create dictionary for names:
    species = {
            'ethan':'ethane',
            'ethen':'ethene',	
            'ethin': 'ethyne',
            'propan':'propane',
            'propen':'propene',
            'i-butan':'2-methylpropane',	
            'i-butane':'2-methylpropane',	
            'n- butan': 'butane',		
            'n-butan': 'butane',	  
            'trans-2-buten': 'trans-2-butene',	 
            '1-buten': '1-butene',  
            'i-buten': '2-methylpropene',
            'i-butene': '2-methylpropene',	
            'cis-2-buten': 'cis-2-butene',	
            'i-pentan': '2-methylbutane',	
            'i-pentane': '2-methylbutane',	
            'n-pentan': 'pentane',	 
            'n-pentane': 'pentane',
            'butadien1,3': '1,3-butadiene',	 
            'isopren': '2-methyl-1,3-butadiene',		
            'isoprene': '2-methyl-1,3-butadiene',		 
            '2-methylpentan': '2-methylpentane',		 
            '2-methylpentane': '2-methylpentane',		 
            'i-hexane': '2-methylpentane',
            'n-hexan': 'hexane',	 
            'i-octane': '2,2,4-trimethylpentane',
            'benzol': 'benzene',	 
            'n-heptan': 'heptane',
            'toluol': 'toluene',	 
            'ethylbenzol': 'ethylbenzene',	 
            'm/p-xylol': 'm+p-xylene',	  
            'o-xylol': 'o-xylene', 
            'pentene': '1-pentene',		
            'gesamt-voc': 'total_voc'}
    
    ### rename dataframe columns to match ACTRIS nomenclature
    print('\nRenaming column headers...')
    df_header_ls = [df.columns[0]]
    for i in range(1,len(df.columns)):
        gas = df.columns[i].replace(' ','').lower()
        #print(gas)
        df_header_ls.append(species[gas])
        
    df.columns = df_header_ls
    
    return df