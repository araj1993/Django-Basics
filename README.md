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

# Django Variable and Tags

### Templates variable 
 - They are special variables used by the views.py file to render dynamic data to the template html page.
 - Basically placeholder for data passed from views
 - They are written in double culry braces {{}}. When html pages are rendered they replaces it with actual values from view.
   - eg : {{ user.username }}

### Template tags
 - Tags help to add logic or structures - loops, conditions, includes
 - written with {%...%}
   - eg: {% for item in items%}
            ....
         {% endfor %}   
