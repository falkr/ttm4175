<div>
<table class="table table-sm">
<caption style=""></caption>
<thead>
<tr class="row-1">
<th></th><th>Subscription Topic</th><th>Receive a/b/c/d ?</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-1">
<td class="column-1">1</td><td class="column-2">#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-2">
<td class="column-1">2</td><td class="column-2">+/+/+</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-3">
<td class="column-1">3</td><td class="column-2">+/+/+/+</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-4">
<td class="column-1">4</td><td class="column-2">+/b/c/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-5">
<td class="column-1">5</td><td class="column-2">+/b/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-6">
<td class="column-1">6</td><td class="column-2">a/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-7">
<td class="column-1">7</td><td class="column-2">a/+/+/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-8">
<td class="column-1">8</td><td class="column-2">a/+/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-9">
<td class="column-1">9</td><td class="column-2">a/b/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-10">
<td class="column-1">10</td><td class="column-2">a/b/c</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-11">
<td class="column-1">11</td><td class="column-2">a/b/c/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-12">
<td class="column-1">12</td><td class="column-2">a/b/c/d/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-13">
<td class="column-1">13</td><td class="column-2">a/b/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-14">
<td class="column-1">14</td><td class="column-2">b/+/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-15">
<td class="column-1">15</td><td class="column-2">a/b/c/d/+</td><td><input type="checkbox" class="form-check-input"></td></tr>
</tbody>
</table>
</div>



---
type: hint
title: Solution for the exercise above. Click to reveal. 
---
<div>
<table class="table table-sm">
<caption style=""></caption>
<thead>
<tr class="row-1">
<th></th><th>Subscription Topic</th><th>Receive a/b/c/d ?</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-1">
<td class="column-1">1</td><td class="column-2">#</td><td>Yes!</td></tr>
<tr class="row-2">
<td class="column-1">2</td><td class="column-2">+/+/+</td><td>No! We only subscribe to topics that include 3 levels.</td></tr>
<tr class="row-3">
<td class="column-1">3</td><td class="column-2">+/+/+/+</td><td>Yes!</td></tr>
<tr class="row-4">
<td class="column-1">4</td><td class="column-2">+/b/c/#</td><td>Yes!</td></tr>
<tr class="row-5">
<td class="column-1">5</td><td class="column-2">+/b/c/d</td><td>Yes!</td></tr>
<tr class="row-6">
<td class="column-1">6</td><td class="column-2">a/#</td><td>Yes!</td></tr>
<tr class="row-7">
<td class="column-1">7</td><td class="column-2">a/+/+/d</td><td>Yes!</td></tr>
<tr class="row-8">
<td class="column-1">8</td><td class="column-2">a/+/c/d</td><td>Yes!</td></tr>
<tr class="row-9">
<td class="column-1">9</td><td class="column-2">a/b/#</td><td>Yes!</td></tr>
<tr class="row-10">
<td class="column-1">10</td><td class="column-2">a/b/c</td><td>No! The publishing topic also includes a 'd', which does not match, even at the end.</td></tr>
<tr class="row-11">
<td class="column-1">11</td><td class="column-2">a/b/c/#</td><td>Yes!</td></tr>
<tr class="row-12">
<td class="column-1">12</td><td class="column-2">a/b/c/d/#</td><td>Yes!</td></tr>
<tr class="row-13">
<td class="column-1">13</td><td class="column-2">a/b/c/d</td><td>Yes!</td></tr>
<tr class="row-14">
<td class="column-1">14</td><td class="column-2">b/+/c/d</td><td>No! The first b of the subscription topic does not match the first a of the publishing topic.</td></tr>
<tr class="row-15">
<td class="column-1">15</td><td class="column-2">a/b/c/d/+</td><td>No! The last plus implies that there should be another level for the topic, after the d/.</td></tr>
</tbody>
</table>
</div>