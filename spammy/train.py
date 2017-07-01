# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @Date:   2016-03-12
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-12 16:54:10
# @MIT License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman


"""
Trainer class for the classifier
"""

from __future__ import absolute_import

import os
import string
import re
import codecs
import mimetypes

# specify the folder `/path_to_plino/nltk_data/` as heroku will not be having
# the nltk installed in it!
APP = os.path.abspath(__file__)
FILE_DIR, APP_NAME = os.path.split(APP)
NLTK_DATA_PATH = os.path.join(FILE_DIR, 'nltk_data')

import nltk
nltk.data.path.append(NLTK_DATA_PATH)

import bs4
from nltk.corpus import stopwords
from nltk import stem  # uses PoterStemmer()

from spammy.classifier import NaiveBayesClassifier


class Trainer(object):

    """
    The trainer class
    """

    def __init__(self, directory, spam, ham, limit):
        """
        :param self: Trainer object
        :param directory: location of the training dataset
        :param spam: the sub directory inside the 'directory' which has spam
        :param ham: the sub directory inside the 'directory' which has ham
        :param limit: The maximum number of mails, the classifier should \
                      be trained over with
        """

        self.spamdir = os.path.join(directory, spam)
        self.hamdir = os.path.join(directory, ham)
        self.limit = limit

        self.classifier = NaiveBayesClassifier()

    def train_classifier(self, path, label):
        """
        The function doing the actual classification here.

        :param self: Trainer object
        :param path: The path of the data directory
        :param label: The label underwhich the data directory is
        """

        limit = len(os.listdir(path)) < self.limit and len(os.listdir(path)) \
            or self.limit

        # changing the path to that particular directory
        os.chdir(path)

        for email in os.listdir(path)[:self.limit]:
            email_file = open(email, 'r')  # explicit better than implicit
            email_text = email_file.read()

            """
            Don't even get me started on the Unicode issues that I faced
            here. Thankfullly 'BeautifulSoup' was there to our rescue.

            Thanks to Leonard Richardson for this module
            """

            try:
                email_text = bs4.UnicodeDammit.detwingle(
                    email_text).decode('utf-8')
            except:
                "Skipping the file for bad encoding"
                continue

            email_file.close()
            email_text = email_text.encode("ascii", "ignore")

            # Extracting the features from the text
            features = self.extract_features(email_text)

            # Training the classifier
            self.classifier.train(features, label)

    def train(self):
        """
        Starts the training process on the directories passed by the user

        :param self: Trainer object
        """
        self.train_classifier(self.spamdir, 'spam')
        self.train_classifier(self.hamdir, 'ham')

        return self.classifier

    def extract_features(self, text):
        """
        Will convert the document into tokens and extract the features.

        .. note:: 

            So these are some possible features which would make an email a SPAM

            features looked for
            - Attachments
            - Links in text
            - CAPSLOCK words
            - Numbers
            - Words in text


        :param self: Trainer object
        :param text: Email text from which we will extract features
        :returns: A list which contains the feature set
        :rtype: list
        """
        features = []
        tokens = text.split()
        link = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        # ^ for detecting whether the string is a link

        # Will use PorterStemmer() for stemming
        porterStemmer = stem.porter.PorterStemmer()

        # cleaning out the stopwords
        tokens = [
            token for token in tokens if token not in stopwords.words(
                "english"
            )
        ]

        for token in tokens:
            if len(token.translate(None, string.punctuation)) < 3:
                continue
            if token.isdigit():
                features.append("NUMBER")
            elif "." + token in mimetypes.types_map.keys():
                """
                >>> import mimetypes
                >>> mimetypes.types_map.keys()
                ['.obj', '.ra', '.wsdl', '.dll', '.ras', '.ram', '.bcpio',
                 '.sh', '.m1v', '.xwd', '.doc', '.bmp', '.shar', '.js',
                 '.src', '.dvi', '.aif', '.ksh', '.dot', '.mht', '.p12',
                 '.css', '.csh', '.pwz', '.pdf', '.cdf', '.pl', '.ai',
                 '.jpe', '.jpg', '.py', '.xml', '.jpeg', '.ps', '.gtar',
                 '.xpm', '.hdf', '.nws', '.tsv', '.xpdl', '.p7c', '.ico',
                 '.eps', '.ief', '.so', '.xlb', '.pbm', '.texinfo', '.xls',
                 '.tex', '.rtx', '.html', '.aiff', '.aifc', '.exe', '.sgm',
                 '.tif', '.mpeg', '.ustar', '.gif', '.ppt', '.pps', '.sgml',
                 '.ppm', '.latex', '.bat', '.mov', '.ppa', '.tr', '.rdf',
                 '.xsl', '.eml', '.nc', '.sv4cpio', '.bin', '.h', '.tcl',
                 '.wiz', '.o', '.a', '.c', '.wav', '.vcf', '.xbm', '.txt',
                 '.au', '.t', '.tiff', '.texi', '.oda', '.ms', '.rgb', '.me',
                 '.sv4crc', '.qt', '.mpa', '.mpg', '.mpe', '.avi', '.pgm',
                 '.pot', '.mif', '.roff', '.htm', '.man', '.etx', '.zip',
                 '.movie', '.pyc', '.png', '.pfx', '.mhtml', '.tar', '.pnm',
                 '.pyo', '.snd', '.cpio', '.swf', '.mp3', '.mp2', '.mp4']
                >>>
                """
                features.append("ATTACHMENT")
            elif token.upper() == token:
                features.append("ALL_CAPS")
                features.append(
                    porterStemmer.stem(
                        token.translate(None, string.punctuation)
                    ).lower()
                )
            elif link.match(token):
                features.append("LINK")
            else:
                features.append(
                    porterStemmer.stem(token.translate(
                        None, string.punctuation
                        )
                    ).lower()
                )

        return features
