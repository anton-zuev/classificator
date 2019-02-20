import itertools

import matplotlib
from sklearn.datasets import make_blobs

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer

from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix
from pandas import DataFrame


def NaiveBayes(dataset, show=False):
    gnb = GaussianNB()
    X, labels = dataset
    new_labels = gnb.fit(X, labels).predict(X)

    conf = confusion_matrix(labels, new_labels)
    conf = conf / np.linalg.norm(conf)
    plt.matshow(conf)
    plt.show()
    if show:
        for i in range(len(X[0])):
            if i >= 3:
                break
            for j in range(i):
                x = list(x[i] for x in X)
                y = list(x[j] for x in X)

                paint(x, y, labels)
                paint(x, y, new_labels)

        plt.show()


def GaussianClassifier(dataset, show=False):
    X, labels = dataset
    kernel = 1.0 * RBF(1.0)
    classifier = GaussianProcessClassifier(kernel=kernel, random_state=0).fit(X, labels)
    classifier.score(X, labels)
    new_labels = classifier.predict(X)

    conf = confusion_matrix(labels, new_labels)
    conf = conf / np.linalg.norm(conf)

    plt.matshow(conf)
    plt.show()

    if show:
        for i in range(len(X[0])):
            if i >= 3:
                break
            for j in range(i):
                x = list(x[i] for x in X)
                y = list(x[j] for x in X)

                paint(x, y, labels)
                paint(x, y, new_labels)

        plt.show()


def pca():
    X, labels = load_iris(return_X_y=True)
    pca = PCA(n_components=4)
    pca.fit(X, labels)
    print(pca.score(X, labels))
    df1 = DataFrame(data=X)
    plt.matshow(df1.corr())
    df2 = DataFrame(data=pca.transform(X))
    plt.matshow(df2.corr())
    plt.show()


def paint(x, y, label):
    N = max(label) + 1

    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    cmap = plt.cm.jet
    cmaplist = [cmap(i) for i in range(cmap.N)]
    cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)
    bounds = np.linspace(0, N, N + 1)
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)

    scat = ax.scatter(x, y, c=label, s=10, cmap=cmap, norm=norm)
    cb = plt.colorbar(scat, spacing='proportional', ticks=bounds)


if __name__ == "__main__":
    pca()
    func = [
        NaiveBayes,
        GaussianClassifier,

    ]
    for x in func:
        print(x)
        x(load_breast_cancer(return_X_y=True), False)
