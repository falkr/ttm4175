# How to Teach a TTM4175 Unit

This note summarizes guidelines and tips on how to structure and run a unit in this course.
Ideally, all units are structured similarly to provide a routine to students that reinforces good learning habits. 

# Unit Design

Ideally, a unit should be designed starting with the specific learning goals in mind, and then backwards develop lab activities, class activities, RAT questions and preparation material to ensure constructive alignment.

The unit should make its specific learning goals explicit.
These should contribute to the [overall learning goals of the course](https://www.ntnu.edu/studies/courses/TTM4175#tab=omEmnet), but should be more specific and more concrete.

The unit is structured in four parts, explained in the following:

1. Preparation
2. RAT
3. Lecture
4. Lab


# Part 1: Preparation

The preparation material should be of a form and extend that students can manage to work through it within about 2 hours of homework.
The material can be videos, articles or scripts.
The preparation material should be presented in a cohesive way, that means, including a comment on why a specific video or article is relevant and what to focus on. 


# Part 2: Readiness Assurance Tests (RATs)

Students meet up to class time (Fridays 8:15). 
They sit in teams of 6 students at tables.
The first 30 to 45 minutes are used for the RATs.

Prepare 10 multiple choice questions for the preparation material.
Each question should have four answer alternatives (A, B, C, D), where one is the best answer. 
Write the questions in [this format](https://falkr.github.io/teampy/write-rats.html), or copy them from previous years.

For the individual test, we use the [teampy program](https://falkr.github.io/teampy) to generate paper copies of the test. 

---
type: link
link: "https://falkr.github.io/teampy/"
title: "Teampy App for Printing RATs"
icon: gear-fill
---

For the team test, the teams of 6 students solve the same test again.
They use the [Nøtteknekker App](https://apps.apple.com/no/app/n%C3%B8tteknekker/id1667651492). One of the students in the team installs it on their iPhone, and the app reveals the correct answer of each question.

---
type: link
link: "https://apps.apple.com/no/app/n%C3%B8tteknekker/id1667651492"
title: "Nøtteknekker on the App Store"
icon: apple
---


# Part 3: Lecture Parts

After the RAT, you continue with an expansion of the preparation material, discussion of more advanced issues, exercises and demos in the classroom or teamwork tasks.

One recurring request of students is a clear link between the material taught in the preparation and lecture time and the lab. To achieve that, we found three tips to be helpful:
1. Express at the beginning of a unit why we learn something and why it is relevant later in studies and working life.
2. Have a good alignment between lab, lecture and preparation material.
3. Introduce the lab at the end of the lecture and explain its goals, and how it related to the content covered so far.


# Part 4: Lab

The lab is in [Sahara](https://link.mazemap.com/pR24A3cf) from 10:15 to 14:00.
Students sit in teams of three.

It is hard to find the right level of difficulty for the lab, and how much description and instructions and help to provide.
Too much help, and students feel that they only have to follow instructions, executing one command after the other. Too little help and students get frustrated by lack of progress or too difficult tasks.
With feedback from the reference groups over the years, we found the following techniques helpful to make labs more robust with respect to difficulty:

* Clearly expressed milestones
* Provision of tips and hints
* Clear labels on optional tasks


### Expressing Milestones

Dependong on the specific task, it can be helpful to express milestones that the students can use as checkpoints during their work, so that the lab doesn't feel like an endless, unstructured task. Example:

:milestone: **Milestone 1:** Your network is configured correctly and you can reach all the nodes.


### Providing Tips and Hints

Provide tips where it makes sense. Example:

:tip: Provide tips with optional but helpful information where it makes sense.


It is also possible to provide *hints*, which are only visible after the students click a button to reveal them. Example:

---
type: hint
title: Hint about Something
---
Within the content you can have lists:
* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16


### Optional Tasks

Labs may include optional tasks. These should be clearly marked as "optional".


## Providing Hints for the Report

Students must write and deliver a report for the labs. They should write about how they solved tasks and reflect about insights gained. Where possible you can also include hints on what to write about additionally in the reports. Example:

:report: For the report, include a screenshot of your terminal and explain the different lines in detail.


## Breaks

The lab lasts from 10:15 to 14:00.
It's a good idea to remind students to take breaks, and to organize common breaks when they are needed. 
It may also be a good idea to empty the room at least once completely and let some fresh air inside.


# Website

Each unit is published in its own folder on the website. It should follow the same structure, so students know where to find what.

:tree:
- course/
	- pages/
		- index.md
		- hello.md
	    - unit-p1/
			- index.md
			- preparation-1.md
			- preparation-2.md
			- teamwork-1.md
			- teamwork-2.md
			
			
Main Page (index.md):
- Title and short introduction to the unit
- Short list of specific learning goals
- Links to all the preparation pages
- Links to all teamwork (lab) pages
- Optional material or ides for follow up