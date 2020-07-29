X. Platform Proof of Concept
============================

This demo is accompanied by a Docker instance of the app that was created during testing. The test app is available
for download on `GitHub <https://github.com/markpbaggett/utk_hyrax_test>`_.

Requirements
------------

The Docker instance requires:

* docker-compose 3.6 or greater
* docker 19 or greater

Default Ports Used
------------------

* 3000 - Rails
* 8983 - Solr
* 8984 - Fedora
* 6379 - Redis

Building and Running
--------------------

To build and start:

.. code-block:: shell

    docker-compse run web rails db:setup
    docker-compose up -d

To run test specs:

.. code-block:: shell

    docker-compose run web rspec

To enter bash on a running web container:

.. code-block:: shell

    docker-compose run web bash
