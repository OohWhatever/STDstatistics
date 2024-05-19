README.md
apt install python3.11-venv
python -m venv venv 
. ./venv/bin/activate 
pip install Flask requests svgwrite
![asda](https://stdstatistics.onrender.com/generate-svg?username=whatever)

# ⚡ Project: Standoff365 cyberrange rating badge

Here is the dynamic SVG image that updates every hour by GitHub Actions with new timestamp and how to:

![Dynamic SVG Image](https://github.com/OohWhatever/OohWhatever/blob/main/img/data.svg?raw=true)

# Setup a personal README profile:
Create a repository with the same name as your GitHub login
<img width="761" alt="image" src="https://github.com/OohWhatever/STDstatistics/assets/41408448/98921f75-5e79-4719-bcab-0480e046b25a">

You need README.md to be displayed on your user profile:
<img width="1323" alt="image" src="https://github.com/OohWhatever/STDstatistics/assets/41408448/77fd53dd-e569-4fcc-ba25-41eb04cbaa47">

# Create a GitHub personal token
From the Developer settings of your account settings, select Personal access tokens to create a new token.
<img width="1220" alt="image" src="https://github.com/OohWhatever/STDstatistics/assets/41408448/f3fde1ff-23b2-498a-a605-fdf6371a0450">

#Put your GitHub personal token in repository secrets
Go to the Settings of your repository and to create a new secret and paste your freshly generated GitHub token there.
![image](https://github.com/OohWhatever/STDstatistics/assets/41408448/4188b39a-f5e7-4dd2-800e-ed840cbf6b2d)

Setup GitHub Action workflow
Create a new workflow from the Actions tab of repository and paste the following:

First - you need to create in your repository .github/workflows/state.yml file  and put this actions here:

name: Update README

on:
  schedule:
    - cron: '0 * * * *'  # Запускать workflow каждый час
  push:
    branches:
      - main  # Выполнение при каждом push на ветку main
  workflow_dispatch:  # Позволяет запускать workflow вручную

jobs:
  update-readme:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Fetch SVG from API
      run: |
        curl -o data.svg "https://stdstatistics.onrender.com/generate-svg?username=whatever"
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'
        mv data.svg img/data.svg
    - name: Display directory contents for debugging
      run: ls -R

    - name: Commit new SVG
      run: |
        git add img/data.svg
        git diff-index --quiet HEAD || git commit -m 'Update SVG image'
      env:
        GITHUB_TOKEN: ${{ secrets.README_WORKFLOW }}

    - name: Update README with new timestamp
      run: |
        TIMESTAMP=$(date +%s)
        sed -i.bak "s|!\[Dynamic SVG Image\](https://github.com/OohWhatever/OohWhatever/blob/main/img/data.svg?raw=true).*|![Dynamic SVG Image](https://github.com/OohWhatever/OohWhatever/blob/main/img/data.svg?raw=true&timestamp=${TIMESTAMP})|" README.md
        git add README.md
        git diff-index --quiet HEAD || git commit -m 'Update README with new SVG'
      env:
        GITHUB_TOKEN: ${{ secrets.README_WORKFLOW }}

    - name: Push changes
      env:
        GITHUB_TOKEN: ${{ secrets.README_WORKFLOW }}
      run: |
        git remote set-url origin https://x-access-token:${GITHUB_TOKEN}@github.com/${{ github.repository }}.git
        git push origin HEAD:main

this code will update your badge everu hour

# Create first img file

push to your repo emty data.svg file in /img folder




