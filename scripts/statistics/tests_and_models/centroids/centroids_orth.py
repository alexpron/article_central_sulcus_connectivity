import os
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import levene, shapiro, ttest_rel, ttest_ind, ttest_1samp
from statsmodels.stats.anova import anova_lm
from variables import DIR_OUT

if __name__ == "__main__":
    path_df1 = os.path.join(DIR_OUT, "derived_tables", "centroids_iso.csv")
    df1 = pd.read_csv(path_df1)
    path_df2 = os.path.join(DIR_OUT, "inter_tables", "hemispheres_level.csv")
    df2 = pd.read_csv(path_df2)

    df = pd.merge(df1, df2, on=["Subject", "Hemisphere"])
    print
    df.columns

    model = smf.ols("Centroid_Orth_Coord_Iso ~ C(Hemisphere)", data=df).fit()
    summary = model.summary()
    anova = anova_lm(model)

    print
    summary
    print
    anova
    #
    # labels = np.unique(df['Label'].values)
    #
    # print df.columns
    #
    # # sns.catplot(x='Hemisphere',y='Centroid_Diag_Coord',data=df, kind='box')
    # # plt.show()
    # for l in labels:
    #     lab_df = df.loc[df['Label']==l]
    #     L = lab_df.loc[lab_df['Hemisphere']=='L','Centroid_Diag_Coord_Iso'].values
    #     R = lab_df.loc[lab_df['Hemisphere'] == 'R', 'Centroid_Diag_Coord_Iso'].values
    #
    #     L_Low = lab_df.loc[(lab_df['Hemisphere']=='L') & (lab_df['HandednessQ']=='Low') ,'Centroid_Diag_Coord_Iso'].values
    #     R_Low = lab_df.loc[(lab_df['Hemisphere']=='R') & (lab_df['HandednessQ']=='Low') ,'Centroid_Diag_Coord_Iso'].values
    #     L_High = lab_df.loc[(lab_df['Hemisphere']=='L') & (lab_df['HandednessQ']=='High') ,'Centroid_Diag_Coord_Iso'].values
    #     R_High = lab_df.loc[(lab_df['Hemisphere']=='R') & (lab_df['HandednessQ']=='High') ,'Centroid_Diag_Coord_Iso'].values
    #
    #     #W, p = levene(R, L) #All centroids except dorsal one have equal variances
    #     W, p = levene(L_Low, R_Low,L_High, R_High)
    #     #print W, p
    #
    #     L_Low_M = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'L') & (lab_df['HandednessQ'] == 'Low') & (lab_df['Gender'] == 'M') , 'Centroid_Diag_Coord_Iso'].values
    #     L_Low_F = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'L') & (lab_df['HandednessQ'] == 'Low') & (lab_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
    #     R_Low_M = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'R') & (lab_df['HandednessQ'] == 'Low') & (lab_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
    #     R_Low_F = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'R') & (lab_df['HandednessQ'] == 'Low') & (lab_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
    #     L_High_M = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'L') & (lab_df['HandednessQ'] == 'High') & (lab_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
    #     L_High_F = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'L') & (lab_df['HandednessQ'] == 'High') & (lab_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
    #     R_High_M = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'R') & (lab_df['HandednessQ'] == 'High') & (lab_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
    #     R_High_F = lab_df.loc[
    #         (lab_df['Hemisphere'] == 'R') & (lab_df['HandednessQ'] == 'High') & (lab_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
    #     W, p = levene(L_Low_M,L_Low_F,R_Low_M, R_Low_F,L_High_M, L_High_F,R_High_M, R_High_F  )
    #     #print "Levene test label",l, ":", W, p
    #     subgroups = [L_Low_M,L_Low_F,R_Low_M, R_Low_F,L_High_M, L_High_F,R_High_M, R_High_F]
    #     for j, g in enumerate(subgroups):
    #         W, p =  shapiro(g)
    #         if p<=0.05:
    #             print "Label",l, "Subgroup", j, "nb_ind",len(g), "Gaussian assumption rejected"
    #     # D = R - L
    # A = 2*D/(R+L)
    # #W,  p = shapiro(D)
    # W, p = shapiro(A)
    # t, p_t = ttest_rel(L,R)
    # # print "Label", l
    # # print "Shapiro test", W, p
    # # print "Student paired t test", t, p_t
    # sub_df = lab_df.drop_duplicates(['Subject','Label'])
    # #print sub_df
    # sub_df['Assymetry'] = A
    # low = sub_df.loc[sub_df['HandednessQ']=='Low','Assymetry']
    # high = sub_df.loc[sub_df['HandednessQ']=='High','Assymetry']
    # W_l, p_l = shapiro(low)
    # W_h, p_h = shapiro(high)
    # print "Low Hand Shapiro", W_l, p_l
    # print "High Hand Shapiro",  W_h, p_h
    # W, p = levene(low,high)
    # print "Levene Low/High Hand"
    # print W, p
