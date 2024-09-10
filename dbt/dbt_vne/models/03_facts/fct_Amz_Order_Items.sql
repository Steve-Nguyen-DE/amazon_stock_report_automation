
{{
    config(
        materialized='incremental'
    )
}}

SELECT 
    *
FROM 
    {{ ref('stg_Amz_Order_Items') }}

{% if is_incremental() %}

  -- this filter will only be applied on an incremental run
  -- (uses >= to include records whose timestamp occurred since the last run of this model)
  -- (If event_time is NULL or the table is truncated, the condition will always be true and load all records)
where last_update_time_stamp >= (select coalesce(max(last_update_time_stamp),'1900-01-01') from {{ this }} )

{% endif %}
