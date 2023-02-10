gh repo create git-setup-scripts --private
echo "# git-setup-scripts" >> README.md 
git init
git add --all :/
git add --force
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ruodeee/git-setup-scripts.git
git push -u origin main