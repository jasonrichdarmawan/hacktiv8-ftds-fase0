# Supervised Learning

`sklearn.tree.DecisionTreeClassifier`, `sklearn.ensemble.RandomForestClassifier`
1. Do not do feature selection based on multicollinearity. It will only reduce the metrics.

2. Do not use OneHotEncoder for ordinal data. It will only reduce the metrics and increase the computational cost. 

   If there is 1 value that can't be ordered ie 'Unknown', it is still an ordinal data.
   
   Just put the 'Unknown' value as index 0 or -1. This is because of how the internal nodes are splitted:
   1. Try 'Education_Level' < 2
   2. Check the gini impurity
   3. If it is not pure, split the internal node
   4. 'Education_level' < 1, and so on, until the gini impurity is 0.

3. Log Transform and Square Root Transform to transform skewed data to more like normally distributed data does increase the metrics.
4. Do not use OneHotEncoder even for nominal data. It will only reduce metrics because of how each tree select features.

   1. Decision Tree select feature for the root node, and internal node by comparing the gini impurity of each feature.
   2. Random Forest randomly assign feature for each decision tree to work on. Now imagine that Random Forest assign 'Education_Level_Unknown' (instead of the entire 'Education_Level_Uneducated', 'Education_Level_High School' and so on) to a specific tree. That tree lost so much information about 'Education_Level', making that 'Education_Level_Unknown' worthless.

`sklearn.linear_model.LogisticRegression`, `sklearn.svm.SVC`
1. Do not do feature selection based on multicollinearity. It will only reduce the metrics.
2. Use OneHotEncoder for nominal data.