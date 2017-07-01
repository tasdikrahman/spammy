# -*- coding: utf-8 -*-
# @Author: tasdik
# @Date:   2016-04-11 19:33:30
# @Last Modified by:   tasdik
# @Last Modified time: 2016-04-11 23:02:20
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/tasdikrahman


class SpammyError(Exception):
    """A Spammy related error"""

    def __call__(self, *args):
        return self.__class__(*(self.args + args))

SpammyException = SpammyError


class CorpusFileError(SpammyError):
    """
    Raised when the one of the corpus files passed to the spammy ctor do not
    exist

    OR 

    When we do not pass any file to the ctor for initialization
    """

CorpusError = CorpusFileError('Directory does not exist')


class LimitError(SpammyError):
    """
    raised when the limit passed is either less than 0
    """
    pass
