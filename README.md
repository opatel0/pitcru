# PiTCRU
<details>
<summary>Screenshots</summary>
</details>
<details>
<summary>List of Technologies Used</summary>
</details>
<details>
<summary>Installation Instructions Used</summary>
</details>
<details>
<summary>Unsolved Problems and Development Hurdles</summary>
</details>
<details>
<summary>Prep Materials</summary>
![Pitch Deck](https://docs.google.com/presentation/d/1qpX5GW_Bafp2oBqJjIH_7ISXsjz8pVqTMe-U6UNrceg/edit#slide=id.p)<br>
Trello Board<br>
Wireframes<br>
ERD
</details>

<details>
<summary>How we git</summary>
We implement a feature branch workflow, the rules of which include: <br>
<ul>
	<li>All development work by a team member will be completed in a descriptively named branch</li>
	<li>Development work will only be added to the main project through branch merge pull requests</li>
	<li>All discussion and decision making will be tracked in pull request comments</li>
</ul>
Instructions for developing a new feature
<ol>
	<li>Select ticket from Trello board</li>
	<li>Navigate to local repo in terminal</li>
	<li>Run the following with no square brackets where new-branch-name matches Trello ticket name<pre>git branch [new-branch-name]</pre></li>
	<li>Set your local working branch to your new feature branch by running the following <pre>git checkout [new-branch-name]</pre></li>
	<li>Check that your active branch is your new feature by observing the output from the following command <pre>git branch</pre></li>
	<li>Push new branch to Github by running the following <pre>git push --set-upstream remote [new-branch-name]</pre>
	<li>Complete all development work in this branch (write functionality piece by piece and add, stage, commit between getting each piece working!)</li>
	<ul>
		For reference, here are the comments to 1. stage, 2. commit, and 3. push
		<li>Stage changes by running <pre>git add -A</pre>
		<li>Commit changes by running <pre>git commit -m "commit message"</pre></li>
		<li>Push changes by running<pre>git push</pre></li>
		<li><strong>CONTACT GIT GUY IMMEDIATELY IF YOU RUN INTO ISSUES YOU DO NOT KNOW HOW TO RESOLVE</strong></li>
	</ul>
	<li>After feature is fully developed, ensure all your commits are pushed to remote branch, and then submit pull request</li>
	<li>Assign reviewer and notify in communication channel that PR is ready for review</li>
	<li>Discuss/finalize changes in comments. If voice call is necessary to resolve certain topics, one of the attendees of that conversation must include notes from the conversation as a comment in the PR. Merge conflicts should also be handled in the Github PR UI, and should always be handled by at least two people.</li>
	<li>Reviewer confirms merge after approving PR</li>
</ol>
</details>