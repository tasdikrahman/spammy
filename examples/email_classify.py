# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-04-11 23:46:26
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-04-12 03:35:04
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman

HAM_TEXT = \
    """
Bro. Hope you are fine.

Hows the work going on ? Can you send me some updates on it.

And are you free tomorrow ?

No problem man. But please make sure you are finishing it 
by friday night and sending me on on that day itself. As we 
have to get it printed on Saturday.
"""

SPAM_TEXT = \
    """
My Dear Friend,

How are you and your family? I hope you all are fine.

My dear I know that this mail will come to you as a surprise, but it's for my 
urgent need for a foreign partner that made me to contact you for your sincere
genuine assistance My name is Mr.Herman Hirdiramani, I am a banker by 
profession currently holding the post of Director Auditing Department in 
the Islamic Development Bank(IsDB)here in Ouagadougou, Burkina Faso.

I got your email information through the Burkina's Chamber of Commerce 
and industry on foreign business relations here in Ouagadougou Burkina Faso 
I haven'disclose this deal to any body I hope that you will not expose or 
betray this trust and confident that I am about to repose on you for the 
mutual benefit of our both families.

I need your urgent assistance in transferring the sum of Eight Million,
Four Hundred and Fifty Thousand United States Dollars ($8,450,000:00) into
your account within 14 working banking days This money has been dormant for 
years in our bank without claim due to the owner of this fund died along with 
his entire family and his supposed next of kin in an underground train crash 
since years ago. For your further informations please visit 
(http://news.bbc.co.uk/2/hi/5141542.stm)
"""

import os

from spammy import Spammy

PATH = os.path.dirname(os.path.abspath(__file__))
TRAINING_CORPUS = os.path.join(PATH, 'training_dataset')


def main():
    # trainin the classifier on the test test
    cl = Spammy(TRAINING_CORPUS, limit=200)
    cl.train()

    # classfying texts one at a time
    print cl.classify(SPAM_TEXT)
    """
    >>> cl.classify(SPAM_TEXT)
    'spam'
    """

    print cl.classify(HAM_TEXT)
    """
    >>> cl.classify(HAM_TEXT)
    'ham'
    """

if __name__ == "__main__":
    main()
