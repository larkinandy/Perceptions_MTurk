# linear regression models for R21

setwd('#insert working directory here')

allMeta <- read.csv("AllFinal.csv")
relStats <- read.csv("mturkGIS2.csv")

allStats <- merge(x =relStats, y=allMeta,by.x=c("image_id"),by.y=c("panid"))

############ greenspace ###########
greenAbsCity <-  lm(avg_mu_greenspace ~ accessibility_z + grass_z*as.factor(sampleCat) + sidewalk +  grass_z*as.factor(sampleCat) + 
                      grass_z + tree_z*as.factor(sampleCat) + tree_z + other_nature + flower*as.factor(sampleCat) + 
                      flower + accessibility_z*as.factor(angle) + tree_z*as.factor(angle)
                    + building + build2_z  + animate_z + plant + earth + sky + as.factor(sampleCat) + as.factor(angle), data =allStats)
summary(greenAbsCity)

############ safety ##########
safeRel  <- lm(avg_mu_safe ~ accessibility_z  + road +  grass_z + tree_z + other_nature + house +
                 accessibility_z*as.factor(angle) + car*as.factor(angle) + plant + car + as.factor(sampleCat) + as.factor(angle), data =allStats)
summary(safeRel)

############ relax ##########
relaxRel  <- lm(avg_mu_relax ~ accessibility_z + accessibility_z*as.factor(angle) + other_nature*as.factor(sampleCat) + 
                  tree_z*as.factor(angle) +  grass_z + tree_z + 
                  other_nature + earth*as.factor(sampleCat) + building  + animate_z +
                  plant + car + person + earth + sky  + as.factor(sampleCat) + as.factor(angle), data =allStats)

summary(relaxRel)

############ relax ##########
beautyRel  <- lm(avg_mu_beauty ~  accessibility_z + tree_z*as.factor(angle) + house*as.factor(sampleCat) + road + grass + tree_z + built_env_z + house + animate_z + plant + car + as.factor(sampleCat) + as.factor(angle), data =allStats)

summary(beautyRel)
