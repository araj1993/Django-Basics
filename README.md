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

# Django Template Inheritance
 
 - commonly used templates (footer, header, navbar) can be kept as a base template and inherited to child templates, using {% extends %} tag.
 - inside the base template the {% block title %} and {% block content %} tags define replaceable sections in child template. 
 - Each section defined inside {% block <name> %} will replace the name tag from child templates
 - {% extends "base.html" %} tells Django this template is a child of base.html

 ### To include logo images, CSS, JavaScript saved inside the /static/ folder inside the base.html file, it can be done in 2 ways:
  1. To inherite logo images, css used in base template to children, then children template should start with {% load static %} 
  2. Create separate html file for each section(eg: header.html, navbar.html, footer.html) inside the /template/ folder and cut&paste each section from base.html to proper html files. Then used the {% include 'template_name.html' %} inside the base template from where the section are removed. 
  3. The logo path inside each newly created template html pages, replace the path of images using the {% static /path/to/image/ %} template variable. 
