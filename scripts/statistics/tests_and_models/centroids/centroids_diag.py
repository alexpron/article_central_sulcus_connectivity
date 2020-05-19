import os
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import levene, shapiro, ttest_rel, ttest_ind, ttest_1samp, mannwhitneyu
from statsmodels.stats.anova import anova_lm
from variables import DIR_OUT

if __name__ == '__main__':

    path_df1 = os.path.join(DIR_OUT, 'derived_tables', 'centroids_iso.csv')
    df1 = pd.read_csv(path_df1)
    path_df2 = os.path.join(DIR_OUT, 'inter_tables', 'hemispheres_level.csv')
    df2 = pd.read_csv(path_df2)

    df = pd.merge(df1, df2, on=['Subject', 'Hemisphere'])

    labels = np.unique(df['Label'].values)

    for l in labels:
        new_df = df.loc[df['Label'] == l]
        # Test Hemisphere influence
        L = new_df.loc[new_df['Hemisphere'] == 'L', 'Centroid_Diag_Coord_Iso'].values
        R = new_df.loc[new_df['Hemisphere'] == 'R', 'Centroid_Diag_Coord_Iso'].values

        L_L = new_df.loc[
            (new_df['Hemisphere'] == 'L') & (new_df['HandednessQ'] == 'Low'), 'Centroid_Diag_Coord_Iso'].values
        L_H = new_df.loc[
            (new_df['Hemisphere'] == 'L') & (new_df['HandednessQ'] == 'High'), 'Centroid_Diag_Coord_Iso'].values
        R_L = new_df.loc[
            (new_df['Hemisphere'] == 'R') & (new_df['HandednessQ'] == 'Low'), 'Centroid_Diag_Coord_Iso'].values
        R_H = new_df.loc[
            (new_df['Hemisphere'] == 'R') & (new_df['HandednessQ'] == 'High'), 'Centroid_Diag_Coord_Iso'].values

        L_L_M = new_df.loc[
            (new_df['Hemisphere'] == 'L') & (new_df['HandednessQ'] == 'Low') & (
                        new_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
        L_L_F = new_df.loc[
            (new_df['Hemisphere'] == 'L') & (new_df['HandednessQ'] == 'Low') & (
                        new_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
        L_H_M = new_df.loc[
            (new_df['Hemisphere'] == 'L') & (new_df['HandednessQ'] == 'High') & (
                        new_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
        L_H_F = new_df.loc[
            (new_df['Hemisphere'] == 'L') & (new_df['HandednessQ'] == 'High') & (
                        new_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
        R_L_M = new_df.loc[
            (new_df['Hemisphere'] == 'R') & (new_df['HandednessQ'] == 'Low') & (
                        new_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
        R_L_F = new_df.loc[
            (new_df['Hemisphere'] == 'R') & (new_df['HandednessQ'] == 'Low') & (
                        new_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values
        R_H_M = new_df.loc[
            (new_df['Hemisphere'] == 'R') & (new_df['HandednessQ'] == 'High') & (
                        new_df['Gender'] == 'M'), 'Centroid_Diag_Coord_Iso'].values
        R_H_F = new_df.loc[
            (new_df['Hemisphere'] == 'R') & (new_df['HandednessQ'] == 'High') & (
                        new_df['Gender'] == 'F'), 'Centroid_Diag_Coord_Iso'].values

        # W_var , p_var = levene(L_L, L_H, R_L, R_H)
        # print W_var, p_var
        W_var_t, p_var_t = levene(L_L_M, L_L_F, L_H_M, L_H_F, R_L_M, R_L_F, R_H_M, R_H_F)
        print
        "Levene test, Label:", l, W_var_t, p_var_t
        model = smf.ols('Centroid_Diag_Coord_Iso ~ C(Hemisphere)*C(HandednessQ)*C(Gender)', data=new_df).fit()
        resid = model.resid
        W_r, p_r = shapiro(resid)
        print
        "Shapiro Residuals test, Label:", l, W_r, p_r
        anova = anova_lm(model)
        # summary = model.summary()

        # print "Label: ", l, summary.tables[]
        # print summary
        #
        # print "Label",l,  anova
        # # print "LABEL", l, summary
        # #

        # model = smf.ols('Centroid_Diag_Coord_Iso ~ C(Hemisphere)',data=new_df).fit()
        #
        # print model.summary()
        # #anova = anova_lm(model)
        # #print anova

    # for l in labels:
    #     L = df.loc[(df['Hemisphere']=='L') & (df['Label']==l),'Centroid_Orth_Coord_Iso'].values
    #     R = df.loc[(df['Hemisphere']=='R') & (df['Label']==l),'Centroid_Orth_Coord_Iso'].values
    #     W_l, p_l = shapiro(L)
    #     # print "L Label", l, W_l, p_l
    #     # W_r, p_r = shapiro(R)
    #     # print "R Label", l, W_r, p_r
    #     # D = R - L #Difference is non gaussian
    #     # W, p = shapiro(D)
    #     # print "Diff Label", l, W, p
    #
    #     # W_v, p_v = levene(L,R)
    #     # print "Var Label", W_v, p_v
    #     #
    #     #Data are not gaussian
    #     W, p = mannwhitneyu(L, R)
    #     print "Mann Wit, Label", l, W, p
