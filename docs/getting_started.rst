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

.. code-block:: python

   import anapioficeandfire

   api = anapioficeandfire.API()

   jon_snow = api.get_character(id=583)
   for title in jon_snow.aliases:
       print(title)
