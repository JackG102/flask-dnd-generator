# Flask DND Generator

## Goals and Descriptions

### Project Description
The actual project is to generate helpful content for Dungeon Masters in role playing games. Currently, I am working on auto generating non-playable characters and taverns. The current approach is to have txt files that are used to generate names and such. The application looks into each of these files and often pulls out a line at random to be used for an NPC or tavern.

The .txt lists are rough and ready, which makes some of the auto-generations humorous but that's the fun of it.

The end goal for this program is to continue adding components that can be auto generated for the DM. Right now, I am starting with NPCs, then a number of places like taverns, shops, town squares that are populated by NPCs that are generated. Then, once that is completed move on to generating, villages, towns, and cities with the building blocks that I have completed.  See Project Roadmap for further how I am starting to outline the project.

### Personal Goal
This project is to help me learn the basics of Python and the world of web development in Python.  I didn't want to be stuck doing tutorials, so I bought some general Python books and started learning the basics.  I eventually wanted to transition to making a website in Python.  I settled on Flask for this project, because it felt most like writing Python as opposed to framework-specific code like Django.  

## Project Roadmap

## Who am I
I am Drupal developer doing this project in my spare time early in the morning, late at night, or a few minutes in between things.  I have full-time job and a new parent! 

The website uses Flask, which I found to be the simplest tool for what this website intends to be: a website wrapper for the DND Generator module that I am writing in Python.  Essentially this project started out as a Python script that could be invoked by the command line interface (CLI); however, I realized if I wanted others to use this as well, making it a website would be better.  Before you say that perhaps this would be better as a React application embedded in a Flask site, I agree!  But, once again, the goal of this project is to learn Python, not React :).

## Deployment and Infrastructure
I chose Google Cloud Platform using there Cloud Run service, which I learned is shockingly easy for simple applications in Python. I integrated it with the Github repository, configured a build trigger, and selected the option where Cloud Run configured and built containers for Python automatically, and away it went.  To be honest, it was shockingly easy for this application.  I like it when my tools do the things that I need and then get out of the way, so I can focus on application work.
  
## Shout Outs:
No software is an island, but I wanted to call out repositories that I used to generate my txt files and get some styling implemented quickly without writing lots of CSS or implementing a big library like Bootstrap.

TXT lists that I started with to help generate content:
- https://github.com/arineng/arincli/blob/master/lib/male-first-names.txt
- https://github.com/arineng/arincli/blob/master/lib/female-first-names.txt
- https://github.com/arineng/arincli/blob/master/lib/last-names.txt
- https://gist.github.com/wsc/10834595
- https://gist.github.com/cjwebb/3c114a60e2ec2872e1cd

Simple CSS library for styling 
- https://simplecss.org/