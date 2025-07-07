# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "openai==1.93.0",
#     "pandas==2.3.0",
#     "polars==1.31.0",
# ]
# ///

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    #Este archivo esta generado con el argumento '--sandbox' y ya incluye una serie de paquetes y configuraciones prefijadas. 
    ### Mi objetivo era que me hiciese un docker seguro como ponia en la documentacion pero creo que no ha funcionado.
    """
    )
    return


@app.cell
def _(mo):
    import polars as pl

    # Crear un DataFrame con datos de alumnos y sus notas
    data = {
        'Alumno': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
        'Nota': [85, 90, 78, 92, 88]
    }
    notas_df = pl.DataFrame(data)

    # Mostrar la tabla interactiva
    mo.ui.table(notas_df)
    return


if __name__ == "__main__":
    app.run()
