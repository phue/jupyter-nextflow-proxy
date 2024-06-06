# jupyter-nextflow-proxy

Spawn nextflow pipelines from Jupyter and monitor them.

:warning: This will only work if the pipeline implements a process that responds to http requests on a configurable port.

For instance, a shiny app:

```groovy
process SHINY {
    tag "localhost:${params.PORT}"

    input:
        env(SHINY_APP_DATA)

    script:
        """
        shiny run --port=${params.PORT} app.py
        """
}
```