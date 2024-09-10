{% macro custom_schema_name() %}
    {% set branch = get_git_branch() %}
    
    {%- if branch == 'main' or branch == 'master' -%}
        {{ return('vne_production') }}
    {%- elif branch == 'dev_steve' -%}
        {{ return('dev_steve') }}
    {%- else -%}
        {{ return('public') }}  {# Append branch name to the schema for safety #}
    {%- endif -%}
{% endmacro %}