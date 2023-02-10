gh repo create git-setup-scripts --private
echo "# git-setup-scripts" >> README.md
git init
git add . && git commit -m "initial commit"
git branch -M test
git remote add origin https://github.com/ruodeee/git-setup-scripts.git
git push -u origin test
pause