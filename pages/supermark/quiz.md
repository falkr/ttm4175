



---
type: nav
prev: ["All extensions", "index.html"]
---





# Documentation

A multiple choice questions that can be solved directly in the page.




<table class="table"><tbody><td>Python type</td><td>Quiz</td>
<tr></tr>
<td>type</td><td>quiz</td>
<tr></tr>
<td>Language</td><td><a href="#">YAML</a></td>
<tr></tr>
<td>Required fields</td><td>correct, false-1</td>
<tr></tr>
<td>Optional fields</td><td>question, title, false-2, false-3, result-correct, result-false, result-false-1, result-false-2, result-false-3</td>
<tr></tr>
<td>Post-Yaml Section</td><td>optional</td>
<tr></tr></tbody></table>






# Example

---
type: quiz
title: Example Quiz 1
question: Which of the alternatives is the best one?
correct: This is the right answer.
false-1: An fake answer.
false-2: Another fake answer.
false-3: Yet another fake anser.
result-correct: Correct. You selected the 
result-false-1: False. You selected a fake answer.
result-false-2: False. You selected another fake answer.
result-false-2: False. You selected yet another fake answer.
---






## Source Code

```yaml
---
type: quiz
title: Example Quiz 1
question: Which of the alternatives is the best one?
correct: This is the right answer.
false-1: An fake answer.
false-2: Another fake answer.
false-3: Yet another fake anser.
result-correct: Correct. You selected the 
result-false-1: False. You selected a fake answer.
result-false-2: False. You selected another fake answer.
result-false-2: False. You selected yet another fake answer.
---
```






# Example

---
type: quiz
title: Example Quiz 2
correct: This is the right answer.
false-1: An fake answer.
false-2: Another fake answer.
false-3: Yet another fake anser.
result-correct: Correct. You selected the 
result-false-1: False. You selected a fake answer.
result-false-2: False. You selected another fake answer.
result-false-2: False. You selected yet another fake answer.
---
Which of the alternatives is the best one?

* A list with one item
* Another item






## Source Code

```yaml
---
type: quiz
title: Example Quiz 2
correct: This is the right answer.
false-1: An fake answer.
false-2: Another fake answer.
false-3: Yet another fake anser.
result-correct: Correct. You selected the 
result-false-1: False. You selected a fake answer.
result-false-2: False. You selected another fake answer.
result-false-2: False. You selected yet another fake answer.
---
Which of the alternatives is the best one?

* A list with one item
* Another item
```



