# CI Workflow Documentation

This document explains the GitHub Actions CI workflow defined in `.github/workflows/ci.yaml`.

## Workflow Overview

The CI workflow automatically tests the application on every push or pull request to the main branch.

## Workflow Configuration

### Workflow Name
```yaml
name: CI Workflow
```

### Triggers

The workflow runs on:

**Push Events:**
```yaml
push:
  branches:
    - main
```
- Triggers when code is pushed directly to the `main` branch

**Pull Request Events:**
```yaml
pull_request:
  branches:
    - main
```
- Triggers when a pull request targets the `main` branch

## Jobs

### Test Job

**Runner Environment:**
```yaml
runs-on: ubuntu-latest
```
- Runs on the latest Ubuntu Linux environment provided by GitHub

### Workflow Steps

#### Step 1: Checkout Code
```yaml
- name: Checkout code
  uses: actions/checkout@v2
```
- **Purpose**: Retrieves the repository code
- **Action**: `actions/checkout@v2`
- **What it does**: Clones the repository to the runner environment

#### Step 2: Set up Python
```yaml
- name: Set up Python
  uses: actions/setup-python@v2
  with:
    python-version: '3.9'
```
- **Purpose**: Configures Python environment
- **Action**: `actions/setup-python@v2`
- **Python Version**: 3.9
- **What it does**: Installs Python 3.9 and makes it available for subsequent steps

#### Step 3: Install Dependencies
```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install pytest streamlit
```
- **Purpose**: Installs required Python packages
- **Commands**:
  - `python -m pip install --upgrade pip` - Updates pip to the latest version
  - `pip install pytest streamlit` - Installs pytest (testing framework) and streamlit (app framework)

#### Step 4: Run Tests
```yaml
- name: Run tests
  run: |
    pytest _test.py
```
- **Purpose**: Executes the test suite
- **Command**: `pytest _test.py`
- **What it does**: Runs all tests in the `_test.py` file
- **Result**: Workflow fails if any test fails, passes if all tests pass

## How to View CI Results

1. Navigate to your GitHub repository
2. Click on the **Actions** tab
3. Select a workflow run from the list
4. Click on the **test** job to see detailed logs
5. Expand each step to view its output

## CI Status Badge

Add this badge to your README to display the workflow status:

```markdown
![CI Workflow](https://github.com/taanjit/YT-MLOPS-CI/workflows/CI%20Workflow/badge.svg)
```

## Workflow Execution Flow

```
Trigger (Push/PR to main)
    ↓
Checkout code from repository
    ↓
Set up Python 3.9 environment
    ↓
Install pip, pytest, and streamlit
    ↓
Run pytest on _test.py
    ↓
Report Success ✅ or Failure ❌
```

## Requirements for CI to Pass

- The `_test.py` file must exist in the repository root
- All tests in `_test.py` must pass
- The code must be compatible with Python 3.9
- Streamlit must be importable (if used in tests)

## Troubleshooting CI Failures

**If tests fail:**
- Check the Actions tab for detailed error logs
- Run `pytest _test.py` locally to reproduce the issue
- Fix failing tests and push the changes

**If dependencies fail to install:**
- Verify package names are correct
- Check for version conflicts
- Ensure pip is compatible with Python 3.9

**If Python setup fails:**
- Verify the `python-version` is specified correctly
- Check GitHub Actions status page for service issues
