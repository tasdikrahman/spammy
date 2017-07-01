Contributing
============

1. Fork it.

2. Clone it 

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__ 

.. code:: bash

    $ virtualenv env              # Create virtual environment
    $ source env/bin/activate     # Change default python to virtual one
    (env)$ git clone https://github.com/tasdikrahman/spammy.git
    (env)$ cd spammy
    (env)$ pip install -r requirements.txt  # Install requirements for 'spammy' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py env    # Create virtual environment
    $ source env/bin/activate     # Change default python to virtual one
    (env)$ git clone https://github.com/tasdikrahman/spammy.git
    (env)$ cd spammy
    (env)$ pip install -r requirements.txt  # Install requirements for 'spammy' in virtual environment

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)

5. Run tests

``nosetests`` is being used as the testing suite. To run the tests 

.. code:: bash

    (env) $ nosetests

Conform to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ and if everything is running fine, integrate your feature 

6. Push to the branch (``$ git push origin my-new-awesome-feature``)

7. Create new Pull Request

Hack away! 