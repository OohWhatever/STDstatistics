
# ⚡ Project: Standoff365 cyberrange rating badge

Here is the dynamic SVG image that updates every hour and how to install MANUAL:




>⚠️ Images are cached for 1 hour after being rendered. They won't be updated during this time window when queried again. However it is possible to manually update them by using Github Actions again

## Setup a personal README profile with Github Actions (10 mins):

Create a repository with the same name as your GitHub login

<img width="761" alt="image" src="https://github.com/OohWhatever/STDstatistics/assets/41408448/98921f75-5e79-4719-bcab-0480e046b25a">


You need README.md to be displayed on your user profile:


<img width="1323" alt="image" src="https://github.com/OohWhatever/STDstatistics/assets/41408448/77fd53dd-e569-4fcc-ba25-41eb04cbaa47">

## Insert markdown image link

`![Dynamic SVG Image](https://github.com/{Your-GitHub-login}/{Your-GitHub-login}/blob/main/img/data.svg?raw=true)`

> here you need to change ` {Your-GitHub-login} ` to your actual login

## Create a GitHub personal token

From the Developer settings of your account settings, select Personal access tokens to create a new token.

<img width="1220" alt="image" src="https://github.com/OohWhatever/STDstatistics/assets/41408448/f3fde1ff-23b2-498a-a605-fdf6371a0450">

## Put your GitHub personal token in repository secrets

Go to the Settings of your repository and to create a new secret and paste your freshly generated GitHub token there.

![image](https://github.com/OohWhatever/STDstatistics/assets/41408448/4188b39a-f5e7-4dd2-800e-ed840cbf6b2d)

## Setup GitHub Action workflow

Create a new workflow file from the Actions tab of repository and paste the following:

First - you need to create in your repository `.github/workflows/state.yml` file  and put this actions there:
```
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
        git pull
        curl -o data.svg "https://stdstatistics.onrender.com/generate-svg?username={your_standoff365_login}"    # бейджик с основной статистикой киберполигона
        curl -o bbdata.svg "https://stdstatistics.onrender.com/generatebb-svg?username={your_standoff365_login}"     # бейджик с багбаунти статистикой 
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'
      
        mv data.svg img/data.svg
        mv bbdata.svg img/bbdata.svg
    - name: Display directory contents for debugging
      run: ls -R

    - name: Commit new SVG
      run: |
        git add img/data.svg
        git add img/bbdata.svg
        git diff-index --quiet HEAD || git commit -m 'Update SVG image'
      env:
        GITHUB_TOKEN: ${{ secrets.README_WORKFLOW }} # сюда вставлять токен

    - name: Update README with new timestamp
      run: |
        TIMESTAMP=$(date +%s)
        sed -i.bak "s|!\[Dynamic SVG Image\](https://github.com/{your-github-login}/{your-github-login}/blob/main/img/data.svg?raw=true).*|![Dynamic SVG Image](https://github.com/OohWhatever/OohWhatever/blob/main/img/data.svg?raw=true&timestamp=${TIMESTAMP})|" README.md       # основной бейджик со статистикой киберполигона
        sed -i.bak "s|!\[Dynamic BBSVG Image\](https://github.com/{your-github-login}/{your-github-login}/blob/main/img/bbdata.svg?raw=true).*|![Dynamic BBSVG Image](https://github.com/OohWhatever/OohWhatever/blob/main/img/bbdata.svg?raw=true&timestamp=${TIMESTAMP})|" README.md      # бейджик с багбаунти статистикой киберполигона
        git add README.md
        git diff-index --quiet HEAD || git commit -m 'Update README with new SVG'
      env:
        GITHUB_TOKEN: ${{ secrets.README_WORKFLOW }} # сюда вставлять токен

    - name: Push changes
      env:
        GITHUB_TOKEN: ${{ secrets.README_WORKFLOW }} # сюда вставлять токен
      run: |
        git remote set-url origin https://x-access-token:${GITHUB_TOKEN}@github.com/${{ github.repository }}.git
        git push origin HEAD:main

```

This code will update your badge everu hour

>Here you need to change soime parameters like {Your-GitHub-login} to your login, { secrets.README_WORKFLOW } to name of your github secret and {Standoff365-login} to your actual login
## Create first img file

Push to your repo emty data.svg or bbdata.svg file in `/img` folder or you can download it from `https://stdstatistics.onrender.com/`

![image](https://github.com/OohWhatever/STDstatistics/assets/41408448/bc51fc78-261e-4bcf-92b4-2abd1cc55af5)

## PROFIT

## To do:
- [x] Badge for BugBouny statistics
- [ ] Some design changes
- [x] More information in badges
- [ ] Standoff profile medals



