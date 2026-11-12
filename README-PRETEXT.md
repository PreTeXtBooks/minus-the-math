# Statistics Minus the Maths - PreTeXt Edition

This repository contains a PreTeXt version of "Statistics Minus the Maths" textbook.

## PreTeXt Structure

The book is organized in a standard PreTeXt structure:

- **project.ptx** - Main project configuration file (using PreTeXt version 2 format)
- **publication/** - Contains publication settings
  - **publication.ptx** - Publication configuration for HTML, LaTeX, and PDF output
- **source/** - Contains all source files for the book
  - **main.ptx** - Main book file that includes all chapters
  - **preface.ptx** - Preface content
  - **ch01-graphical-tools.ptx** - Chapter 1: Graphical Tools for Describing Variables
  - **ch02-describing-one-variable.ptx** - Chapter 2: Statistics for Describing One Variable at a Time
  - **ch03-relationship-two-quantitative.ptx** - Chapter 3: Tools for Describing the Relationship Between Two Quantitative Variables
  - **ch04-estimation.ptx** - Chapter 4: Estimation
  - **ch05-probability-distributions.ptx** - Chapter 5: Probability Distributions
  - **ch06-sampling-distributions.ptx** - Chapter 6: Sampling Distributions
  - **ch07-hypothesis-testing.ptx** - Chapter 7: Hypothesis Testing
  - **ch08-comparing-means.ptx** - Chapter 8: Comparing Means (How a Qualitative Variable Relates to a Quantitative One)
  - **ch09-comparing-groups.ptx** - Chapter 9: Comparing Groups (How Two Qualitative Variables Relate to One Another)
  - **ch10-causality-experimental-designs.ptx** - Chapter 10: Causality and Experimental Designs
  - **ch11-models-uncertainty.ptx** - Chapter 11: Models and Uncertainty
  - **ch12-regression-qual-independent.ptx** - Chapter 12: Regression with Qualitative Independent Variables
  - **ch13-regression-qual-dependent.ptx** - Chapter 13: Regression with Qualitative Dependent Variables
- **assets/** - External assets directory (`pretext/assets/`)
  - **Images/** - All images used in the book, referenced from the source as `Images/...`

## Building the Book

To build the book, you'll need to have PreTeXt installed. Visit [PreTeXt Guide](https://pretextbook.org/) for installation instructions.

### Prerequisites

1. Install PreTeXt CLI from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up PreTeXt cache (workaround for known bug in PreTeXt 2.32.0):
   ```bash
   bash .github/scripts/setup-pretext-cache.sh
   ```

### Build Commands

#### Build HTML version:
```bash
pretext build html
```

#### Build PDF version:
```bash
pretext build pdf
```

#### Build LaTeX version:
```bash
pretext build latex
```

#### View the HTML output:
```bash
pretext view html
```

## Output

Built files will be placed in the `output/` directory:
- `output/html/` - HTML version
- `output/pdf/` - PDF version
- `output/latex/` - LaTeX source files

## GitHub Pages Deployment

The book is automatically built and deployed to GitHub Pages whenever changes are pushed to the `main` branch. The workflow:

1. Installs PreTeXt CLI
2. Builds the HTML version of the book
3. Deploys the HTML output to GitHub Pages

You can also manually trigger the deployment from the Actions tab in the GitHub repository.

### Prerequisites for GitHub Pages

Ensure that GitHub Pages is enabled in your repository settings:
1. Go to Settings → Pages
2. Set Source to "GitHub Actions"
3. The workflow will automatically deploy on the next push to `main`

## About PreTeXt

PreTeXt is an authoring and publishing system for scholarly documents, with special support for textbooks. Learn more at [pretextbook.org](https://pretextbook.org/).
