Content Modeling in Hyrax
=========================

Work Types aka "Curation Concerns"
----------------------------------

In Hyrax, types of digital repository objects are referred to as work types.  In Islandora 7, we referred to these as
content models with associated "solution packs."  It's also worth noting that these were previously referred to as
curation concerns, which is where the old front-end solution for Hydra go its name.

In Hyrax, all repositories have at least one work type that you establish with a rails generator tool. Here's an example:

.. code-block:: sh

    rails generate hyrax:work Work

You can have as many "work types" as you need, but there are few rules. The type must be camel-cased:

.. code-block:: sh

    rails generate hyrax:work MovingImage

You can namespace these if necessary by using a forward slash:

.. code-block:: sh

    rails generate hyrax:work Marks/MovingImage

Also, it's important to note that these work types often have pluralized forms that are used in routing.  Rather than
simply adding an "s", Rails attempts to guess what the route should be. If this route doesn't meet expectations you can
override it in the `config/initializers/inflections.rb` file:

.. code-block:: ruby

    ActiveSupport::Inflector.inflections(:en) do |inflect|
        inflect.irregular 'atlas', 'atlases'
    end

