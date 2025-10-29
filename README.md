# Django Templates

 - They are basic HTML files which creates the basic web application interface. 
 - Follows the Model-View-Template workflow:
    - view contains the context to be rendered to html page, passed via templates.
    - template render data to html and return to browser
 - Steps tp follow
    - create a tempate HTML page
    - create a view.py with context to be rendered to html page
    - map the url of views in url.py     
 - Django templates use a simple syntax with two main constructs:
    - template variables 
     - syntax: {{ variables }}
     - description: they display values from context
     eg: {{ user.username }} 
    - template tags
     - syntax: {% tag %}
     - description: controls logic with loops, conditions etc.
     eg: {% if user.is_authentictated %} 