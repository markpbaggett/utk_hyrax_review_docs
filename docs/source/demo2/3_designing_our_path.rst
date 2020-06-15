III. Designing the UT Libraries Path to Hyrax from Islandora
============================================================

The findings of this grant are interesting and thought-provoking particularly for our use case. In the environtmental
scanning and institutional profiling of the grant, the team doesn't review or cover institutions who would be jumping
from Islandora and Fedora 3 to Samvera and Fedora 4 or later.  Because of this, niether the Samvera or Islandora profiles
would fit our use case.  Our case would likely be closest to the custom solution category.

This is because our Fedora 3 objects are tightly-bound with Islandora 7. In Fedora 3 and our version of Islandora, there
is no Portland Common Data Model.  Simply migrating these objects from Fedora 3 to Fedora 4 would not make them
interoperable with Hyrax because certain elements would be missing and our objects would be quite different than what
Hyrax would expect.

Let's start by thinking about a book in Islandora 7 / Fedora 3:

.. image:: ../images/islandora7_book.png

Now what might that same book look like in Hyrax?

.. image:: ../images/hyrax_book.png
