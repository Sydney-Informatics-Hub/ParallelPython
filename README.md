---
title: "SIH Quarto Training template"
---
# Read me

- We recommend storing all notebooks (.ipynb) or R files (as .qmd or .rmd) in the `notebooks` folder.

## How to use

- Copy this repository
- Edit `index.qmd` to change the main landing page.
- Edit or create `setup.qmd` to change the Setup instruction pages.
- Edit `_quarto.yml` to change the dropdown menu options.
- Add additional `*.md` files to the root dir to have them converted to html files (and add them to `_quarto.yml` to make them navigable).

- If using Python, use VSCode's [Quarto Extension](https://quarto.org/docs/tools/vscode.html) to render the project (recommended b/c it's easier/nice)
- If using R, type `quarto render` in the Terminal in RStudio (not the R command line, the Terminal tab!) - or use the buttons
- If you want to command line, run the below commands (after activating the correct Python environment, if needed) 

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
