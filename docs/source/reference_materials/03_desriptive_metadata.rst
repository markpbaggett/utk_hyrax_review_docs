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

Hyrax's Metadata Application Profile and Applying our MODS to RDF
-----------------------------------------------------------------

As you'll see in the next chapter, Hyrax's Default Metadata Mapping is extremely basic and to some extent bad.  To be
honest, it does not even adhere to Linked Data principles appropriately. Because of this we would need to do a few things
prior to moving to Hyrax:

1. Create our own MODS to RDF mapping based on our data and needs

    Over time, we have developed our own practices based on our needs.  To ensure our migration is not lossy, we must first
    develop a  MODS to RDF mapping and associated metadata application profile for RDF.

2. Determine if we need an external triple store

    Hyrax does not ship with an external triple store.  If we need one, we will need to select one and install it.

3. Modify the default metadata application profile to remove bad elements or one's that don't meet our needs

    As you'll see in the next chapter, Hyrax's MAP is bad.  We need to modify the bad elements to be good base on our MAP
    and removed the good but unneeded metadata elements.

4. Expand the models of our generated works to include other required elements

    Once we have determined what work types we need, we need to update their models to have our other elements.

5. If necessary, modify code so that Hyrax can "talk" to our external triple store

    More info can be found `here <https://wiki.lyrasis.org/display/samvera/Hydra+Triple+Store+Interest+Group>`_.


Leveraging our "Linked Data-Ready" Elements During Migration
------------------------------------------------------------
