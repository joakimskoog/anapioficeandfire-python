.. _getting_started:


***************
Getting started
***************

Introduction
============

This is the place for people that are new to anapioficeandfire. This tutorial will help you to get started with anapioficeandfire. Note that we won't go too much
into detail, just the most important basic functionality.

Installation
============

At the command line::

    $ pip install anapioficeandfire

First example
============

.. code-block :: python

   import anapioficeandfire

   api = anapioficeandfire.API()

   jon_snow = api.get_character(id=583)
   for title in jon_snow.aliases:
       print(title)

This example will download all data about the character Jon Snow and print each one of his aliases to the console.

API
============

The API class provides access to the entire An API of Ice And Fire in a clean and "pythonic" way. Each method accepts various parameters and return responses. For detailed information about the methods, please refer to :ref:`API Reference <api_reference>`.

Models
============

When an API method is invoked the response will be an apioficeandfire model class instance. The model will contain the data returned from An API of Ice And Fire which you can then use inside your applications. For example, the following code returns a :class:`Book` model::

   # Get a Book object form An API of Ice And Fire
   game_of_thrones = api.get_book(id=1)
   
For detailed information about the models, please refer to :ref:`Models Reference <models_reference>`. 



