Python Mediawiki API
====================

A very simple and direct wrapper around the Mediawiki API

Introduction
------------

This library provides a very simple convenience wrapper around the `Mediawiki API <http://www.mediawiki.org/wiki/API>`_. It is meant to closely mirror the interface provided by `mw.Api <http://www.mediawiki.org/wiki/ResourceLoader/Default_modules#mediaWiki.Api>`_
 
Features
--------

The library allows you to call Mediawiki APIs without having to deal without dealing with network calls. It also has authentication support and a few convenience methods. 

Non Features
------------

This is the anti-`mwclient <http://sourceforge.net/projects/mwclient/>`_. It does not add another layer for you to understand over the well `documented <http://en.wikipedia.org/w/api.php>`_ Mediawiki API, and it never will :)

Documentation
-------------
    MWApi
    
    class MWApi
     |  Class representing a single API Session, with a single authenticated user.
     |  
     |  Useful Attributes:
     |  tokens              - Contains an edittoken & watchtoken (if populateTokens() has been called)
     |  is_authenticated    - Boolean indicating if the MWApi is sending authenticated requests
     |  
     |  Methods defined here:
     |  
     |  __init__(self, host, api_path='/w/api.php')
     |      Create a MWApi instance
     |      
     |      Arguments:
     |      host        - Host to which to connect to. Must include http:// or https:// and no trailing slash
     |      api_path    - Url to api.php on the host. Must start with /
     |  
     |  get(self, **params)
     |      Makes an API request with the GET method
     |      
     |      Arguments:
     |      params - Parameters to send to the API. Varies depending on the action to be performed.
     |  
     |  login(self, username, password)
     |      Authenticates with the given credentials and logs in the user for the session. 
     |      All further requests sent from this MWApi object will be signed as said user.
     |      
     |      Arguments:
     |      username - The username of the user to be authenticated
     |      password - The password of the user to be authenticated
     |      
     |      Throws:
     |      Throws an exception with (Message, Response) if Authentication fails
     |      
     |      Note: 
     |      Passwords are sent as plaintext. This is a limitation of the Mediawiki API.
     |      Use a https host if you want your password to be secure
     |  
     |  populateTokens(self)
     |      Populates the `tokens` attribute of the object with `edittoken` and `watchtoken`.
     |      Requires that authentication has been performed already with `login()`
     |  
     |  post(self, **params)
     |      Makes an API request with the POST method
     |      
     |      Arguments:
     |      params - Parameters to send to the API. Varies depending on the action to be performed.
     |  
     |  _request(self, method, params)
     |      Makes a request to the API and returns a dictionary containing the results
     |      
     |      Arguments:
     |      method - GET or POST, depending on which API is being called
     |      params - Parameters to send to the API. Varies depending on the action to be performed.
     |  


Contact
-------

Support requests and flames can be sent to me via several means.

Email: yuvipanda@gmail.com. Twitter: @yuvipanda. IRC: yuvipanda on FreeNode

You can file bugs `on Github <https://github.com/yuvipanda/python-mwapi/issues>`_.
