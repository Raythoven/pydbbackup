pgbackup
=========

CLI for backup remote PostgreSQL database either locally or to S3

Preparing the Dev
--------------

1. Ensure ``pip`` and ``pipenv`` are installed2.
2. Clone repo: ``example``
3. ``cd`` into the repo
4. Fetch development dependencies ``make install``
5. Activate virtualenv ``pipenv shell``


Usage
------

Pass in a full databasue IRL, the storage driver, and the destination

S3 Example w/ bucket name:

::

    $pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w local path:

::

    $pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql


Running Tests
------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make

