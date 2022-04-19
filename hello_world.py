echo "print(“Hello World”)" > hello_world.py
git add hello_world.py
git commit -m "Add Hello World"
git push origin dev
git log
git checkout main
git merge dev
git push
git checkout dev
echo "print("Hello World2")" >> hello_world.py
git add .
git commit -m "Add Hello World2"
git push origin dev
