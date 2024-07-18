---
title: "SIH Quarto Training template"
---
# Read me

- We recommend storing all notebooks (.ipynb) or R files (as .qmd or .rmd) in the `notebooks` folder.

## How to use this repository

- Clone this repository and `ParallelPython`.
- Edit `index.qmd` to change the main landing page.
- Edit or create `setup.qmd` to change the Setup instruction pages.
- Edit `_quarto.yml` to change the dropdown menu options.
- Add additional `*.md` files to the root dir to have them converted to html files (and add them to `_quarto.yml` to make them navigable).

- Download [Quarto](https://quarto.org/. VSCode also has an extension [Quarto Extension](https://quarto.org/docs/tools/vscode.html) to render the training. 

- On the command line after Quarto is installed, type `quarto render`. Afterwhich, `open -a "firefox" docs/index.html` can be run to view the rendered training.


## Note:

- If using Python, you will need to have Jupyter and Quarto installed to convert the notebooks and render them for the web.
- If using R, you will need rmarkdown, xml2 and X to have the notebooks generate properly and link out to the documentation, as specified in the `_quarto.yml` file.
- The building from Jupyter notebooks will NOT re-render all of the notebooks unless you use the `quarto render notebook.ipynb --execute` command
- Building from R will by default re-render all of the outputs


```
quarto render
#First time you create the file, add them to be tracked by github, e.g.
git add docs/*
git commit -am "your comments"
git push
```

You can browse the result locally by exploring the html files created (note: sometimes figures display locally but not on web and the other way around too.)
