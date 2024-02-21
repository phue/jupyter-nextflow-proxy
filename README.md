# jupyter-nextflow-proxy

Spawn nextflow pipelines from Jupyter and monitor them.

:warning: This will only work if the pipeline implements a process that responds to http requests on a configurable port.

For instance, a shiny app:

```groovy
process COMMS {
    tag "localhost:${params.COMMS.port}"

    when:
        params.COMMS.enabled

    input:
        env(SHINY_APP_DATA)

    script:
        """
        shiny run --port=${params.COMMS.port} app.py
        """
}
```