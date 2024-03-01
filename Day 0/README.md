# Day 0

Set up the environment, created the repo, trying to decide what this would be but I'll just speak my thoughts and see how it turns out.

Not really important but looked up a few commands for markdown and had a thought about if there was any similarity to HTML but M markup and not markdown so my guess is there's not much other than 'mark' haha.

Thinking of starting with some review of basic data structures and algorithms (DSA) in python leetcode problems mainly because it's been a while since I last worked on them and I should practice if I want to get better and more fluent with my skills. 

Approach to take for these interviewesque problems\
Looking at these steps side by side when tackling the problems

1. Thinking about a problem systematically
2. Envision different inputs, outputs, and edge cases
3. Communicate Ideas clearly
4. Convert thoughts into code

The Strategy
1. Stating the problem. Identify format of inputs and outputs
2. Come up with sample inputs and resulting outputs that cover edge cases
3. Come up with the correct solution and explain each step in simple english
4. Implement and test. Fix any bugs when applicable
5. Identify complexity and address any inefficiencies
6. Use better algorithm/technique to improve runtime and address inefficency


Trying some git techniques like committing to a branch instead of directly to main first. So watching a git branch tutorial to figure this out

Notes from [Git Branch Tutorial](https://www.youtube.com/watch?v=e2IbNHi4uCI&ab_channel=freeCodeCamp.org)\
Head: active branch
Creating a branch: **git branch (name)**\
Check existing branches: git branch
Checking which branch is active: git status\
Switch branch: git switch {name}\
Rename current: git branch -m (new_name)\
Rename any: git branch -m {old_name} {new_name}
Upload to repo: git push -u origin (current branch)\
-u  flag establishes a tracking branch

**Review Tracking Connections and write more about it**

Show which changes need to be added (ahead -> havent pushed to remote; behind -> remote has new info). Determine how current your data is\
git branch -v

Delete Branches (cant delete head branch)\
For Local\
git branch -d {branch_name}\
For remote\
git push origin --delete {name}

Merge branches: Integrate changes from another branch -> Head branch\
Commands:\
git switch main\
git merge {branch_name}


