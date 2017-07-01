# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-04-12 03:32:51
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-12 03:33:24
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman

import os

from spammy import Spammy

PATH = os.path.dirname(os.path.abspath(__file__))
TRAINING_CORPUS = os.path.join(PATH, 'training_dataset')
TESTING_CORPUS = os.path.join(PATH, 'test_dataset')


def main():
    # trainin the classifier on the test test
    cl = Spammy(TRAINING_CORPUS, limit=200)
    cl.train()

    # cross validating with the TEST corpus
    cl.accuracy(directory=TESTING_CORPUS, label='spam', limit=300)
    """
    >>> cl.accuracy(directory=TESTING_CORPUS, label='spam', limit=300)
    0.9554794520547946
    >>> 
    """

    cl.accuracy(directory=TESTING_CORPUS, label='ham', limit=300)
    """
    >>> cl.accuracy(directory=TESTING_CORPUS, label='ham', limit=300)
    0.9033333333333333
    >>> 
    """

if __name__ == "__main__":
    main()
