IV. Fedora 6 and the Oxford Common File Layout
==============================================

In the last demo, I got some specific questions about Fedora 6 and Hyrax Samvera.  Since we're talking migration, I felt
it was necessary to lend some time to talk about OCFL, Fedora 6, and how it relates to Samvera and Hyrax specifically.

=============================
What is the focus of Fedora 6
=============================

|:star:| Reduce effort to migrate from Fedora 2 and 3

|:star:| Enhance long term preservation

|:star:| Improve performance and scale

============================================
The Focus as it relates to Samvera and Hyrax
============================================

The Samvera community starting moving to Fedora 4 very early (2014). Almost immediately, certain Samvera repositories
started to report issues under certain scenarios specifically related to the third star here.

=======================================
How is Fedora 6 different than Fedora 5
=======================================

|:star:| ModeShape (or lack thereof)

Fedora 4 and 5 is built upon an open source repository platform called ModeShape.  ModeShape in recent years has decreased
in popularity and also was the primary source of all the performance and scale issues that repositories experienced in
Fedora 4 and 5. Fedora

|:star:| Implements Oxford Common File Layout (back to that in a sec)

===============================================================
How difficult will it be for Hyrax and Samvera to move to OCFL?
===============================================================

As far as making Rails work with Fedora, not at all.  Fedora 6 **completely** retains alignment with the Fedora API.
Therefore both ActiveFedora and Valkyrie / Wings work with Fedora 6 out of the box.

The big change is the underlying persistence layer underneathe Fedora 6 (OCFL), so anyone running Fedora 4 or 5 will have
to migrate there Fedora implentation to use OCFL.

Because of this, Fedora 6 is focusing on building and releasing **robust** migration utilities and other tooling to make
this migration easier.

================
So what is OCFL?
================

At a high level, you can think of OCFL as a:

    simple, non-proprietary, specified, open standards approach to the layout of the preservation persistence layer in a repository.

A simpler way of thinking about OCFL:

    a specification that is file system agnostic (cloud, bare metal, whatever) that describes how to layout content on whatever storage media you choose

OCFL is focused on several things.  The first is **parseability**:

    In disaster recovery situations, **humans** should be able to understand the content.

    Similarly, machine readability allows for simple applications to be placed on top of an existing OCFL storage root.

The next is **robustness**.  OCFL wants to protect the repository from errors, corruption, and migration between storage media (bare metal to cloud and vice versa).

    Strong fixity and use of checksums is built into OCFL.

    Content can easily be validated using the inventory.json files.

    Objects are completely self-contained.  Everything you need to understand about an object and its relationships is in the OCFL object.

The next is **versioning**. OCFL ensures:

    Changes to objects are tracked over time with auditing information.

    OCFL employs forward delta.  This means that when a new version of an object is created, only the things that are different are stored in the new version. All other files are stored in their original directory.

    The inventory file is built in a way to make it easy for previous versions of objects to be restored, or as they say, *reconstructed*.

The next is **storage diversity**.

    OCFL is file system agnostic.

Finally, the most important, **completeness**. This means ensuring that a repository can be completely restored by reading in content in the OCFL format.

    This falls in line with Trusted Digital Repositories (ISO 16363), NDSA Levels of Preservation, and Open Archival Information Systems (OAIS).

    While these standards talk about what you should do, OCFL explains how to do it.

=========================
So Why Is OCFL Important?
=========================

|:star:| Longterm disaster preparedness

|:star:| Ability to rebuild a repository from contents on disk

==========================================================================
Is it easier to migrate from Fedora 3 to Fedora 5 or Fedora 3 to Fedora 6?
==========================================================================

The answer is the latter.  This is because the data in your Fedora 3 repository can be transformed in place.

Migration utilities can be run to take the Fedora 3 data and create Fedora 6 OCFL-compliant data.  Once that is done,
you can simply drop a Fedora 6 instance on top of your Fedora 6, OCFL compliant data and read it in.

============================================
What else does having OCFL as a standard do?
============================================

Makes future migrations easier because repositories (including things that are not Fedora) now have a specification for
how to layout data and be compliant with TDR, OAIS, etc.

Data will no longer conform to applications. **Applications will conform to data.**

According to David Wilcox, the main source of corruption of objects and files in digital repositories occurs during migrations.

=================
Is OCFL released?
=================

No, Beta 0.3 was released in June 2019.  Version 1.0 should be released **soon**. All criteria for a 1.0 release have been met.

==================================================
Who is implementing and building tooling for OCFL?
==================================================

|:star:| Johns Hopkins University - Go client

|:star:| Cornell University - Python client, validator (Hyrax shop)

|:star:| Penn State - Go client (Hyrax shop)

|:star:| University of Wisconsin, Madison - Java client (Hyrax shop)

|:star:| Stanford - Ruby client, validator, and test suite (Hyrax shop plus dozens of other Samvera flavors)

|:star:| University of Technology, Sydney - Javascript client

|:star:| Brown University - Clojure HTTP server (Hyrax shop)

==================================
Example of a Versioned OCFL Object
==================================

So what does an example of an OCFL object look like?

.. code-block:: text

    object_root
    ├── 0=ocfl_object_1.0
    ├── inventory.json
    ├── inventory.json.sha512
    ├── v1
    │   ├── inventory.json
    │   ├── inventory.json.sha512
    │   └── content
    │       ├── empty.txt
    │       ├── foo
    │       │   └── bar.xml
    │       └── image.tiff
    ├── v2
    │   ├── inventory.json
    │   ├── inventory.json.sha512
    │   └── content
    │       └── foo
    │           └── bar.xml
    └── v3
        ├── inventory.json
        └── inventory.json.sha512

