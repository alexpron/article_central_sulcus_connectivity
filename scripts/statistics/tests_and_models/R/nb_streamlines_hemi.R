# Title     : TODO
# Objective : TODO
# Created by: alex
# Created on: 28/01/19

library(ez)

#my first dataset
datf = read.csv('/home/alex/PycharmProjects/HCP/statistics/data/output/derived_tables/nb_streamlines_hemi_level_norm.csv')
#print(datf)
#print datf.
datf <- na.omit(datf)
#print(datf2)
rt_anova  <- ezANOVA(data=datf,dv=.(Nb_Streamlines_Hemi), wid=.(Subject), within=.(Hemisphere), within_covariates=.(Roi_Area), type=3, detailed=TRUE, return_aov=TRUE)
print(rt_anova)