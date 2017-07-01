.. spammy documentation master file, created by
   sphinx-quickstart on Tue Apr 12 19:17:46 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|Pypi version| |Build Status| |percentagecov| |Requirements Status| |License| 

.. contents::
    :backlinks: none

.. sectnum::

spammy
======

:Author: `Tasdik Rahman <http://tasdikrahman.me>`__
:Latest version: 1.0.0



Overview
--------

`spammy <https://github.com/tasdikrahman/spammy>`__ : Spam filtering at your service

Features
--------

- train the classifier on your own dataset to classify your emails into spam or ham
- Dead simple to use. See `usage <#example>`__
- Blazingly fast once the classifier is trained. (See `benchmarks <#benchmarks>`__)
- Custom exceptions raised so that when you miss something, spammy tells you where did you go wrong in a graceful way
- Written in uncomplicated ``python``
- Built on top of the giant shoulders of `nltk <http://nltk.org>`__

Example
-------
`[back to top] <#overview>`__

.. code:: python

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
    >>> cl.train()
    >>>
    >>> SPAM_TEXT = \
    ... """
    ... My Dear Friend,
    ... 
    ... How are you and your family? I hope you all are fine.
    ... 
    ... My dear I know that this mail will come to you as a surprise, but it's for my 
    ... urgent need for a foreign partner that made me to contact you for your sincere
    ... genuine assistance My name is Mr.Herman Hirdiramani, I am a banker by 
    ... profession currently holding the post of Director Auditing Department in 
    ... the Islamic Development Bank(IsDB)here in Ouagadougou, Burkina Faso.
    ... 
    ... I got your email information through the Burkina's Chamber of Commerce 
    ... and industry on foreign business relations here in Ouagadougou Burkina Faso 
    ... I haven'disclose this deal to any body I hope that you will not expose or 
    ... betray this trust and confident that I am about to repose on you for the 
    ... mutual benefit of our both families.
    ... 
    ... I need your urgent assistance in transferring the sum of Eight Million,
    ... Four Hundred and Fifty Thousand United States Dollars ($8,450,000:00) into
    ... your account within 14 working banking days This money has been dormant for 
    ... years in our bank without claim due to the owner of this fund died along with 
    ... his entire family and his supposed next of kin in an underground train crash 
    ... since years ago. For your further informations please visit 
    ... (http://news.bbc.co.uk/2/hi/5141542.stm)
    ... """
    >>> cl.classify(SPAM_TEXT)
    'spam'
    >>>

**Accuracy of the classifier**

.. code:: python

    >>> from spammy import Spammy
    >>> directory = '/home/tasdik/Dropbox/projects/spammy/examples/training_dataset'
    >>> cl = Spammy(directory, limit=300)  # training on only 300 spam and ham files
    >>> cl.train()
    >>> cl.accuracy(directory='/home/tasdik/Dropbox/projects/spammy/examples/test_dataset', label='spam', limit=300)
    0.9554794520547946
    >>> cl.accuracy(directory='/home/tasdik/Dropbox/projects/spammy/examples/test_dataset', label='ham', limit=300)
    0.9033333333333333
    >>> 

**More examples can be found over in the `examples directory <https://github.com/tasdikrahman/spammy/tree/master/examples>`__ **

Installation
------------
`[back to top] <#overview>`__

.. figure:: http://hd.wallpaperswide.com/thumbs/shut_up_and_take_my_money-t2.jpg
    :alt:

**Install the dependencies first**

.. code:: bash

    $ pip install nltk==3.2.1, beautifulsoup4==4.4.1


To install use pip:

.. code:: bash

    $ pip install spammy

or use easy_install

.. code:: bash

    $ easy_install spammy

Or build it yourself (only if you must):


.. code:: bash

    $ git clone https://github.com/tasdikrahman/spammy.git
    $ python setup.py install

Upgrading
~~~~~~~~~

To upgrade the package, 

.. code:: bash

    $ pip install -U spammy

Installation behind a proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are behind a proxy, then this should work
    
.. code:: bash

    $ pip --proxy [username:password@]domain_name:port install spammy

Benchmarks
----------
`[back to top] <#overview>`__

Spammy is blazingly fast once trained

Don't believe me? Have a look

.. code:: python

    >>> import timeit
    >>> from spammy import Spammy
    >>>
    >>> directory = '/home/tasdik/Dropbox/projects/spamfilter/data/corpus3'
    >>> cl = Spammy(directory, limit=100)
    >>> cl.train()
    >>> SPAM_TEXT_2 = \
    ... """
    ... INTERNATIONAL MONETARY FUND (IMF)
    ... DEPT: WORLD DEBT RECONCILIATION AGENCIES.
    ... ADVISE: YOUR OUTSTANDING PAYMENT NOTIFICATION
    ...  
    ... Attention
    ... A power of attorney was forwarded to our office this morning by two gentle men,
    ... one of them is an American national and he is MR DAVID DEANE by name while the
    ... other person is MR... JACK MORGAN by name a CANADIAN national.
    ... This gentleman claimed to be your representative, and this power of attorney 
    ... stated that you are dead; they brought an account to replace your information 
    ... in other to claim your fund of (US$9.7M) which is now lying DORMANT and UNCLAIMED,
    ...  below is the new account they have submitted:
    ...                     BANK.-HSBC CANADA
    ...                     Vancouver, CANADA
    ...                     ACCOUNT NO. 2984-0008-66
    ...  
    ... Be further informed that this power of attorney also stated that you suffered.
    ... """
    >>>
    >>> def classify_timeit():
    ...    result = cl.classify(SPAM_TEXT_2)
    ... 
    >>> timeit.repeat(classify_timeit, number=5)
    [0.1810469627380371, 0.16121697425842285, 0.16121196746826172]
    >>>


Contributing
------------
`[back to top] <#overview>`__

Refer `CONTRIBUTING <https://github.com/tasdikrahman/spammy/tree/master/CONTRIBUTING.rst>`__ page for details

Roadmap
~~~~~~~

- Include more algorithms for increased accuracy

Licensing
---------
`[back to top] <#overview>`__

Spammy is built by `Tasdik Rahman <http://tasdikrahman.me>`__ and licensed under GPLv3.

    spammy
    Copyright (C) 2016  Tasdik Rahman(prodicus@outlook.com)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

You can find a full copy of the LICENSE file `here <https://github.com/tasdikrahman/spammy/tree/master/LICENSE.txt>`__

Credits
-------
`[back to top] <#overview>`__

If you'd like give me credit somewhere on your blog or tweet a shout out to `@tasdikrahman <https://twitter.com/tasdikrahman>`__, well hey, I'll take it.


.. |PyPI version| image:: https://img.shields.io/pypi/v/spammy.svg
   :target: https://pypi.python.org/pypi/spammy
.. |Build Status| image:: https://travis-ci.org/tasdikrahman/spammy.svg?branch=master
    :target: https://travis-ci.org/tasdikrahman/spammy
.. |License| image:: https://img.shields.io/pypi/l/spammy.svg
   :target: https://pypi.python.org/pypi/spammys
.. |grade| image:: https://api.codacy.com/project/badge/grade/c61c09b6c4ca4580b1f24c03ce3ad8e2
    :target: https://www.codacy.com/app/tasdik95/spammy
.. |percentagecov| image:: https://api.codacy.com/project/badge/coverage/e2cb32eae16242f795f498d40d0d8984
    :target: https://www.codacy.com/app/tasdik95/spammy
.. |Requirements Status| image:: https://requires.io/github/tasdikrahman/spammy/requirements.svg?branch=master
     :target: https://requires.io/github/tasdikrahman/spammy/requirements/?branch=master
     :alt: Requirements Status

Documentation
=============

.. toctree::
   :maxdepth: 4

   api_reference


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

