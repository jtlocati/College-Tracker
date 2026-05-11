# Match Map

A Django web app that helps high school students build their college list with the help of **Accepto Unit-01**, an AI assistant powered by OpenAI's GPT-5. Students fill out a detailed academic profile (GPA, test scores, AP exams, activities, awards, recommenders, intended major, preferred school type), and Accepto generates a tailored list of reach / match / safety schools with deadlines, application URLs, and admission likelihoods. Everything is tracked in a per-user dashboard inspired by the layout of popular college-tracking tools.

Built by Jet Locati.

---

## Features

- **Account system** — sign up, log in, and log out using Django's built-in auth.
- **Profile builder** — captures geographic info, GPA per year (unweighted & weighted), SAT/ACT, up to 10 activities + descriptions, 5 awards, 4 recommender slots, intended major, preferred college environment, and a free-form background note. AP exams use a dynamic formset (click "+ Add Exam" for each test you've taken).
- **Accepto college recommendations** — generates 10 reach, 10 match, and 5 safety schools in a structured format and stores them as per-user `Colleges` rows.
- **Tracker dashboard (`/home/`)** — sortable, filterable table of every saved school with editable plan (EA/ED/REA/Reg), deadline date, status, and notes; computed "days until deadline"; tier badges; portal link; and per-row delete plus a master reset.
- **Loading overlay** — shows while Accepto generates results so the page doesn't feel frozen.

---

## Tech Stack

- **Backend**: Django 5.1, Python 3.11
- **Database**: PostgreSQL hosted on render disk
- **AI**: OpenAI Python SDK (`gpt-5` model)
- **Frontend**: vanilla HTML, CSS, and a sprinkle of JS — no framework
- **Auth**: `django.contrib.auth` with `UserCreationForm`

---

## Project Layout