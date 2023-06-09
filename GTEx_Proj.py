import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

gene_expr = pd.read_csv('https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.gct.gz', compression='gzip', sep='\t', skiprows=2, header=0, index_col=0)
gene_expr = gene_expr.drop(['Description'], axis=1)
heart_expr = gene_expr[['Heart - Atrial Appendage', 'Heart - Left Ventricle']].mean(axis=1)
heart_expr.name = 'Heart'

metadata = pd.read_csv('https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt.gz', compression='gzip', sep='\t', header=0, index_col=0)
data = pd.concat([heart_expr, metadata[['sex']]], axis=1)

data['sex'] = np.where(data['sex'] == 'Male', 0, 1)
