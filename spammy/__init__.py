# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-04-11 18:52:17
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-12 17:07:33
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman

from __future__ import absolute_import, division
import os

import bs4
from spammy.train import Trainer
from spammy.exceptions import CorpusFileError, CorpusError, LimitError
from spammy.version import VERSION


__title__ = 'spammy'
__version__ = VERSION
__author__ = 'Tasdik Rahman'
__email__ = 'prodicus@outlook.com'
__license__ = 'GPLv3'
__copyright__ = 'Copyright 2016 Tasdik Rahman'

class Spammy(object):

    """Stiches everything from train module and classifier module together"""

    def __init__(self, directory=None, limit=None, **kwargs):
        """
        Initializing the essential

        :param directory: Pass the full path of the directory where your
                          training data is 
        :param spam: folder spam inside the 'directory'
        :param ham: folder ham inside the 'directory'
        :param limit: limit the number of files for the classifier to be
                      trained upon when training the classifier                      

        :Example:

            >>> import os
            >>> from spammy import Spammy
            >>>
            >>> directory = '/home/tasdik/Dropbox/projects/spamfilter/data/corpus3'
            >>>
            >>> # directory structure
            >>> os.listdir(directory)
            ['spam', 'Summary.txt', 'ham']
            >>> os.listdir(os.path.join(directory, 'spam'))[:5]
            ['4257.2005-04-06.BG.spam.txt', '0724.2004-09-21.BG.spam.txt', '2835.2005-01-19.BG.spam.txt', '2505.2005-01-03.BG.spam.txt', '3992.2005-03-19.BG.spam.txt']
            >>>
            >>> # Spammy object created
            >>> cl = Spammy(directory, limit=100)
            
        """
        if kwargs:
            spam = kwargs['spam']
            ham = kwargs['ham']
        else:
            spam = 'spam'
            ham = 'ham'

        """checking if the directories passed are valid ones or not"""

        if not os.path.isdir(directory):
            raise CorpusError(directory)
        if not os.path.isdir(os.path.join(directory, ham)):
            raise CorpusError(ham)
        if not os.path.isdir(os.path.join(directory, spam)):
            raise CorpusError(spam)

        if limit < 0:
            raise LimitError("Limit cannot be less than 0")

        safe_limit = min(len(os.listdir(os.path.join(directory, spam))),
                         len(os.listdir(os.path.join(directory, ham))))

        if limit > safe_limit:
            limit = safe_limit

        self.directory = directory
        self.ham = os.path.join(self.directory, ham)
        self.spam = os.path.join(self.directory, spam)
        self.limit = limit


    def train(self):
        """
        Trains the classifier object

        :param self: the classifier object

        :Example:

            >>> from spammy import Spammy
            >>> directory = '/home/tasdik/Dropbox/projects/spammy/examples/training_dataset'
            >>> cl = Spammy(directory, limit=300)  # training on only 300 spam and ham files
            >>> cl.train()

        """
        kwargs = {
            "directory": self.directory,
            "spam": self.spam,
            "ham": self.ham,
            "limit": self.limit
        }

        self.trainer = Trainer(**kwargs)
        self.classifier_object = self.trainer.train()


    def classify(self, email_text):
        """
        tries classifying text into spam or ham

        :param email_text: email_text to be passed here which is to be classified
        :returns: Either ham or spam
        :rtype: str

        .. note :: To be run after you have trained the classifier object on your dataset

        :Example:

            >>> from spammy import Spammy
            >>> cl = Spammy(path_to_trainin_data, limit=200)
            # 200 or the number of files you need to train the classifier upon
            >>>  
            >>> HAM_TEXT = \
            '''
            Bro. Hope you are fine. Hows the work going on ? Can you send me some updates on it.
            And are you free tomorrow ?
            No problem man. But please make sure you are finishing it 
            by friday night and sending me on on that day itself. As we 
            have to get it printed on Saturday.
            '''
            >>> cl.classify(HAM_TEXT)
            'ham'

        """
        email_text = bs4.UnicodeDammit.detwingle(email_text).decode('utf-8')
        email_text = email_text.encode('ascii', 'ignore')
        return self.classifier_object.classify(
            self.trainer.extract_features(email_text)
            )


    def accuracy(self, **kwargs):
        """
        Checks the accuracy of the classifier by running it against a testing
        corpus

        :param limit: number of files the classifier should test upon
        :param label: the label as in spam or ham
        :param directory: The absolute path of the directory to be tested
        :returns: the precision of the classifier. Eg: 0.87
        :rtype: float

        :Example:

            >>> from spammy import Spammy
            >>> directory = '/home/tasdik/Dropbox/projects/spammy/examples/training_dataset'
            >>> cl = Spammy(directory, limit=300)  # training on only 300 spam and ham files
            >>> cl.train()
            >>> cl.accuracy(directory='/home/tasdik/Dropbox/projects/spammy/examples/test_dataset', label='spam', limit=300)
            0.9554794520547946
            >>> cl.accuracy(directory='/home/tasdik/Dropbox/projects/spammy/examples/test_dataset', label='ham', limit=300)
            0.9033333333333333
            >>>

        """
        directory = kwargs['directory']
        label = kwargs['label']
        limit = kwargs['limit']

        if not os.path.isdir(directory):
            raise CorpusError(directory)

        if not os.path.isdir(os.path.join(directory, label)):
            raise CorpusError(os.path.join(directory, label))
            
        if limit < 0:
            raise LimitError("Limit cannot be less than 0")

        label_dir = os.path.join(directory, label)
        safe_limit = len(os.listdir(label_dir))

        if limit > safe_limit:
            limit = safe_limit

        os.chdir(label_dir)

        correct = 0
        total = 0

        for email in os.listdir(label_dir)[:limit]:
            email = os.path.join(label_dir, email)
            email_file = open(email, 'r')
            email_text = email_file.read()
            email_file.close()
            try:
                email_text = bs4.UnicodeDammit.detwingle(email_text).decode(
                    'utf-8'
                )
            except:
                # bad encoding error, skipping file
                continue
            email_text = email_text.encode('ascii', 'ignore')

            hamorspam = self.classifier_object.classify(
            self.trainer.extract_features(email_text)
            )

            total += 1
            if hamorspam == label:
                correct += 1

        precision = correct / total

        return precision