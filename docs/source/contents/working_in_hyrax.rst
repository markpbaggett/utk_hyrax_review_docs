Working in Hyrax
================

Adding a New Metadata Field with Integration Tests and Unit Tests with Capybara
-------------------------------------------------------------------------------

Hyrax uses `Capybara <https://teamcapybara.github.io/capybara/>`_ to automate integration tests and unit tests for the
entire application. This section exists to help me remember how to:

1. Create a new metadata field in a Work
2. Create the associated integration tests
3. Create the associated unit tests

The Hyrax Work Generator creates a default feature test for each work type you create. For example, if you created
a work type called `Image` like so:

.. code-block:: sh

    bundle exec rails generate hyrax:work Image

you'd generate a feature test in a file named `spec/features/create_image_spec.rb` like:

.. code-block:: ruby
    :linenos:

    scenario do
      visit '/dashboard'
      click_link "Works"
      click_link "Add new work"

      # If you generate more than one work uncomment these lines
      # choose "payload_concern", option: "Image"
      # click_button "Create work"

      expect(page).to have_content "Add New Image"
      click_link "Files" # switch tab
      expect(page).to have_content "Add files"
      expect(page).to have_content "Add folder"
      within('span#addfiles') do
        attach_file("files[]", "#{Hyrax::Engine.root}/spec/fixtures/image.jp2", visible: false)
        attach_file("files[]", "#{Hyrax::Engine.root}/spec/fixtures/jp2_fits.xml", visible: false)
      end
      click_link "Descriptions" # switch tab
      fill_in('Title', with: 'My Test Work')
      fill_in('Creator', with: 'Doe, Jane')
      fill_in('Keyword', with: 'testing')
      select('In Copyright', from: 'Rights statement')

      # With selenium and the chrome driver, focus remains on the
      # select box. Click outside the box so the next line can't find
      # its element
      find('body').click
      choose('image_visibility_open')
      expect(page).to have_content('Please note, making something visible to the world (i.e. marking this as Public) may be viewed as publishing which could impact your ability to')
      check('agreement')

      click_on('Save')
      expect(page).to have_content('My Test Work')
      expect(page).to have_content "Your files are being processed by Hyrax in the background."
    end

The feature test runs directly in browser.

You can run the entire test suite like so:

.. code-block:: sh

    rspec spec

You can run just this test like this:

.. code-block:: sh

    rspec spec/features/create_image_spec.rb

In order to add a new metadata field, there are several steps we should follow:

1. Add the new field to our feature spec.
2. Add a unit test for our new metadata field to our model.
3. Add the new metadata field and its predicate to our model.
4. Add test to our form.
5. Add field to our form.
6. Run tests.

In my example, let's add to an Image work year from http://www.europeana.eu/schemas/edm/year (RDF::Vocab::EDM.year).

===========================================================
1. Add the New Field to our Feature Spec / Integration Test
===========================================================

For starters, we need to add to our existing feature test a definition of how we expect our new field to work in Hyrax.
To do this, edit our test scenario at `spec/features/create_image_spec.rb` by adding the following after the
copyright selection test:

.. code-block:: ruby

    click_link("Additional fields")
    fill_in "Year", with: "2005"

If you run `rspec`, it will fail because we haven't updated our model.

==========================================================
2. Add a Unit Test for our New Metadata Field to our Model
==========================================================

Before we update our model, let's add a unit test for our model update in `spec/models/image_spec.rb`. Inside of
the Rspec.describe block, add this:

.. code-block:: ruby

      describe "#year" do
        context "with a new Image" do
          it "has no year value when it is first created" do
            image = Image.new
            expect(image.year).to be_empty
          end
        end

        context "with an Image that has a year defined" do
          it "can set and retrieve a year value" do
            image = Image.new
            image.year = ["2005"]
            expect(image.year).to eq(["2005"])
          end
        end
      end

If you run tests now, you'll have even more fails! Let's Fix it.

===================================================
3. Add the New Field and its Predicate to our Model
===================================================

Edit `app/models/image.rb` and add the following before `include ::Hyrax::BasicMetadata`:

.. code-block:: ruby

    property :year, predicate: "http://www.europeana.eu/schemas/edm/year"

This updates our model. Running rspec now will result in passing unit tests but failing integration tests.

===============================
4. Add a Unit Test for our Form
===============================

As always, start by adding your unit test to the form by modifying `spec/forms/hyrax/image_form_spec.rb`. Replace or
add to  the parts inside the Rspec.describe block with:

.. code-block:: ruby

      subject { form }
      let(:image)    { Image.new }
      let(:ability) { Ability.new(nil) }
      let(:request) { nil }
      let(:form)    { described_class.new(image, ability, request) }
      it "has the expected terms" do
        expect(form.terms).to include(:title)
        expect(form.terms).to include(:year)
      end

========================
5. Add Field to our Form
========================

Rspec will still fail until will modify `app/forms/hyrax/image_form.rb` by adding this line:

.. code-block:: ruby

    self.terms += [:year]

============
6. Run Tests
============

Now run tests.  Everyone is happy!