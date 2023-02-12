gh repo create git-setup-scripts --private
echo "# git-setup-scripts" >> README.md 
git init
git add --all :/
git commit -m "first commit"
git branch -M main
git remote remove origingit remote add origin https://github.com/ruodeee/git-setup-scripts.git
