gh repo create git-setup-scripts --private
git init
git add --all :/
git commit -m "first commit"
git branch -M main
git remote remove origin
git remote add origin https://github.com/ruodeee/git-setup-scripts.git
git push -u origin main