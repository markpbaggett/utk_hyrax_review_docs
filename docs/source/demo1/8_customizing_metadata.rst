VIII. Customizing Your Metadata
-------------------------------

========================
Exercise / Demo Overview
========================

If you're running Islandora 7, you don't necessarily need developers. This likely is not the case if you're using Hyrax.

A good example of this is metadata customization. Let's say we want to add a field in addition to the out-of-the-box
Hyrax fields. Let's demonstrate what the initial work here looks like.

Before we start, we need a field. You can't use these because I added them already as part of my exploration of Hyrax:

1. skos:Note (http://www.w3.org/2004/02/skos/core#note)
2. edm:Year (http://www.europeana.eu/schemas/edm/year)

Also, this is RDF / LDP. If we're adding a field, we need a predicate.

If you can't come up with one, here are a few you can choose from:

1. dct:extent (http://purl.org/dc/terms/extent)
2. relators:photographer (http://id.loc.gov/vocabulary/relators/pht)

=================================================
Capybara, Integration / Feature Tests, Unit Tests
=================================================

Hyrax uses `Capybara <https://teamcapybara.github.io/capybara/>`_ to automate integration tests and unit tests for the
entire application. Because we are adding a new metadata field, we **SHOULD** add integration tests and unit tests instead
of simply adding the field.

This will allow us to make certain that our Hyrax application does not have bugs that we cause.

When I'm talking about feature or integration tests, I mean tests that happen directly in the browser. Capybara uses
Selenium and Webkit to perform these.

To run all our tests, we're simply going to:

.. code-block:: sh

    rspec spec

If I only want to run tests in a specific file:

.. code-block:: sh

    rspec spec/features/create_image_spec.rb

========================
Step 1. Integration Test
========================

It may seem backwards, but you always start with your integration / feature request.

We do this because it forces us to decide what we expect should happen first.

Let's open `spec/features/create_image_spec.rb` which Hyrax provided for me when I created my work, `Image`. Let's add
some lines to tell Capybara what to do.

.. code-block:: ruby

    click_link("Additional fields")
    fill_in "Extent", with: "3 1/4 x 5 inches"

If we were to run `rspec` now, it will fail because we haven't updated our model yet.

==============================
Step 2. Unit Testing Our Model
==============================

Again, it may seem backwards, but we need to write a unit test for our change to our Image model in `spec/models/image_spec.rb`.

.. code-block:: ruby

      describe "#extent" do
        context "with a new Image" do
          it "has no extent value when it is first created" do
            image = Image.new
            expect(image.extent).to be_empty
          end
        end

        context "with an Image that has an extent defined" do
          it "can set and retrieve an extent value" do
            image = Image.new
            image.extent = ["3 1/4 x 5 inches"]
            expect(image.extent).to eq(["3 1/4 x 5 inches"])
          end
        end
      end

If you run tests now, you'll have even more fails! Let's start to fix these.

========================================================
Step 3. Add the New Field and its Predicate to our Model
========================================================

To add our new field and its predicate to our model, let's edit `app/models/image.rb` and add the following before
`include ::Hyrax::BasicMetadata`:

.. code-block:: ruby

    property :extent, predicate: "http://purl.org/dc/terms/extent"

This updates our model. Running rspec now will result in passing unit tests but failing integration tests.

====================================
Step 4. Add a Unit Test for our Form
====================================

Our integration tests will fail because we have no field! But before we add one, we need a unit test!

We can add our test to `spec/forms/hyrax/image_form_spec.rb`:

.. code-block:: ruby

      subject { form }
      let(:image)    { Image.new }
      let(:ability) { Ability.new(nil) }
      let(:request) { nil }
      let(:form)    { described_class.new(image, ability, request) }
      it "has the expected terms" do
        expect(form.terms).to include(:title)
        expect(form.terms).to include(:year)
        expect(form.terms).to include(:extent)
      end

=============================
Step 5. Add Field to our Form
=============================

Rspec will still fail until will modify `app/forms/hyrax/image_form.rb` and add our field:

.. code-block:: ruby

    self.terms += [:extent]

====================================
Step 6. Run Tests and Look at Things
====================================

1. Now run tests.  Everyone is happy!
2. Let's look at our form.
3. Let's look at our Fedora container.

