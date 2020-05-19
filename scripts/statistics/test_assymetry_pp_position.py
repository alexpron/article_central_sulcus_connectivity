import pandas as pd
from scipy.stats import shapiro, mannwhitneyu, levene, ttest_1samp,ttest_ind, ttest_rel
from matplotlib import pyplot as plt
import seaborn as sns

if __name__ == '__main__':

    df = pd.read_csv(os.path.join(DIR_OUT,'pli_passage','tables','pp_manual_drawing_coord_sulcus.csv'))
    df = df[['Subject','Hemisphere','PP_CS_Coord_Iso','Drawer']]
    df = df.dropna()
    #Test normality of the different distributions
    #Whole distribution
    W, p = shapiro(df['PP_CS_Coord_Iso'].values)
    #Left Distribution
    L = df.loc[df['Hemisphere']=='L','PP_CS_Coord_Iso'].values
    W_l , p_l = shapiro(L)
    R = df.loc[df['Hemisphere'] == 'R', 'PP_CS_Coord_Iso'].values
    W_r, p_r = shapiro(R)
    #Difference
    D = R - L
    W_d, p_d = shapiro(D)
    A = 2*(R - L)/(R + L)
    W_a, p_a = shapiro(A)

    print W, p
    print W_l, p_l
    print W_r, p_r
    print W_d,p_d
    print W_a, p_a
    #
    # sns.distplot(L,label='Left')
    # sns.distplot(R,label='Right')
    # plt.legend()
    # plt.title('Distribution of Pli de Passage locations \n along the central sulcus fundus (ventral to dorsal)')
    # plt.show()
    t_d , p_td = ttest_rel(R, L)

    t_a, p_ta = ttest_1samp(A,0)
    print t_d, p_td
    print t_a, p_ta



