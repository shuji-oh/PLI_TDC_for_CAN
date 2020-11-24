from sklearn.ensemble import RandomForestClassifier
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.model_selection import StratifiedKFold

def main():
    df = pd.read_csv("delay_time.csv")
    X = df[['mean','stdev','skew','kurtosis','max','min','rms','fine_stdev']]
    Y = df['label'].map({'ECU0': 0, 'ECU1': 1, 'ECU2': 2, 'ECU3': 3, 'ECU4': 4, 'ECU5': 5, 'ECU6': 6})
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0) # dividing the data to 80% as training data, 20% as testing data
    
    # rf
    rf = RandomForestClassifier(n_estimators=50)

    # K-fold cross validation
    #print(np.mean(cross_val_score(rf, X, Y, cv=5)))
    kfold = StratifiedKFold(n_splits=5, shuffle=True)
    cvscores = []
    X = X.values
    Y = Y.values
    for train, test in kfold.split(X, Y):
        rf.fit(X[train], Y[train])
        Y_pred = rf.predict(X[test])
        scores = accuracy_score(Y[test], Y_pred)
        cvscores.append(scores*100)
        print('Test accuracy:', scores)

    # K-fold result
    print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))

    rf.fit(X_train, Y_train)
    Y_pred = rf.predict(X_test)
    C = confusion_matrix(Y_test, Y_pred)
    # Normalization
    C_sum= C.astype(np.float).sum(axis=1)
    NC = [C[0]/C_sum[0], C[1]/C_sum[1], C[2]/C_sum[2], C[3]/C_sum[3], C[4]/C_sum[4], C[5]/C_sum[5], C[6]/C_sum[6]]
    print(NC)

    # plot
    X_combined = np.vstack((X_train, X_test))
    y_combined = np.hstack((Y_train, Y_test))
    
    df = pd.DataFrame(NC, index=['ECU0', 'ECU1', 'ECU2', 'ECU3', 'ECU4', 'ECU5', 'ECU6'], columns=['ECU0', 'ECU1', 'ECU2', 'ECU3', 'ECU4', 'ECU5', 'ECU6'])
    fig = plt.figure()
    sns.heatmap(df, cmap="Greens", annot=True, fmt=".4f")
    plt.yticks(rotation=0)
    
    plt.xlabel('Predicted label')
    plt.ylabel('Actual label')

    pp = PdfPages('rf_confusion.pdf')
    pp.savefig(fig)

    pp.close()
    plt.close('all')

if __name__ == '__main__':
    main()
