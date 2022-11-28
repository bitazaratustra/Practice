## Objective

Create your first CD (Continuous Deployment)

Now that we have setup a CI on GitHub, our code will be automatically tested every time we push new commits to our GitHub repository.
Would not it be nice if once our code has passed all the tests we wrote, and only if it passes all the tests, it would be automatically deployed to production? 👉 This is what CD is about.

## Where to deploy ?

We want to be able to deploy a software/package on a remote machine living in the cloud.
Where to deploy? You have many different options, we chose Heroku for many reasons:
👉 It is free
👉 It is amazingly easy to use
👉 It has smooth git integration

## Heroku setup

- Sign in to [Heroku](https://signup.heroku.com/)
- Install the Heroku CLI (Command Line Interface):

<details>
  <summary markdown='span'><strong> macOS </strong></summary>

  ``` bash
  brew tap heroku/brew && brew install heroku
  ```

</details>
<details>
  <summary markdown='span'><strong> Ubuntu </strong></summary>

  ``` bash
  curl https://cli-assets.heroku.com/install.sh | sh
  ```

</details>
<details>
  <summary markdown='span'><strong> WSL2 </strong></summary>

  ``` bash
  curl https://cli-assets.heroku.com/install.sh | sh
  ```

</details>

- Login the CLI

```bash
heroku login
```

## Deploy your first package to Heroku

Deploying to Heroku is as simple as:
👉 Adding a `Procfile` file indicating the command to run on the Heroku servers in order to run your code
👉 Creating a Heroku app and running 3 commands from the command line

Here is how to do it:
- Go to the root of the repository you used in the last challenges
- Add a file named `Procfile` at the root of the repository
- Insert the following line inside of the `Procfile` (change the name of your package/script in the line) in order to run your script when the application is deployed

```bash
web: pip install . -U && YOUR_PACKAGE_NAME-run
```

- Upload the **public** SSH key created during the setup in order to authentify to **Heroku** using SSH

``` bash
heroku keys:add ~/.ssh/id_ed25519.pub
```

- Create your Heroku app (change the name of your package, the name of the app must be unique worldwide and don't use underscores - it will be a part of the URL)
```bash
heroku create --ssh-git YOUR-PACKAGE-NAME
```
- You should see in the console that Heroku deployed a web server online exposing for you an empty app that is visible here:
https://YOUR-PACKAGE-NAME.herokuapp.com/
- Now we will deploy our package to this server. **Do not forget to commit your code** before pushing to Heroku: only the commited code will be pushed to production!

```bash
git add Procfile
git commit -m 'Heroku Procfile added'
git status
```

- Push your code to Heroku
```bash
git push heroku master
```

- Deploy on a free Heroku dyno
```bash
heroku ps:scale web=1
```

- You should see in the server logs the result of the execution of the script of your package
```bash
heroku logs --tail
```

📣 And `voila` 📣
**NB: We only ran our script once on Heroku. Once the script finished running, Heroku considered that our app had unexpectedly terminated and decided to shutdown the service.
==> You should see the corresponding crash message in the Heroku logs**

👉 Do not worry, we will see by the end of the module how to deploy to Heroku something that does not crash right away 😉

## Automate the deployment inside of your GitHub CI-CD

Running the previous commands was boring, right?
You would rather have your package automatically deployed every time you change your code and push it to GitHub!

Here we will get back to our precious `.github/workflows` GitHub configuration...
👉 Simply add or uncomment the step called `deploy_heroku` which is following the `build` step. Do not forget to change the name of the Heroku app that you created in the code:
```yaml
  deploy_heroku:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - uses: akhileshns/heroku-deploy@v3.0.4 # This is the action
      with:
        heroku_api_key: ${{secrets.HEROKU_API_KEY}}
        heroku_app_name: "REPLACE_WITH_YOUR_HEROKU_APP_NAME" # Must be unique in Heroku
        heroku_email: ${{secrets.HEROKU_EMAIL}}
```

You may verify that the syntax of the uncommented YAML remains correct using a [YAML validation tool](https://codebeautify.org/yaml-validator).

Then add your email address and your Heroku API key in the Secrets of your project repository on Github (follow the steps below).

This CD configuration will do nothing more than execute the commands that you manually executed in the previous section. The only difference is that these commands will be executed automatically from the **Github servers** whenever the code that you push to your GitHub repository passes all the steps defined in the CI:
```bash
git push heroku master
heroku ps:scale web=1
```

💡 How will GitHub authenticate itself as myself on Heroku in order to be allowed to push my code to production ?

In order to allow GitHub to do that, we will configure in GitHub a Heroku API key that we will generate on Heroku and our email address.

**HEROKU API KEY**

👉 Go to your [Heroku account](https://dashboard.heroku.com/account) and generate or copy (Reveal) your API key.

👉 Store it as a Secret on your GitHub repository under `Settings` then `Secrets`
   => name it `HEROKU_API_KEY` and paste the API key that you copied from Heroku

**HEROKU EMAIL**

👉 Store it as a Secret on your GitHub repository under `Settings` then `Secrets`
   => name it `HEROKU_EMAIL` and save the email that you are using in order to login on Heroku

👉 Then from the Terminal, inside of your project, update your code, push it to GitHub and see the CI/CD do its work:
- Verify the status of your git repository
```bash
git status
```

- Look at the differences in the GitHub CI/CD configuration
```bash
git diff
```

- Add a `Procfile` file and commit the changes to `.github/workflows/pythonpackage.yml`
```bash
git add Procfile
git commit -am "added CD to deploy to Heroku"
```

- Finally
```bash
git push origin master
```

📣 Sit back, relax, grab a drink and chill as GitHub is doing all the work for you in the `Actions` tab 📣
