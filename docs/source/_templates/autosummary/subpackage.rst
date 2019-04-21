{{ fullname }} (*subpackage*)
{{ underline }}===============

.. automodule:: {{ fullname }}
    :members:
    :private-members:
    :show-inheritance:
    :inherited-members:
    :member-order: bysource

    {% block members %}
    {% if members %}
    .. rubric:: Subpackage Members

    .. autosummary::
    {% for item in members %}
        {% if "__" not in item and "_" not in item|first  %}
            {% if "test" not in item %}
                ~{{ item }}
           {% endif %}
        {% endif %}
    {%- endfor %}
    {% for item in members %}
        {% if "__" not in item and "_" in item|first  %}
            {% if "test" not in item %}
                ~{{ item }}
           {% endif %}
        {% endif %}
    {%- endfor %}
    {% endif %}
    {% endblock %}

