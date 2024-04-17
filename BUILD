python_sources(name="root")

python_requirement(name="sqlalchemy", requirements=["sqlalchemy"])

python_requirement(name="greenlet", requirements=["greenlet"])

pex_binary(
    name="main",
    entry_point="app.py",
    complete_platforms=[":platforms"],
)

python_google_cloud_function(
    name="cloud_function",
    # runtime="python38",
    complete_platforms=[":platforms"],
    handler="app.py:handler",
    type="http",
)

file(name="platforms", source="platforms.json")
