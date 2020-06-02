IV. The Hyrax Stack
-------------------

Samvera stacks broadly look like this:

.. image:: ../images/Samvera-Components-Diagram.png

I say broadly because some of the middleware is changing (i.e. Valkyrie vs. ActiveFedora), but we aren't getting there
today.

========
The Core
========

At the core of Hyrax are **Fedora** and **Solr**. Hyrax currently uses **Fedora 4** as its persistence layer. These two
services are is where the actual content and its associated metadata **(or pointers to them)** are stored.

Interaction with Fedora happens via an HTTP API. Fedora 4 stores its content as linked data. We'll look at this more
later.

Apache Solr is used as the basis for search. Content from Fedora is indexed into Solr via **ActiveFedora**, a Ruby gem.

Interaction with Solr also happens via an HTTP API.

==========
Middleware
==========

1. `hydra-head <https://github.com/projecthydra/hydra-head>`_:  This is one of those things I've heard about for years but never really understood.  This is a Ruby-on-Rails gem containing the core code for a web application using the full stack of Samvera building blocks. This is maybe similar to the old `islandora/islandora <https://github.com/islandora/islandora>`_ from Islandora 7.
2. **active-fedora**: Ruby on Rails normally follows the Active Record pattern to persist objects to its database. In Hyrax, an alternative pattern called ActiveFedora is used to persist objects to Fedora.
3. **ldp**: A ruby gem called ldp is used to implement the LDP (Linked Data Platform) interaction patterns for interaction with containers in Fedora.
4. **rsolr**: Rsolr is a ruby client for interacting with Solr.
5. **blacklight**:  Most search and display behavior in Hyrax is inherited from Blacklight. Many Samvera institutions also run Blacklight applications separately from Samvera itself, to provide search and discovery for their other collections (think our use of **Ex Libris Primo**). The Blacklight Project also has many of its own plugins, such as **Spotlight** for building virtual exhibits, and **GeoBlacklight** which enhances Blacklight for use with geospatial data.

============
Other things
============

1. **Queuing System and Redis**: Hyrax does not package a default queuing back-end. There are a lot flavors here (**Sidekiq**, **Resque**, and **DelayedJob**) but they all have **Redis** as a dependency.  `Sidekiq <https://github.com/samvera/hyrax/wiki/Using-Sidekiq-with-Hyrax>`_ is most popular.
2. **Postgres**: You of course need a database layer of some kind and most of the Rails world prefers Postgres over Maria / MySQL. In my investigation, I haven't found any institutions not using PostGres except for testing.
3. *An External Triple Store?*: You may be wondering, where is the external triple store for storing minted objects? Hyrax does not package one and it is entirely optional based on your needs.
