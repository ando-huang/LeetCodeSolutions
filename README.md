# LeetCodeSolutions

### Instructions

#### First Time Setup

Note: `$` represents a line that should be run in the terminal

1. Ask @ando-huang to be added as a collaborator to the repository
2. Clone the repository (top right) into a local directory 
    `$ git clone git@github.com:ando-huang/LeetCodeSolutions.git`
3. Change Directories `$ cd` into the cloned repository
4. Create a new branch for your solution
    `$ git checkout -b <YourName>TwoSum`
5. Check which branch you're currently on
    `$ git branch`
6. If you're on the branch you just created, great! If not, run this command
    `$ git checkout <YourName>TwoSum`
7. Make your changes, place your solution file in a folder named after the
   problem, and push your changes to your branch. There should be no conflicts. 
8. Navigate to the github page for the repo, go to the tab "Pull Requests" and
   open a pull request for your change. Request everyone as a reviewer so that
we're aware of your changes. 
9. Once the request is approved, you can merge your change into the `main`
   branch. 
Now you can delete the branch you created, because all of it's data is in main. 
10. In your terminal, switch to branch main, run `$ git pull origin main` to grab changes
    from the upstream, and run `$ git branch -d AndrewHuangTwoSum` to delete
the branch from your local .git file. Now it will not show up when you run
`$ git branch` and you will not be able to switch to it as an existing branch. 
11. In the future, before creating a new branch, it is best to run `$ git pull
    origin main` while on the main branch, to get the most recent code on main
and then work off of that. 
