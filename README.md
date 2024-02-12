# PiTCRU
<details>
<summary>Screenshots</summary>

  <h3>Home Page</h3>  <img src="https://i.imgur.com/mIN62S4.png" width="700"> 
   <h3>About</h3>  <img src="https://i.imgur.com/fTCN2As.png" width="700"> 
   <h3>Sign Up Form</h3>  <img src="https://i.imgur.com/f1CPCpe.png" width="700"> 
   <h3>Login Page</h3>  <img src="https://i.imgur.com/XEEsCI5.png" width="700"> 
   <h3>Car Index</h3>  <img src="https://i.imgur.com/XrRzPcY.png" width="700"> 
  
</details>
<details>
<summary>List of Technologies Used</summary>
API Ninjas, bs4 (Beautiful Soup) , Django, Postgres, Neon, HTML, Python, CSS, Heroku, Python, Javascript, HTML, CSS, PostgreSQL, Django, 
</details>
<details>
<summary>Unsolved Problems and Development Hurdles</summary>
Thankfully there were only a few obstacles we encountered mainly with our static assets and the forms pages, which still remains unsolved. Other obstacles that we overcame were synching out database and api content on the screen.
</details>
<details>
<summary>Prep Materials</summary>
<h1>Pitch Deck</h1>
https://docs.google.com/presentation/d/1qpX5GW_Bafp2oBqJjIH_7ISXsjz8pVqTMe-U6UNrceg/edit#slide=id.p<br>
<h1>Trello Board</h1>https://trello.com/invite/b/ZwKB3WGc/ATTI825093ffdfe208138f2e6222500dcc912ADDC12A/pitcru<br>
<h1>Wireframes</h1>
<img src="https://i.imgur.com/ol7G6B6.png" width="700"> 
<img src="https://i.imgur.com/8QMKZi6.png" width="700"> 
<img src="https://i.imgur.com/j6GPgFs.png" width="700"> 
<img src="https://i.imgur.com/wGtDWAW.png" width="700"> 
<br>
<h1>ERD</h1><img src="https://i.imgur.com/NdtdEqh.png" width="700"> 
</details>

<details>
<summary>How we git</summary>
<h2>Feature Branch Workflow</h2>
We implement a feature branch workflow, the rules of which include: <br>
<ul>
	<li>All development work by a team member will be completed in a descriptively named feature branch</li>
	<li>Development work will only be added to the main project through branch merge pull requests</li>
	<li>All discussion and decision making will be tracked in pull request comments</li>
</ul>
<h2>Instructions</h2>
<ol>
	<li>
		<details>
			<summary>Review assigned ticket from Trello board</summary>
			<br><img src="./main_app/static/media/move_ticket.png" width="500px"><br>
		</details>
	</li>
	<li>Navigate to local repo in terminal</li>
	<li>
		<details>
			<summary>Refresh local main branch</summary>
			First, ensure your main branch is checked out by simply running the following <pre>git checkout main</pre>
			Next, sync your local main branch to the remote main branch by running the following <pre>git pull</pre>
			Next, output the status of your repo by running the following <pre>git status</pre>
			Finally, observe the output and check that your branch is up to date by confirming the following text appears in your git status output <br><img src="./main_app/static/media/git_status.png" width="500px"><br>
		</details>
	</li>
	<li>
		<details>
			<summary>Create New Feature Branch</summary>
			Run the following with no square brackets where new_branch_name is a descriptive name that correlates to your assigned Trello ticket<pre>git branch [new_branch_name]</pre>
			Set your local working branch to your new feature branch by running the following <pre>git checkout [new_branch_name]</pre>
			List all your branches created for this repo by running the following <pre>git branch</pre>
			Confirm your new feature branch is selected by ensuring it appears in the output list and has an asterisk next to it <br><img src="./main_app/static/media/branches.png" width="500px"> <br>
			Set your upstream branch by running the following <pre>git push -u origin <[new_branch_name]</pre>
			Push new branch to Github by running the following <pre>git push --set-upstream origin [new_branch_name]</pre>
			Check remote repository and assure new branch now appears in the list <br><img src="./main_app/static/media/remote.png" width="500px"><br>
			<strong>CONTACT GIT GUY IMMEDIATELY IF YOU RUN INTO ISSUES YOU DO NOT KNOW HOW TO RESOLVE</strong>
		</details>
	<li>
		<details>
			<summary>Develop Code in New Branch to Meet Trello Ticket Requirements</summary>
			Complete all development work in this branch (write functionality piece by piece and add, stage, commit between getting each piece working!)
			<ul>
				For reference, here are the comments to 1. stage, 2. commit, and 3. push
				<li>Stage changes by running <pre>git add -A</pre>
				<li>Commit changes by running <pre>git commit -m "commit message"</pre></li>
				<li>Push changes by running<pre>git push</pre></li>
			</ul>
			<strong>CONTACT GIT GUY IMMEDIATELY IF YOU RUN INTO ISSUES YOU DO NOT KNOW HOW TO RESOLVE</strong>
		</details>
	</li>
	<li>
		<details>
			<summary>Submit Pull Request and Notify Reviewers</summary>
			Run the following <pre>git log</pre>
			Compare log output to remote branch commit history and ensure the most recent commit IDs match <img src="./main_app/static/media/compare_commits.png" width="500px"> <br>
			If remote repo not up to date, refer to step 5 to stage, commit, and push changes.<br>
			Once local and remote branches are sync'd, submit pull request <br> <img src="./main_app/static/media/pull_request.png" width="500px"> <br>
			Notify reviewer(s) via Discord group chat that PR is ready for review <br>
			<strong>CONTACT GIT GUY IMMEDIATELY IF YOU RUN INTO ISSUES YOU DO NOT KNOW HOW TO RESOLVE</strong>
		</details>
	</li>
</ol>
<strong>NOTE:</strong> All discussion regarding PRs must be logged in PR comments. If voice call is necessary to resolve certain topics, one of the attendees of that conversation must include notes from the conversation as a comment in the PR. Merge conflicts should also be handled in the Github PR UI, and should always be handled by at least two people.</li>
</details>
<details>
	<summary>How we Seed(Installation Instructions)</summary>
	<h2>Follow the following steps</h2>
	<ul>
		<li>First make sure there isnt any changes that havent been migrated<pre>python3 manage.py makemigrations</pre>
		<li>Migrate any changes that may be pending<pre>python3 manage.py migrate</pre>
		<li>Drop your db through the terminal<pre>dropdb pitcru</pre>
		<li>Create your db through the terminal<pre>createdb pitcru</pre>
		<li>If you dont have requests folder download using the follow<pre>pip3 install requests</pre>
		<li>Enter the python shell<pre>python3 manage.py shell</pre>
		<li>Import the main app models folder <pre>from main_app.models import *</pre>
		<li>Run the seeding function <pre>seed_db()</pre>
	<ul>
</details>
<details>
	<summary>Next Steps</summary>
	<li>Actualize racing game car selection screen design for details page</li>
	<li>Refactor backend to implement industry standard API such as KBB</li>
	<li>Resolve issues with animation on pages with forms</li>
	<li>Shorten form on homepage and expose button to toggle between simple and advanced search</li>
</details>
