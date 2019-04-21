{{ fullname }} (*module*)
{{ underline }}===========



.. automodule:: {{ fullname }}
    :members:
    :private-members:
    :undoc-members:
    :show-inheritance:
    :inherited-members:
    :member-order: bysource
    
    {% block classes %}
    {% if classes %}
    .. rubric:: Classes

    .. autosummary::
    {% for item in classes %}
      ~{{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block functions %}
    {% if functions %}
    .. rubric:: Functions

    .. autosummary::
    {% for item in functions %}
      ~{{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}

    {% block attributes %}
    {% if attributes %}
    .. rubric:: Attributes

    .. autosummary::
    {% for item in attributes %}
      ~{{ item }}
    {%- endfor %}
    {% endif %}
    {% endblock %}
