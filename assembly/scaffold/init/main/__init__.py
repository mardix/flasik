# -*- coding: utf-8 -*-
"""
Assembly views

This is the views file. Create all of your view classes in here

## Example

class Index(Assembly):

    # path: /
    # It will match the template at /templates/Index/index.html
    def index(self):
        return "Hello world"

    # path: /about-us
    # It will match the template at /templates/Index/about_us.html
    def about_us(self):
        return 

class Blog(Assembly):

    # path: /blog/
    # It will match the template at /templates/Blog/index.html
    def index(self):
        return "Hello world"

    # path: /blog/posts
    # It will match the template at /templates/Blog/posts.html
    def posts(self):
        return   

class API(Assembly):

    # path: /api/
    # It will return a json

    @response.json    
    def index(self):
        return {
            "name": "Assembly",
            "version": "x.y.z"
        }

    # path: /api/items
    # It will return a json

    @response.json    
    def items(self):
        return {
            "data": {
                "items": [1, 2, 3]
            }
        }

"""

from assembly import (Assembly,
                      asm,
                      date,
                      models,
                      request,
                      response,
                      HTTPError)

# ------------------------------------------------------------------------------


class Index(Assembly):

    def index(self):
        print("we are here in index route")
        return

    @request.cors
    @response.json
    def api(self):
        """API Endpoint with CORS and JSON response
    This is using docstrings for specifications.
    ---
    definitions:
      Endpoint:
        type: object
        properties:
          date:
            type: date
          description:
            type: string
        items:
        $ref: '#/definitions/Endpoint'
    responses:
      200:
        description: API Endpoint with CORS and JSON response
        schema:
          $ref: '#/definitions/Endpoint'
        examples:
          response: {
              "date": "2019-11-29T18:28:07.125075+00:00",
              "description": "API Endpoint with CORS and JSON response"
          }
    """
        return {
            "date": date.utcnow(),
            "description": "API Endpoint with CORS and JSON response"
        }

    @response.json
    @response.cache(timeout=10)
    def cached(self):
        return {
            "description": "This is a cached endpoint",
            "date": date.utcnow(),
        }


    def error(self):
        """
        Accessing /error should trigger the error handlers below
        """
        raise HTTPError.NotFound()

# ------------------------------------------------------------------------------


class Error(Assembly):
    """
    This View handles errors
    """

    def _error_handler(self, e):
        """
        * special method
        Error handler method to catch all HTTP Error
        It's template must be the same name without the leading _, ie 'error_handler.html'
        """
        return {
            "code": e.code,
            "e": e
        }

    def _error_404(self, e):
        """
        * special method
        Error handler for 404
        It's template must be the same name without the leading _, ie 'error_404.html'
        """
        return {
            "code": e.code,
            "e": e
        }
