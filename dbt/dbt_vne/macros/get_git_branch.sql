{% macro get_git_branch() %}
    {# Use Python's GitPython if available, otherwise fallback to command-line git #}
    {% set branch = run_query("SELECT pg_backend_pid();") %}  {# Dummy query to force template compilation #}
    {% if not env_var('GIT_BRANCH') %}
        {% set branch = env_var('GIT_BRANCH') %}
    {% else %}
        {% set branch = return(execute('git rev-parse --abbrev-ref HEAD').stdout.strip()) %}
    {% endif %}
    {{ return(branch) }}
{% endmacro %}
