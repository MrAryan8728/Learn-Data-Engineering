"""
Task 3:
Create this function:

def create_pipeline_config(**kwargs):

Call it like:

config = create_pipeline_config(
    source="API",
    target="Snowflake",    
    load_type="incremental",    
    batch_size=1000
)


The function should:
1. Accept any number of keyword arguments.
2. Add one additional key:status: "active"
3. Return the resulting dictionary.
4. Print the returned configuration outside the function.
Expected result:
{
    "source": "API",
    "target": "Snowflake",    
    "load_type": "incremental",    
    "batch_size": 1000,    
    "status": "active"
}
"""

def create_pipeline_config(**kwargs):
    kwargs["status"] = "active"
    return kwargs

response = create_pipeline_config(source="API",
    target="Snowflake",
    load_type="incremental",
    batch_size=1000)
print(response)