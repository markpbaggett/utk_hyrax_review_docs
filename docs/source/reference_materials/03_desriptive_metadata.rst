III. Migrating Our Linked Data Ready Metadata
=============================================

Introduction
------------

Since 2015, UT Libraries has worked diligently to make our metadata "linked data-ready." You can see this throughout our
MODS with the presence of URIS in `valueURI` and `xlink:href` URIs.

While we've worked to make our data "linked-data ready," this part of our migration will be complex because we have our
own practices that are different from other libraries.  This is because our needs are different and our metadata has been
influence from local requirements and the requirements of metadata sharing agreements with things like the Digital
Publice Library of America.

In this chapter I will focus on:

* An explanation and justification for what we must do prior to migration
* Demonstrate how we can leverage our "linked data-ready" elements during migration.

In the next chapter, I will describe in detail:

* Hyrax's default RDF metadata mapping
* What we lose if we use it out of the box
* Alternative mappings
