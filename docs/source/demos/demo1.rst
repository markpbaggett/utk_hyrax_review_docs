Demo 1: Content Models, Metadata, and the Stack
===============================================

Overview, Goals, and Outcomes
-----------------------------

========================================================
Topic from Project Charter: Content Models and Solutions
========================================================

Week of Monday, May 18, 2020. ​ Topic: Content Models and Solutions

a. Content modeling and PCDM
b. MODS to RDF
c. Explanation of underlying technologies used in the stack

===============
Goals of Demo 1
===============

1. Explain Samvera and its Philosophy
2. Explain Hyrax, its Origins, and why I'm Focusing on it for this Project
3. Explain Hyrax and its Underlying Technologies
4. Explain and Demonstrated Content Modeling in Hyrax and How it Works
5. Explain PCDM and how it is used in Hyrax
6. Explain Metadata in Hyrax, What's Out of the Box, and Demo how you Customize it

I. Samvera and its Philosophy
-----------------------------

As taken from `its website <https://samvera.org/>`_,

    Samvera™ is a vibrant and welcoming **community** of information and technology professionals who share challenges,
    build expertise, and create sustainable, best-in-class solutions, making the world’s digital collections accessible
    now and into the future.

    Samvera’s suite of repository software tools offers flexible and rich user interfaces tailored to distinct content
    types on top of a robust back end – giving adopters the best of both worlds.

To be clear, Samvera is more of a **community** than it is a software solution.

    Samvera software was conceived as an open source repository framework.  That is to say that we set out to create a
    series of free-to-use software **“building blocks”** that could put together in various combinations to achieve the
    repository system that an institution needed – as opposed to building a **“one size fits all”** solution.

The building blocks here are what you often hear referred to as **"hydra heads."**

    The framework as it exists today consists of a number of Ruby gems that can be combined, configured and adapted to
    serve a wide variety of digital repository needs.

This is very different from how Islandora 7 worked.  While Islandora 7 is extensible and you can add or create modules
to add functionality to it, it is still a discrete thing. All institutions running Islandora 7 are running more or less
the same thing.  That is not necessarily the case in *"Samvera-land"*.

In the early days of Samvera (Hydra), adopters started with basic building blocks to build the repository solution they
needed.

    Eventually, the more common approach became to find another institution whose use case was similar, clone their
    Samvera variant and then adapt it to more closely fit local needs.

Today, this is a little different.  About five years ago, the two biggest *Samvera variants*, **Curation Concerns**
and **Sufia**, merged into a common solution called **Hyrax**. If you want to know more about the history and this merger,
checkout `the Intro and About Section <https://utk-hyrax-review-docs.readthedocs.io/en/latest/contents/1_intro.html>`_.

    Hyrax is the community-developed Ruby gem that allows users **to design and build their own**, customized installation
    of our software.

Again, this is a very different approach than Islandora 7. The Samvera community believes this approach:

    ... allows an institution to build for themselves a repository solution closely fitted to their needs ...

However, the Samvera community also recognizes that the:

    ... building process and later the maintenance of such a customized system can be resource intensive ...

Because of this, the Samvera Community has seen an emerging need for some off-the-shelf “solution bundles”,
addressing particular needs, that can be installed and maintained with fewer local resources – or that can be deployed
as a hosted, cloud service. Some examples of this are:

1. `Avalon <http://www.avalonmediasystem.org/project>`_: a time-based media solution
2. `Hyku <https://hyku.samvera.org/>`_: , which is based on Hyrax, allows users to build, bundle, and promote a feature-rich, robust, flexible
digital repository that is easy to install, configure, and maintain. Hyku can be installed locally or run in the cloud;
a number of service providers offer cloud-based, hosted versions.
