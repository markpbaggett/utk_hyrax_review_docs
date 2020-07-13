VII. CAS Authentication
=======================

As the Samvera docs state, there are many ways to do this.

This method uses a gem called `devise CAS authenticatable <https://samvera.github.io/devise_cas_authenticatable>`_.

Add this line to your Gemfile:

.. code-block:: ruby

    gem 'devise_cas_authenticatable'

Now run `bundle install`.

Now, modify the user model at `app/models/user.rb`. Find this line:

.. code-block:: ruby

    attr_accessible :email, :password, :password_confirmation #default line from the basic hyrax installation

Replace it with:

.. code-block:: ruby

    attr_accessible :email

Next, find these lines:

.. code-block:: ruby

    devise :database_authenticatable, :registerable,
        :recoverable, :rememberable, :trackable, :validatable

Replace them with this:

.. code-block:: ruby

    devise :cas_authenticatable,
     :recoverable, :rememberable, :trackable

Now add a function that takes the extra attributes from CAS server and maps them to fields in the Hyrax contributor profile.
In this example, we will get the department name and email address.

.. code-block:: ruby

    def cas_extra_attributes=(extra_attributes)
    extra_attributes.each do |name, value|
    case name.to_sym
    when :department
    self.department = value
    when :email
    self.email = value
    end
    end
    end

Now, modify the devise initializer. Go to `config/initializers/devise.rb` and add the following lines:

.. code-block:: ruby

    config.cas_base_url = '[YOUR CAS URL GOES HERE]'
    config.cas_user_identifier = 'email'
    config.cas_username_column = 'email'

Create a migration like this:

.. code-block:: ruby

    class AddUsernameToUsers < ActiveRecord::Migration[5.1]
      def change
        add_column :users, :username, :string
      end
    end

Run `rails db migrate`.
