#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### it's all yours from here forward!
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=.3, random_state=42)
clf = DecisionTreeClassifier().fit(X_train, y_train)
print([1 for (x, y) in zip(y_test, clf.predict(X_test)) if (x==y) and (x==1)])
print(clf.score(X_test, y_test))
print(sum(y_test), len(y_test))
print(metrics.precision_score(clf.predict(X_test), y_test), metrics.recall_score(clf.predict(X_test), y_test))

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
print(metrics.precision_score(true_labels, predictions), metrics.recall_score( true_labels, predictions))
